"""
example = speakId_sentenceId = (instance, label) -> frame.

train.ark:
#line       = 1124823
#Speaker    = 462
#Sentence   = 8
#example    = 3696 = 462 * 8
max(#frame) = 777
"""


# For workstation.
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'


import numpy
import sys
import re
from keras.utils import np_utils


try:
    dataPath = sys.argv[1]
except:
    dataPath = 'data/'


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
with open(dataPath + '/mfcc/train.ark') as file:
    for line in file:
        line  = line.split()
        strId = re.findall(r'^.+(?=_\d+)', line[0])[0]

        if strId not in dictId_Idx:
            dictId_Idx[strId] = cnt
            cnt += 1

        if None == strIdPrev:
            strIdPrev = strId
        elif strIdPrev != strId:        # New speakId_sentenceId.
            instances += [ numpy.array(frames, dtype='float16').reshape(1, -1, len(frames[0])) ]
            strIdPrev = strId
            frames    = []

        frames += [ line[1: ] ]

    # For the last speakId_sentenceId.
    instances += [ numpy.array(frames, dtype='float16').reshape(1, -1, len(frames[0])) ]
    frames    = None


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
            labels[iIdPrev] = numpy.array(frames).reshape(1, -1, 48)
            iIdPrev         = iId
            frames          = []

        frames += [ np_utils.to_categorical(dictPhone_CateIdx[ line[1] ], num_classes=48) ]

    # For the last speakId_sentenceId.
    labels[iId] = numpy.array(frames).reshape(1, -1, 48)
    frames      = None
