from model_init import *
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Masking, Reshape, Activation
from keras.layers.recurrent import LSTM
from keras.layers.convolutional import Conv2D, ZeroPadding2D
from keras.layers.wrappers import TimeDistributed, Bidirectional
from keras.layers.normalization import BatchNormalization


try:
    from keras.models import load_model
    model = load_model('models/model_cnn.h5')
    print('\n* Has loaded existed model. *\n')
except:
    # Build model.
    input_dim = instances[0].shape[-1]      # dim(frame vector)
    nPrevVec  = 2
    radius    = 3

    model = Sequential()

    model.add(Reshape(target_shape=(1, maxTimesteps, input_dim),
                      input_shape=(maxTimesteps, input_dim)))
    model.add(ZeroPadding2D(padding=((nPrevVec, 0), (radius, radius)),
                            data_format='channels_first'))
    model.add(Conv2D(filters=64,
                     kernel_size=(1+nPrevVec, 2*radius+1),
                     strides=(1, 1),
                     padding='valid',
                     data_format='channels_first',
                     activation='linear',
                     use_bias=False,
                     kernel_initializer='he_normal'))
    # model.add(BatchNormalization(axis=1, center=False, scale=False))
    # model.add(Activation('relu'))

    model.add(Conv2D(filters=1,
                     kernel_size=(1, 3),
                     strides=(1, 1),
                     padding='valid',
                     data_format='channels_first',
                     activation='linear',
                     use_bias=False,
                     kernel_initializer='he_normal'))
    # model.add(BatchNormalization(axis=1, center=False, scale=False))
    # model.add(Activation('relu'))

    model.add(Reshape(target_shape=(maxTimesteps, -1)))
    model.add(Masking(mask_value=0))
    model.add(Bidirectional(LSTM(units=128,
                                 return_sequences=True),
                            merge_mode='concat'))
    model.add(TimeDistributed(Dropout(rate=0.5)))
    model.add(Bidirectional(LSTM(units=256,
                                 return_sequences=True),
                            merge_mode='concat'))
    model.add(TimeDistributed(Dropout(rate=0.5)))
    model.add(TimeDistributed(Dense(units=48, activation='softmax')))
    model.compile(loss='categorical_crossentropy', optimizer='nadam', metrics=['accuracy'])
    print('\n* Create a new model. *\n')

# Training.
model.fit(instances, labels, epochs=20, batch_size=64, validation_split=0.2)
model.save('models/model_cnn.h5')
