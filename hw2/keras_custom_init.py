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
