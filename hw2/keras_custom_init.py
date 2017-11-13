from keras.engine.topology import Layer
from keras import backend as K


class Layer_BOS_PrevLabels(Layer):
    def __init__(self, idxBOS, **kwargs):
        super(Layer_BOS_PrevLabels, self).__init__(**kwargs)
        self.idxBOS = idxBOS

    def get_config(self):
        config = {'idxBOS': self.idxBOS}
        base_config = super(Layer_BOS_PrevLabels, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    def call(self, inputs):
        # For each caption, remove the last word vector and append a zero-vector to the beginning.
        _inputs = K.temporal_padding(inputs[:, 0:-1, :], padding=(1, 0))
        # _inputs[:, 0, idxBOS] += 1.
        scatter = K.tf.scatter_nd([[0, self.idxBOS]], K.tf.constant([1.]), K.tf.constant(_inputs.shape.as_list()[1: ]))
        return _inputs + scatter


class Layer_Slicer(Layer):
    def __init__(self, units, iPart, **kwargs):
        super(Layer_Slicer, self).__init__(**kwargs)
        self.units = units
        self.iPart = iPart
    def get_config(self):
        config = {'units': self.units, 'iPart': self.iPart}
        base_config = super(Layer_Slicer, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))
    def call(self, inputs):
        return inputs[:, self.iPart*self.units : (self.iPart+1)*self.units]
    def compute_output_shape(self, input_shape):
        return (None, self.units)


# Modified from: https://github.com/chmp/flowly/blob/master/flowly/ml/layers.py#L156
# Lots of bugfixes (on Keras 2.0.7).
from keras.engine import InputSpec
from keras.layers import Layer, Input
from keras.engine.topology import Container
class RecurrentWrapper(Layer):
    """Define a recurrent model in terms of a general transition model.
    A simple RNN for example would be expressed as:
        hidden = Input((128,))
        input = Input((10,))
        x = Dense(128, activation='relu')(input)
        x = Add()([hidden, x])
        new_hidden = Activation('sigmoid')(x)
        rnn = RecurrentWrapper(
            input=[input],
            output=[new_hidden],
            bind={hidden: new_hidden},
            input_shape=(None, 10),
            return_sequences=True,
        )
    .. note::
        this class is still highly in flux and does only work with tensoflow atm.
    """
    def __init__(
            self, input, output, bind,
            sequence_input=(),
            stateful=False,
            return_sequences=False,
            # Fixed.
            _step_model=None,
            _len_input=None,
            _len_sequence_input=None,
            _final_output_map=None,
            **kwargs
    ):
        if stateful:
            raise RuntimeError('RecurrentWrapper does not support statefule transforms currently')

        self.supports_masking = True
        self.stateful = stateful
        self.return_sequences = return_sequences

        # Fixed for load_model.
        if False == all(x == None for x in [input, output, bind, sequence_input]):
            self.bindings = bind
            self.external_input = self._ensure_list(input)
            self.external_sequence_input = self._ensure_list(sequence_input)
            self.external_output = self._ensure_list(output)

            self.state_input, self.state_output, self.final_output_map = self._build_recurrence_wrapper(
                self.external_input + self.external_sequence_input,
                self.external_output,
                self.bindings,
                self._build_input,
            )

            self.step_model = Container(
                inputs=self.external_input + self.external_sequence_input + self.state_input,
                outputs=self.state_output,
            )

            # Fixed (extra).
            self.len_external_input = len(self.external_input)
            self.len_external_sequence_input = len(self.external_sequence_input)
            # These have be useless.
            self.bindings = None
            self.external_input = None
            self.external_sequence_input = None
        else:
            self.step_model = _step_model

            self.len_external_input = _len_input
            self.len_external_sequence_input = _len_sequence_input

            self.state_input = self.step_model.input[self.number_of_inputs : ]
            self.state_output = self.step_model.output
            self.final_output_map = _final_output_map

            self.external_output = [self.state_output[idx] for idx in self.final_output_map]

        # self.losses = []
        super(RecurrentWrapper, self).__init__(**kwargs)

    # Fixed.
    @property
    def losses(self):
        if self.built is True:
            return self.step_model.losses
        return []

    def getIWant(self):
        return self.state_input, self.state_output, self.final_output_map, self.step_model

    @property
    def number_of_inputs(self):
        return self.len_external_input + self.len_external_sequence_input

    def compute_output_shape(self, input_shape):
        head = tuple(input_shape[:2] if self.return_sequences else input_shape[:1])

        def _shape(output):
            tail = (K.int_shape(output)[1],)
            return head + tail

        return [_shape(output) for output in self.external_output]

    def compute_mask(self, input, mask=None):
        return [
            (mask if self.return_sequences else None)
            for _ in self.external_output
        ]

    def get_constants(self, x):
        return []

    def reset_states(self):
        pass

    def get_config(self):
        # Fixed.
        config = {'input': None,
                  'output': None,
                  'bind': None,
                  'sequence_input': None,
                  'stateful': self.stateful,
                  'return_sequences': self.return_sequences,
                  '_len_input': self.len_external_input,
                  '_len_sequence_input': self.len_external_sequence_input,
                  '_final_output_map': self.final_output_map}
        step_config = self.step_model.get_config()
        base_config = super(RecurrentWrapper, self).get_config()
        return dict(list(base_config.items()) + list(step_config.items()) + list(config.items()))
        # return self.step_model.get_config()

    # Fixed.
    @classmethod
    def from_config(cls, config, custom_objects=None):
        step_model = Container.from_config(config, custom_objects)
        config.pop('name')
        config.pop('layers')
        config.pop('input_layers')
        config.pop('output_layers')
        return cls(_step_model=step_model, **config)

    def build(self, input_shape):
        if self.number_of_inputs > 1:
            self.input_spec = [InputSpec(shape=shape) for shape in input_shape]

        else:
            self.input_spec = [InputSpec(shape=input_shape)]

        self.step_model.build(input_shape)

        self._trainable_weights.extend(self.step_model.trainable_weights)
        self._non_trainable_weights.extend(self.step_model.non_trainable_weights)
        # self.constraints.update(self.step_model.constraints)
        # self.losses.extend(self.step_model.losses)

        self.built = True

    def get_initial_states(self, x):
        return [
            self._get_initial_state(x, inp)
            for inp in self.state_input
        ]

    def call(self, x, mask=None):
        x = self._ensure_list(x)
        initial_states = self.get_initial_states(x)

        recurrent_inputs = x[:self.len_external_input]
        sequence_inputs = x[self.len_external_input:]

        def step(states, inputs):
            full_input = self._ensure_list(inputs) + sequence_inputs + self._ensure_list(states)
            new_states = self.step_model.call(full_input)
            return self._ensure_list(new_states)

        recurrent_inputs = self._swap_time_and_samples(recurrent_inputs)

        outputs = K.tf.scan(step, recurrent_inputs, initial_states)
        outputs = [outputs[idx] for idx in self.final_output_map]

        if self.return_sequences:
            return self._possibly_scalar(self._swap_time_and_samples(outputs))

        return self._possibly_scalar([output[-1] for output in outputs])

    @staticmethod
    def _get_initial_state(x, inp):
        # TODO: check that all x have the same number of samples / timesteps
        # TODO: test that x has 3 dimensions and inp has two dimensions
        x = x[0]
        input_dim = int(inp.get_shape()[1])

        # copied from keras. Recurrent.get_initial_state
        initial_state = K.zeros_like(x, dtype=inp.dtype)  # (samples, timesteps, input_dim)
        initial_state = K.sum(initial_state, axis=(1, 2))  # (samples,)
        initial_state = K.expand_dims(initial_state)  # (samples, 1)
        return K.tile(initial_state, [1, input_dim])  # (samples, output_dim)

    @staticmethod
    def _swap_time_and_samples(inputs):
        return [
            K.tf.transpose(inp, [1, 0, 2])
            for inp in inputs
        ]

    @staticmethod
    def _ensure_list(obj):
        return list(obj) if isinstance(obj, (list, tuple)) else [obj]

    @staticmethod
    def _possibly_scalar(obj):
        return obj[0] if len(obj) == 1 else obj

    @staticmethod
    def _build_recurrence_wrapper(external_input, external_output, bind, build_input):
        """
        - the step model always returns the full state
        :return:
            state_input, state_output, final_output_map
        """
        state_input = []
        state_output = []

        bind = list(bind.items())

        for bound_input, bound_output in bind:
            if bound_input in external_input:
                raise ValueError('cannot bind an external input')

            state_input.append(bound_input)
            state_output.append(bound_output)

        for output in external_output:
            if output in state_output:
                continue

            state_input.append(build_input(output))
            state_output.append(output)

        final_output_map = [state_output.index(item) for item in external_output]

        return state_input, state_output, final_output_map

    @staticmethod
    def _build_input(output):
        return Input(output.shape[1:], dtype=output.dtype)


