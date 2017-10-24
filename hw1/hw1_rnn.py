from hw1_init import *
from keras.models import load_model


model = load_model('hw1.model_rnn.h5')

from itertools import groupby
from operator import itemgetter

with open(outputFileName, 'w') as File:
    File.write('id,phone_sequence\n')
    for i in range(len(instances)):
        Y = model.predict(instances[i])     # Return a 3D tensor.
        Y = numpy.argmax(Y[0], -1)
        strSentence = [ listCateIdx_Char39[y] for y in Y ]
        strSentence = list(map(itemgetter(0), groupby(strSentence)))    # Remove consecutive duplicates
        strSentence = ''.join(strSentence).strip(charSil)
        File.write(strIds[i] + ',' + strSentence + '\n')
