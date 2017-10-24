from model_init import *
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Masking
from keras.layers.recurrent import LSTM
from keras.layers.wrappers import TimeDistributed


try:
    from keras.models import load_model
    model = load_model('hw1.model_rnn.h5')
    print('Has loaded existed model.')
except:
    # Build model.
    input_dim = instances[0].shape[-1]      # dim(frame vector)

    model = Sequential()
    # model.add(Masking(0, input_shape=(777, input_dim))
    model.add(LSTM(units=50,
                   batch_input_shape=(1, None, input_dim),
                   return_sequences=True))
    model.add(TimeDistributed(Dense(units=48, activation='softmax')))
    model.compile(loss='categorical_crossentropy', optimizer='nadam')
    print('Create a new model.')


# Training.
randIdcs = list(range(len(instances)))
numpy.random.shuffle(randIdcs)
randIdcs, randIdcs_val = randIdcs[ : -len(randIdcs)//5], randIdcs[-len(randIdcs)//5 : ]
for epoch in range(0, 10):
    numpy.random.shuffle(randIdcs)

    mce = 0
    for i in range(len(randIdcs)):
        if 0 == (i+1) % 300:
            print('%d) %d / %d done.' % (epoch+1, i+1, len(randIdcs)))
        idx = randIdcs[i]
        mce += model.fit(instances[idx], labels[idx], epochs=1, verbose=0).history['loss'][0]
    print('%d) Training Cross Entropy: %f' % (epoch+1, mce / len(randIdcs)))

    mce = 0
    for idx in randIdcs_val:
        mce += model.evaluate(instances[idx], labels[idx], verbose=0)
    print('%d) Validate Cross Entropy: %f' % (epoch+1, mce / len(randIdcs_val)))

    model.save('hw1.model_rnn.h5')

# 01:53:00 - 03:37:17
# Training time is about 104 mins.
