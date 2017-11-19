from keras.engine.topology import Layer
from keras import backend as K


class BOSPadding(Layer):
    def __init__(self, idxBOS, **kwargs):
        super(BOSPadding, self).__init__(**kwargs)
        self.idxBOS = idxBOS

    def get_config(self):
        config = {'idxBOS': self.idxBOS}
        base_config = super(BOSPadding, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    def call(self, inputs):
        # For each caption, remove the last word vector and append a zero-vector to the beginning.
        _inputs = K.temporal_padding(inputs[:, 0:-1, :], padding=(1, 0))
        # _inputs[:, 0, idxBOS] += 1.
        scatter = K.tf.scatter_nd([[0, self.idxBOS]], K.tf.constant([1.]), K.tf.constant(_inputs.shape.as_list()[1: ]))
        return _inputs + scatter


class Slicer(Layer):
    def __init__(self, units, iPart, **kwargs):
        super(Slicer, self).__init__(**kwargs)
        self.units = units
        self.iPart = iPart

    def get_config(self):
        config = {'units': self.units, 'iPart': self.iPart}
        base_config = super(Slicer, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    def call(self, inputs):
        return inputs[:, self.iPart*self.units : (self.iPart+1)*self.units]

    def compute_output_shape(self, input_shape):
        return (None, self.units)


class ArgmaxOneHot(Layer):
    def __init__(self, **kwargs):
        super(ArgmaxOneHot, self).__init__(**kwargs)

    def call(self, inputs):
        classes = K.argmax(inputs, axis=-1)
        return K.tf.one_hot(classes, depth=inputs.shape.as_list()[-1])


from keras.layers.merge import _Merge
class ScheduleSampling(_Merge):
    def __init__(self, decay_param, **kwargs):
        with K.name_scope(self.__class__.__name__):
            self.iterations  = K.variable(0, dtype='int64', name='iterations')
            self.decay_param = K.constant(decay_param, name='decay_param')
        super(ScheduleSampling, self).__init__(**kwargs)
        self.uses_learning_phase = True

    def build(self, input_shape):
        super(ScheduleSampling, self).build(input_shape)
        self._non_trainable_weights += [ self.iterations ]
        self.built = True

    def get_config(self):
        config = {'decay_param': float(K.get_value(self.decay_param))}
        base_config = super(ScheduleSampling, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))

    def _merge_function(self, inputs):
        if len(inputs) != 2:
            raise ValueError('`ScheduleSampling` layer should be called '
                             'on exactly 2 inputs')
        if inputs[0].shape.as_list() != inputs[1].shape.as_list():
            raise ValueError('`ScheduleSampling` layer should be called '
                             'on inputs of the same shape')

        training = self.training
        y_pred, y_true = inputs

        # Prepare mixed predictions.
        shape   = y_pred.shape.as_list()
        tfShape = K.shape(y_pred)
        # Find zero-vectors in y_true and give thme the mask value 1.
        zero_mask = K.tf.count_nonzero(y_true, axis=-1)
        zero_mask = K.cast(K.tf.where(K.tf.equal(zero_mask, 0),
                                      x=K.tf.ones_like(zero_mask),
                                      y=K.tf.zeros_like(zero_mask)),
                           K.floatx())
        # Find BOS-vectors in y_true and give thme the mask value 1.
        # Note that argmax(BOS) = 1. Check model_init.py.
        BOS_mask = K.argmax(y_true, axis=-1)
        BOS_mask = K.cast(K.tf.where(K.tf.equal(BOS_mask, 1),
                                     x=K.tf.ones_like(BOS_mask),
                                     y=K.tf.zeros_like(BOS_mask)),
                          K.floatx())
        # Aggregate extra masks.
        # Cover y_pred with zero and BOS vectors in y_true.
        # IMPORTANT: This works at testing phase!
        # Even though at training phase, they must be chosen.
        # This is meaningful for using padding.
        extra_mask = zero_mask + BOS_mask
        extra_mask = K.expand_dims(extra_mask, axis=-1)
        extra_mask = K.repeat_elements(extra_mask, shape[-1], axis=len(shape)-1)
        y_pred     = K.tf.where(K.tf.equal(extra_mask, 0),
                                x=y_pred,
                                y=y_true)

        mask   = K.random_uniform(shape=tfShape[ :-1], minval=0.0, maxval=1.0)
        mask   = K.expand_dims(mask, axis=-1)
        # mask   = K.repeat_elements(mask, shape[-1], axis=-1)      # fails on workstation GPU but works on CPU.
        mask   = K.repeat_elements(mask, shape[-1], axis=len(shape)-1)
        y_samp = K.tf.where(K.tf.greater(mask, self.threshold),
                            x=y_pred,
                            y=y_true)

        self.add_update(K.update_add(self.iterations,
                                     K.cast(K.in_train_phase(1, 0, training=training),
                                            dtype='int64')),
                        inputs)

        return K.in_train_phase(y_samp, y_pred, training=training)

    def call(self, inputs, training=None):
        self.training = training
        return super(ScheduleSampling, self).call(inputs)

    @property
    def threshold(self):
        # Inverse sigmoid decay.
        # When i = k*log(k), threshold = 0.5.
        k = self.decay_param
        i = K.cast(self.iterations, K.floatx())
        return k / (k + K.tf.exp(i/k))


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
        self.uses_learning_phase = True    # for Dropout, BatchNormalization, ScheduleSampling.

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
            self.step_model = _step_model   # built in RecurrentWrapper.from_config().
            del _step_model

            self.len_external_input = _len_input
            self.len_external_sequence_input = _len_sequence_input

            self.state_input = self.step_model.input[self.number_of_inputs : ]
            self.state_output = self.step_model.output
            self.final_output_map = _final_output_map

            self.external_output = [self.state_output[idx] for idx in self.final_output_map]

            if len(self.state_input) < len(self.state_output):
                # Modified from part of RecurrentWrapper._build_recurrence_wrapper().
                # Select from the subset of self.external_output, whose items have no related items in self.state_input.
                for idx in self.final_output_map:
                    # Ignore existed (input, output) pairs.
                    if idx != len(self.state_input):
                        continue
                    output = self.state_output[idx]

                    self.state_input.append(self._build_input(output))  # a dummy input to cancel output recurrence in call().

                # Rebuild step_model.
                inputs = self.step_model.input[ : self.number_of_inputs]
                self.step_model = Container(
                    inputs=inputs + self.state_input,
                    outputs=self.state_output,
                )

        # self.losses = []
        super(RecurrentWrapper, self).__init__(**kwargs)

    # Fixed.
    @property
    def losses(self):
        if self.built is True:
            return self.step_model.losses
        return []

    @property
    def number_of_inputs(self):
        return self.len_external_input + self.len_external_sequence_input

    def compute_output_shape(self, input_shape):
        # Fixed for multi-inputs.
        if self.number_of_inputs > 1:
            input_shape = input_shape[0]

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

            state_input.append(build_input(output))     # a dummy input to cancel output recurrence in call().
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
