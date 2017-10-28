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
from sklearn.decomposition import PCA
from sklearn.externals import joblib


try:
    dataPath = sys.argv[1]
except:
    dataPath = 'data/'

try:
    outputFileName = sys.argv[2]
except:
    outputFileName = 'result.csv'

maxTimesteps = 777


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
dictId_Cnt = {}

strIdPrev = None
strIds    = []
frames    = []
instances = []
with open(dataPath + '/mfcc/test.ark') as file:
    PCA_Whiten = joblib.load('models/PCA.pkl')

    for line in file:
        line  = line.split()
        strId = re.findall(r'^.+(?=_\d+)', line[0])[0]

        if strId not in dictId_Cnt:
            dictId_Cnt[strId] = 0
            strIds += [ strId ]
        dictId_Cnt[strId] += 1

        if None == strIdPrev:
            strIdPrev = strId
        elif strIdPrev != strId:        # New speakId_sentenceId.
            instances += [ numpy.concatenate(
                ( numpy.zeros( (maxTimesteps-len(frames), len(frames[0])) ),    # Dummy inputs.
                  PCA_Whiten.transform(numpy.array(frames)).dot(PCA_Whiten.components_) ),
                0                       # Along axis=0, i.e., num_sample dimension.
            ) ]
            strIdPrev = strId
            frames    = []

        frames += [ [ float(ft) for ft in line[1: ] ] ]

    # For the last speakId_sentenceId.
    instances += [ numpy.concatenate(
        ( numpy.zeros( (maxTimesteps-len(frames), len(frames[0])) ),            # Dummy inputs.
          PCA_Whiten.transform(numpy.array(frames)).dot(PCA_Whiten.components_) ),
        0                               # Along axis=0, i.e., num_sample dimension.
    ) ]
    frames    = None

instances = numpy.array(instances, dtype='float16')
