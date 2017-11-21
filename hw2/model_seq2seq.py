from model_init import *
from keras.models import Model
from keras.layers import Input
from keras.layers.core import Dense, Activation, Lambda
from keras.layers.convolutional import ZeroPadding1D, Cropping1D
from keras.layers.recurrent import LSTM
from keras.layers.wrappers import TimeDistributed
from keras.layers.merge import Concatenate, Add, Multiply


nVocabFeat = len(num2vocab)

try:
    from keras.models import load_model
    model = load_model('models/model.h5', custom_objects={
        'BOSPadding': BOSPadding,
        'RecurrentWrapper': RecurrentWrapper,
        'Slicer': Slicer,
        'ArgmaxOneHot': ArgmaxOneHot,
        'ScheduleSampling': ScheduleSampling,
        'Attention': Attention,
        'my_categorical_crossentropy': my_categorical_crossentropy,
        'orgCE': orgCE,
        'myAcc': myAcc })
    print('\n* Has loaded existed model. *\n')
except:
    # Build model.

    # Encoder: receives (frames, features) of one video.
    Encoder_in  = Input(shape=(80, 4096), name='Encoder_in')
    Encoder_out = LSTM(units=1024, implementation=2, return_sequences=True, name='Encoder_out')(Encoder_in)

    # Decoder: receives (frames, features) of one video (from Encoder)
    #          and of the previous (1) ground truth, or (2) output of Decoder.
    Labels_in  = Input(shape=(maxText, nVocabFeat), name='Labels_in')
    Labels_pad = BOSPadding(idxBOS=vocab2num['^'])(Labels_in)

    Decoder_ext_in = Input(shape=(1024, ))
    Pred_in        = Input(shape=(nVocabFeat, ))
    Label_in       = Input(shape=(nVocabFeat, ))
    Pred_or_Label  = ScheduleSampling(decay_param=160)([Pred_in, Label_in])
    Decoder_int_in = Concatenate(axis=-1)([Decoder_ext_in, Pred_or_Label])

    def myLSTMCell(units, input):
        h_ = Input(shape=(units, ))
        c_ = Input(shape=(units, ))

        zf = Dense(units=units, kernel_initializer='glorot_uniform', bias_initializer='ones')(input)
        z_ = Dense(units=units*3, kernel_initializer='glorot_uniform', bias_initializer='zeros')(input)
        z0 = Concatenate(axis=-1)([zf, z_])
        z1 = Dense(units=units*4, kernel_initializer='orthogonal', use_bias=False)(h_)
        z  = Add()([z0, z1])

        z_f = Slicer(units=units, iPart=0)(z)
        z_i = Slicer(units=units, iPart=1)(z)
        z_o = Slicer(units=units, iPart=2)(z)
        z_c = Slicer(units=units, iPart=3)(z)

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
    Pred_OneHot     = ArgmaxOneHot()(Decoder_ext_out)

    # Attention-based layer.
    def AttetionWrapper(num_timesteps, num_features, state):
        SourceFrames = Input(shape=(num_timesteps, num_features))
        # 1) Calculate score for each timestep.
        ScoreFrames  = TimeDistributed(Dense(units=1, use_bias=False))(SourceFrames)
        ScoreState   = Dense(units=1)(state)
        AttenScores  = Add()([ScoreFrames, ScoreState])         # (samples, timesteps, 1)
        AttenScores  = Lambda(lambda x: K.squeeze(x, axis=-1),
                              output_shape=(num_timesteps, )    # (samples, timesteps)
                       )(AttenScores)
        # 2) Apply Softmax to obtain weights of vectors in sequence.
        # AttenWeights = Activation('tanh')(AttenScores)
        AttenWeights = Activation('softmax')(AttenScores)       # Along the last (i.e., timestep) axis.
        AttenWeights = Lambda(lambda x: K.expand_dims(x, axis=-1),
                              output_shape=(num_timesteps, 1)   # (samples, timesteps, 1)
                       )(AttenWeights)
        # 3) Get weighted sum.
        AttenContext = Multiply()([AttenWeights, SourceFrames]) # (samples, timesteps, features)
        AttenContext = Lambda(lambda x: K.sum(x, axis=1),
                              output_shape=(num_features, )     # (samples, features)
                       )(AttenContext)
        return SourceFrames, AttenContext

    # Using the hidden state of Decoder LSTM.
    Atten_seq_in, Atten_out = AttetionWrapper(num_timesteps=80, num_features=1024, state=h_)

    # [recurrent_inputs] + [sequence_inputs]
    Decoder_in  = [Labels_pad] + [Encoder_out]
    Decoder_out = RecurrentWrapper(
        input=[Label_in],
        output=[Decoder_ext_out],
        bind={Decoder_ext_in: Atten_out,
              Pred_in: Pred_OneHot,
              h_: h,
              c_: c},
        sequence_input=[Atten_seq_in],
        input_shape=(None, 1024),
        return_sequences=True,
        name='Decoder',
    )(Decoder_in)

    model = Model(inputs=[Encoder_in, Labels_in], outputs=Decoder_out)

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
    model.fit([instances, labels], labels, epochs=1, batch_size=64, validation_split=0.2)
model.save('models/model.h5')
