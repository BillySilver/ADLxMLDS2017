import numpy as np
from keras.models import Sequential, load_model


# Load dataset from files.
X_test = np.fromfile('data/t10k-images-idx3-ubyte', dtype='uint8')[16:]     # Ignore the first 16 bytes.
X_test = X_test.reshape(-1, 1, 28, 28) / 255.                               # Normalization.


model = load_model('models/model.h5')

# Test.
y_test = model.predict(X_test, batch_size=32)
y_test = np.argmax(y_test, -1)
np.savetxt('result.csv',
           np.stack( (np.arange(0, y_test.size), y_test), axis=-1 ),
           '%d,%d',
           header='id,label',
           comments='')     # To let the header be not a comment.
