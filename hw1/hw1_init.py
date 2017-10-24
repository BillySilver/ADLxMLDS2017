"""
example = speakId_sentenceId = (instance, label) -> frame.

test.ark:
#line       = 180406
#Speaker    = 74
#Sentence   = 8
#example    = 592 = 74 * 8
max(#frame) = 742
"""


import numpy
import sys
import re
from keras.utils import np_utils


try:
    dataPath = sys.argv[1]
except:
    dataPath = 'data/'

try:
    outputFileName = sys.argv[2]
except:
    outputFileName = 'result.csv'


# Create a map from 48 Phones to 39 Phones.
dictPhone48_39 = {}
with open(dataPath + '/phones/48_39.map') as file:
    for line in file:
        line = line.split()
        dictPhone48_39[line[0]] = line[1]

# Create a map from Categorical Indices to Characters (39).
dictPhone_CateIdx = {}
dictCateIdx_Phone = {}
with open(dataPath + '/48phone_char.map') as file:
    for line in file:
        line = line.split()
        dictPhone_CateIdx[line[0]] = int(line[1])
        dictCateIdx_Phone[int(line[1])] = line[0]

listCateIdx_Char39 = [None]*len(dictCateIdx_Phone)
for i in range(len(dictCateIdx_Phone)):
    phone   = dictCateIdx_Phone[i]
    iMapped = dictPhone_CateIdx[ dictPhone48_39[ phone ] ]
    listCateIdx_Char39[i] = chr(iMapped + (ord('a') if iMapped < 26 else ord('A')-26))
    if 'sil' == phone:
        charSil = listCateIdx_Char39[i]


# Read test instances.
dictId = {}

strIdPrev = None
strIds    = []
frames    = []
instances = []
with open(dataPath + '/mfcc/test.ark') as file:
    for line in file:
        line  = line.split()
        strId = re.findall(r'^.+(?=_\d+)', line[0])[0]

        if strId not in dictId:
            dictId[strId] = True
            strIds += [ strId ]

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
