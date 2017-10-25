"""
example = speakId_sentenceId = (instance, label) -> frame.

train.ark:
#line       = 1124823
#Speaker    = 462
#Sentence   = 8
#example    = 3696 = 462 * 8
max(#frame) = 777
"""


import numpy
import sys
import re
from keras.utils import np_utils
from sklearn.decomposition import PCA
from sklearn.externals import joblib


try:
    dataPath = sys.argv[1]
except:
    dataPath = 'data/'

maxTimesteps = 777


# Create a map from Phones to Categorical Indices.
dictPhone_CateIdx = {}
with open(dataPath + '/48phone_char.map') as file:
    for line in file:
        line = line.split()
        dictPhone_CateIdx[line[0]] = int(line[1])


# Read training instances.
dictId_Idx = {}

cnt       = 0
strIdPrev = None
frames    = []
instances = []
nFrames   = []
with open(dataPath + '/fbank/train.ark') as file:
    for line in file:
        line  = line.split()
        strId = re.findall(r'^.+(?=_\d+)', line[0])[0]

        if strId not in dictId_Idx:
            dictId_Idx[strId] = cnt
            cnt += 1

        if None == strIdPrev:
            strIdPrev = strId
        elif strIdPrev != strId:        # New speakId_sentenceId.
            instances += [ numpy.array(frames) ]
            nFrames   += [ len(frames) ]
            strIdPrev = strId
            frames    = []

        frames += [ [ float(ft) for ft in line[1: ] ] ]

    # For the last speakId_sentenceId.
    instances += [ numpy.array(frames) ]
    nFrames   += [ len(frames) ]
    frames    = None

"""ZCA Whitening.

Let X = instances (centered), where its shape is (m = #sample, n = #feature).
Then X = U S V* (singular-value decomposition).
Note that V* = PCA().components_ is an n-by-n unitary
and each 'row' of it is a (right) singular vector of X.

Steps:
1) X_PCA  = X [dot] V.
2) X_PCAW = sqrt(m) X_PCA [dot] S^-1.
3) X_ZCAW = X_PCAW [dot] V*.

(1) lets X transform into anohter coordinate system which has the orthonormal basis V.
(2) makes sure that the variances of features = 1 (whitening).
(3) rotates dataset to the original coordinate system.

(1) and (2) are done by PCA(whiten=True).fit_transform().
"""
instances  = numpy.concatenate(instances)               # Design matrix. #row = #example; #column = #feature.
PCA_Whiten = PCA(whiten=True)
instances  = PCA_Whiten.fit_transform(instances)
instances  = instances.dot(PCA_Whiten.components_)      # 3) X_ZCAW = X_PCAW [dot] V*.
joblib.dump(PCA_Whiten, 'models/PCA_rnn.pkl')           # For testing later.

_instances = []
for i in range(len(nFrames)):
    nFrame = nFrames[i]
    _instances += [ numpy.concatenate(
        ( numpy.zeros( (maxTimesteps-nFrame, instances.shape[-1]) ),            # Dummy inputs.
          instances[ :nFrame] ),
        0                       # Along axis=0, i.e., num_sample dimension.
    ) ]
    instances = instances[nFrame: ]
instances  = _instances
_instances = None
instances  = numpy.array(instances, dtype='float16')


# Read training labels.
iIdPrev = None
frames  = []
labels  = [None]*len(instances)
with open(dataPath + '/label/train.lab') as file:
    for line in file:
        line = line.strip().split(',')
        strId = re.findall(r'^.+(?=_\d+)', line[0])[0]
        iId   = dictId_Idx[strId]

        if None == iIdPrev:
            iIdPrev = iId
        elif iIdPrev != iId:            # New speakId_sentenceId.
            labels[iIdPrev] = numpy.concatenate(
                ( numpy.zeros( (maxTimesteps-len(frames), 48) ),                # Dummy inputs.
                  np_utils.to_categorical(frames, num_classes=48) ),
                0                       # Along axis=0, i.e., num_sample dimension.
            )
            iIdPrev         = iId
            frames          = []

        frames += [ dictPhone_CateIdx[ line[1] ] ]

    # For the last speakId_sentenceId.
    labels[iIdPrev] = numpy.concatenate(
        ( numpy.zeros( (maxTimesteps-len(frames), 48) ),                        # Dummy inputs.
          np_utils.to_categorical(frames, num_classes=48) ),
        0                               # Along axis=0, i.e., num_sample dimension.
    )
    frames      = None

labels = numpy.array(labels)
