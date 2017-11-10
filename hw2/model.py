from model_init import *
from keras.models import Model
from keras.layers import Input
from keras.layers.core import Dense
from keras.layers.convolutional import ZeroPadding1D, Cropping1D
from keras.layers.recurrent import LSTM
from keras.layers.wrappers import TimeDistributed


nVocabFeat = len(num2vocab)

try:
    from keras.models import load_model
    model = load_model('models/model.h5', custom_objects={'my_categorical_crossentropy': my_categorical_crossentropy, 'orgCE': orgCE, 'myAcc': myAcc})
    print('\n* Has loaded existed model. *\n')
except:
    # Build model.

    # Encoder: receives (frames, features) of one video.
    Encoder_in  = Input(shape=(80, 4096), name='Encoder_in')
    x           = ZeroPadding1D(padding=(0, maxText))(Encoder_in)
    Encoder_out = LSTM(units=1024, implementation=2, return_sequences=True, name='Encoder_out')(x)

    # Decoder: receives (frames, features) of one video (from Encoder)
    #          and of the previous (1) ground truth, or (2) output of Decoder.
    x           = LSTM(units=1024, implementation=2, return_sequences=True)(Encoder_out)
    x           = Cropping1D(cropping=(80, 0))(x)
    Decoder_out = TimeDistributed(Dense(units=nVocabFeat, activation='softmax', name='Decoder_out'))(x)

    model = Model(inputs=Encoder_in, outputs=Decoder_out)

    from keras.optimizers import Adam
    myAdam = Adam(decay=0.001)
    model.compile(loss=my_categorical_crossentropy, optimizer=myAdam, metrics=[orgCE, myAcc, 'acc'])
    model.summary()
    print('\n* Create a new model. *\n')


# Training.
epochs = 100
for t in range(epochs):
    labels = getOneHotLabels_RandChoicePerVideo(captions, num_classes=nVocabFeat)
    print('* Epoch %d/%d *' % (t+1, epochs))
    model.fit(instances, labels, epochs=1, batch_size=64, validation_split=0.2)
model.save('models/model.h5')
