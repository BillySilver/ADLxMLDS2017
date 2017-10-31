from model_init import *
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Masking
from keras.layers.recurrent import LSTM
from keras.layers.wrappers import TimeDistributed, Bidirectional


try:
    from keras.models import load_model
    model = load_model('models/model_rnn.h5')
    print('\n* Has loaded existed model. *\n')
except:
    # Build model.
    input_dim = instances[0].shape[-1]      # dim(frame vector)

    model = Sequential()
    model.add(Masking(mask_value=0, input_shape=(maxTimesteps, input_dim)))
    model.add(Bidirectional(LSTM(units=64,
                                 return_sequences=True),
                            merge_mode='concat'))
    model.add(TimeDistributed(Dropout(rate=0.5)))
    model.add(Bidirectional(LSTM(units=128,
                                 return_sequences=True),
                            merge_mode='concat'))
    model.add(TimeDistributed(Dropout(rate=0.5)))
    model.add(Bidirectional(LSTM(units=128,
                                 return_sequences=True),
                            merge_mode='concat'))
    model.add(TimeDistributed(Dropout(rate=0.5)))
    model.add(TimeDistributed(Dense(units=48, activation='softmax')))
    model.compile(loss='categorical_crossentropy', optimizer='nadam', metrics=['accuracy'])
    print('\n* Create a new model. *\n')


# Training.
model.fit(instances, labels, epochs=16, batch_size=64, validation_split=0)
model.save('models/model_rnn.h5')