def orgCE(y_true, y_pred):
    return K.categorical_crossentropy(y_true, y_pred)

def my_categorical_crossentropy(y_true, y_pred):
    # [Shape]
    # y_true: (?, maxText, |Vocab|)
    # mask:   (?, maxText)
    # cateCE: (?, maxtText)

    # mask = numpy.all(y_true == 0, axis=-1)
    mask = K.tf.count_nonzero(y_true, axis=-1)
    mask = K.cast(K.tf.where(K.tf.equal(mask, 0), x=K.tf.zeros_like(mask), y=K.tf.ones_like(mask)),
                  K.floatx())

    nVal = K.cast(K.tf.count_nonzero(mask), K.floatx())     # #valid_label.
    size = K.cast(K.tf.size(mask), K.floatx())              # #total_label.
    mask *= size / nVal                                     # corrected for each batch.
    return mask * K.categorical_crossentropy(y_true, y_pred)

def myAcc(y_true, y_pred):
    mask = K.tf.count_nonzero(y_true, axis=-1)
    mask = K.cast(K.tf.where(K.tf.equal(mask, 0), x=K.tf.zeros_like(mask), y=K.tf.ones_like(mask)),
                  K.floatx())

    nVal = K.cast(K.tf.count_nonzero(mask), K.floatx())     # #valid_label.
    size = K.cast(K.tf.size(mask), K.floatx())              # #total_label.
    mask *= size / nVal                                     # corrected for each batch.
    # https://github.com/fchollet/keras/blob/master/keras/metrics.py
    return mask * K.cast(K.equal(K.argmax(y_true, axis=-1),
                                 K.argmax(y_pred, axis=-1)),
                         K.floatx())
