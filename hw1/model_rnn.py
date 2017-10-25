from model_init import *
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Masking
from keras.layers.recurrent import LSTM
from keras.layers.wrappers import TimeDistributed


try:
    from keras.models import load_model
    model = load_model('models/model_rnn.h5')
    print('\n* Has loaded existed model. *\n')
except:
    # Build model.
    input_dim = instances[0].shape[-1]      # dim(frame vector)

    model = Sequential()
    model.add(Masking(mask_value=0, input_shape=(maxTimesteps, input_dim)))
    model.add(LSTM(units=256,
                   return_sequences=True))
    model.add(TimeDistributed(Dropout(rate=0.5)))
    model.add(LSTM(units=256,
                   return_sequences=True))
    model.add(TimeDistributed(Dropout(rate=0.5)))
    model.add(TimeDistributed(Dense(units=48, activation='softmax')))
    model.compile(loss='categorical_crossentropy', optimizer='nadam', metrics=['accuracy'])
    print('\n* Create a new model. *\n')


# Training.
model.fit(instances, labels, epochs=100, batch_size=64, validation_split=0.2)
model.save('models/model_rnn.h5')
