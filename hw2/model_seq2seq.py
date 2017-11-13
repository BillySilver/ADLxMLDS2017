from model_init import *
from keras.models import Model
from keras.layers import Input
from keras.layers.core import Dense, Activation
from keras.layers.convolutional import ZeroPadding1D, Cropping1D
from keras.layers.recurrent import LSTM
from keras.layers.wrappers import TimeDistributed
from keras.layers.merge import Concatenate, Add, Multiply


nVocabFeat = len(num2vocab)

try:
    from keras.models import load_model
    model = load_model('models/model.h5', custom_objects={
        'Layer_BOS_PrevLabels': Layer_BOS_PrevLabels,
        'RecurrentWrapper': RecurrentWrapper,
        'Layer_Slicer': Layer_Slicer,
        'my_categorical_crossentropy': my_categorical_crossentropy,
        'orgCE': orgCE,
        'myAcc': myAcc })
    print('\n* Has loaded existed model. *\n')
except:
    # Build model.

    # Encoder: receives (frames, features) of one video.
    Encoder_in  = Input(shape=(80, 4096), name='Encoder_in')
    x           = ZeroPadding1D(padding=(0, maxText))(Encoder_in)
    Encoder_out = LSTM(units=1024, implementation=2, return_sequences=True, name='Encoder_out')(x)

    # Decoder: receives (frames, features) of one video (from Encoder)
    #          and of the previous (1) ground truth, or (2) output of Decoder.
    Decoder_ext_in = Input(shape=(1024, ))
    Pred_in        = Input(shape=(nVocabFeat, ))
    Decoder_int_in = Concatenate(axis=-1)([Decoder_ext_in, Pred_in])

    def myLSTMCell(units, input):
        h_ = Input(shape=(units, ))
        c_ = Input(shape=(units, ))

        zf = Dense(units=units, kernel_initializer='glorot_uniform', bias_initializer='ones')(input)
        z_ = Dense(units=units*3, kernel_initializer='glorot_uniform', bias_initializer='zeros')(input)
        z0 = Concatenate(axis=-1)([zf, z_])
        z1 = Dense(units=units*4, kernel_initializer='orthogonal', use_bias=False)(h_)
        z  = Add()([z0, z1])

        z_f = Layer_Slicer(units=units, iPart=0)(z)
        z_i = Layer_Slicer(units=units, iPart=1)(z)
        z_o = Layer_Slicer(units=units, iPart=2)(z)
        z_c = Layer_Slicer(units=units, iPart=3)(z)

        f = Activation('hard_sigmoid')(z_f)
        i = Activation('hard_sigmoid')(z_i)
        o = Activation('hard_sigmoid')(z_o)
        c = Activation('tanh')(z_c)

        c0 = Multiply()([f, c_])
        c1 = Multiply()([i, c])
        c  = Add()([c0, c1])

        h = Activation('tanh')(c)
        h = Multiply()([o, h])

        return h_, c_, h, c

    h_, c_, h, c    = myLSTMCell(units=1024, input=Decoder_int_in)
    Decoder_ext_out = Dense(units=nVocabFeat, activation='softmax')(h)

    Decoder_in  = Encoder_out
    Decoder_out = RecurrentWrapper(
        input=[Decoder_ext_in],
        output=[Decoder_ext_out],
        bind={Pred_in: Decoder_ext_out,
              h_: h,
              c_: c},
        input_shape=(None, 1024),
        return_sequences=True,
        name='Decoder',
    )(Decoder_in)
    Decoder_out = Cropping1D(cropping=(80, 0))(Decoder_out)

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
