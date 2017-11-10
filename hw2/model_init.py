"""
minCaption = 5
maxCaption = 37
minText    = 1
maxText    = 40
|Vocab|    = 6130 + 2(^$)import numpy
"""


import numpy
import sys
import re
import json
from keras.utils import np_utils


import os
try:
    os.stat('models/')
except:
    os.mkdir('models/')

try:
    dataPath = sys.argv[1]
except:
    dataPath = 'MLDS_hw2_data/'


with open(dataPath + '/training_label.json') as file:
    labelFile = json.load(file)

minText   = 1000
maxText   = 0
cnt       = 2
vocab2num = {'.': 0, '^': 1}    # <EOS>: 0, <BOS>: 1.
num2vocab = ['.', '^']
instances = []
captions  = []
for video in labelFile:
    vid = video['id']
    captions += [ [] ]
    for caption in video['caption']:
        texts   = re.findall(r'\w.*?(?=[^\w]*\s|[^\w]*$)', caption)
        nText   = len(texts)
        minText = min(minText, nText)
        maxText = max(maxText, nText)
        for text in texts:
            text = text.lower()
            if text not in vocab2num:
                vocab2num[text] = cnt
                num2vocab += [ text ]
                cnt += 1
        texts = [ vocab2num[text.lower()] for text in texts ]
        captions[-1] += [ texts ]
    instances += [ numpy.load(dataPath + '/training_data/feat/' + vid + '.npy') ]

del labelFile

# (nVideo, nFrame, nFeature) = (1450, 80, 4096)
instances = numpy.array(instances, dtype='float16')


for i in range(len(captions)):
    videoCaps = captions[i]
    for j in range(len(videoCaps)):
        caption = videoCaps[j] + [0]
        # caption += [0] * (maxText - len(caption))   # Padding.


def getOneHotLabels_RandChoicePerVideo(captions, num_classes):
    labels = []
    for videoCaps in captions:
        idx     = numpy.random.randint(len(videoCaps))
        caption = videoCaps[idx]
        # labels  += [ np_utils.to_categorical(caption, num_classes=num_classes) ]
        labels  += [ numpy.concatenate(
            ( np_utils.to_categorical(caption, num_classes=num_classes),
              numpy.zeros( (maxText-len(caption), num_classes) ) ),     # Dummy inputs.
            axis=0
        ) ]
    return numpy.array(labels)


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
