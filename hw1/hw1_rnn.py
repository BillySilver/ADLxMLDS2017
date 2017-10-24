from hw1_init import *
from keras.models import load_model


model = load_model('models/model_rnn.h5')
Y     = model.predict(instances)                # Return a 3D tensor.

from itertools import groupby
from operator import itemgetter

with open(outputFileName, 'w') as File:
    File.write('id,phone_sequence\n')
    for i in range(len(Y)):
        nValidFrame = dictId_Cnt[ strIds[i] ]
        frames      = Y[i][-nValidFrame : ]     # Remove prefix dummy timestep outputs.
        frames      = numpy.argmax(frames, -1)
        strSentence = [ listCateIdx_Char39[CateIdx] for CateIdx in frames ]
        strSentence = list(map(itemgetter(0), groupby(strSentence)))    # Remove consecutive duplicates
        strSentence = ''.join(strSentence).strip(charSil)
        File.write(strIds[i] + ',' + strSentence + '\n')
