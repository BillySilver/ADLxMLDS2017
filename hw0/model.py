import numpy as np
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Flatten, Dropout
from keras.layers.convolutional import Conv2D, MaxPooling2D


# Load dataset from files.
X_train = np.fromfile('data/train-images-idx3-ubyte', dtype='uint8')[16:]   # Ignore the first 16 bytes.
X_train = X_train.reshape(-1, 1, 28, 28) / 255.                             # Normalization.

y_train = np.fromfile('data/train-labels-idx1-ubyte', dtype='uint8')[8:]    # Ignore the first 8 bytes.
y_train = np_utils.to_categorical(y_train, num_classes=10)


try:
    from keras.models import load_model
    model = load_model('models/model.h5')
    print('\n* Has loaded existed model. *\n')
except:
    # Building a Convolutional Neural Network.
    model = Sequential()
    model.add(Conv2D(filters=32,
                     kernel_size=(3, 3),
                     data_format='channels_first',
                     input_shape=(1, 28, 28),
                     activation='relu'))
    model.add(Conv2D(filters=32,
                     kernel_size=(3, 3),
                     activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(rate=0.25))

    model.add(Conv2D(filters=64,
                     kernel_size=(3, 3),
                     activation='relu'))
    model.add(Conv2D(filters=64,
                     kernel_size=(3, 3),
                     activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(rate=0.25))

    model.add(Flatten())
    model.add(Dense(units=256, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=10, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='nadam', metrics=['accuracy'])
    print('\n* Create a new model. *\n')


# Training.
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
model.save('models/model.h5')
