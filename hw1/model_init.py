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
            instances += [ numpy.concatenate(
                ( numpy.zeros( (maxTimesteps-len(frames), len(frames[0])) ),    # Dummy inputs.
                  numpy.array(frames, dtype='float16') ),
                0                       # Along axis=0, i.e., num_sample dimension.
            ) ]
            strIdPrev = strId
            frames    = []

        frames += [ line[1: ] ]

    # For the last speakId_sentenceId.
    instances += [ numpy.concatenate(
        ( numpy.zeros( (maxTimesteps-len(frames), len(frames[0])) ),            # Dummy inputs.
          numpy.array(frames, dtype='float16') ),
        0                               # Along axis=0, i.e., num_sample dimension.
    ) ]
    frames    = None

instances = numpy.array(instances)


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
