"""
minCaption = 5
maxCaption = 37
minText    = 1+1
maxText    = 40+1
|Vocab|    = 6130 + 2(^$)import numpy
"""


from keras_custom_init import *
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
        texts = [ vocab2num[text.lower()] for text in texts ] + [0]
        captions[-1] += [ texts ]
    instances += [ numpy.load(dataPath + '/training_data/feat/' + vid + '.npy') ]
minText += 1    # Including <EOS>.
maxText += 1    # Including <EOS>.

del labelFile

# (nVideo, nFrame, nFeature) = (1450, 80, 4096)
instances = numpy.array(instances, dtype='float16')


with open('models/num2vocab.json', 'w') as file:
    json.dump(num2vocab, file)      # For testing later.


def getOneHotLabels_RandChoicePerVideo(captions, num_classes):
    """choice one caption (list of ints) from caption candidates ramdomly for each video.

    Arguments:
        captions {list} -- contains captions (list) of videos.
        num_classes {int} -- vocabulary size.

    Returns:
        numpy.darray -- one-hot vectors. shape = (#sample, #max_timestep, #feature)
    """
    labels = []
    for videoCaps in captions:
        idx     = numpy.random.randint(len(videoCaps))
        caption = videoCaps[idx]
        # EOS Padding instead of Zero Padding.
        Caption = caption + [0] * (maxText - len(caption))
        labels  += [ np_utils.to_categorical(Caption, num_classes=num_classes) ]
    return numpy.array(labels)
