# https://arxiv.org/pdf/1605.05396.pdf

from keras import backend as K
from keras.models import Model
from keras.layers import Input
from keras.layers.core import Dense, Dropout, Reshape, Activation, Flatten, RepeatVector, Lambda
from keras.layers.convolutional import Conv2D, Conv2DTranspose
from keras.layers.pooling import MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras.layers.advanced_activations import LeakyReLU
from keras.layers.merge import Concatenate, Average, Subtract
from keras.optimizers import Adam
import numpy as np


LReLU_alpha = 0.1
K.set_image_data_format('channels_last')
myOpt = Adam(lr=1e-4, beta_1=0.5, beta_2=0.9)


def _Descriptor(cond_dim=2400, name=None, useReLU=False):
    hidden_cond_dim = 2**int(np.log(cond_dim) / np.log(2))

    # Condition, a.k.a. Description.
    cond = Input(shape=(cond_dim, ), name=name)
    hidden_cond = cond
    while hidden_cond_dim > 128:
        hidden_cond_dim //= 4
        hidden_cond = Dense(units=hidden_cond_dim)(hidden_cond)
        if not useReLU:
            hidden_cond = LeakyReLU(alpha=LReLU_alpha)(hidden_cond)
        else:
            hidden_cond = Activation('relu')(hidden_cond)

    return cond, hidden_cond, hidden_cond_dim


def Generator(img_shape, cond_dim=2400, noise_dim=128):
    def Deconv2DBlock(x, filters, kernel_size, strides=(2, 2), padding='same', isLast=False):
        x = Conv2DTranspose(filters=filters, kernel_size=kernel_size,
                            strides=strides, padding=padding,
                            kernel_initializer='he_uniform')(x)
        if not isLast:
            x = BatchNormalization()(x)
            x = LeakyReLU(alpha=LReLU_alpha)(x)
        return x

    cond, out_cond, out_cond_dim = _Descriptor(cond_dim, name='CONDITION_for_G')
    noise = Input(shape=(noise_dim, ), name='NOISE_INPUT')

    """
    n_row = img_shape[0]
    n_col = img_shape[1]
    # (1, 1, 256) -> (4, 4, 1024) -> (8,8, 512)
    #  -> (16, 16, 256) -> (32, 32, 128) -> (64, 64, 64).
    def recur_build_deconv2d(first_x, n_row, n_col, first_channel, recur_depth=0):
        prev_row   = (n_row // 2) if (n_row >= 6) else n_row
        prev_col   = (n_col // 2) if (n_col >= 6) else n_col
        next_depth = recur_depth + int(prev_row != n_row and prev_col != n_col)

        # First deconv2d block. n_row and n_col are in {3, 4, 5}.
        if prev_row == n_row and prev_col == n_col:
            x = Deconv2DBlock(first_x, filters=1024, kernel_size=(n_row, n_row),
                              strides=(1, 1), padding='valid')
            return x

        x = recur_build_deconv2d(first_x, prev_row, prev_col, first_channel, recur_depth=recur_depth)
    """

    x = Concatenate(axis=-1, name='CONCAT_for_G')([noise, out_cond])
    x = Reshape(target_shape=(1, 1, -1))(x)

    # x = recur_build_deconv2d(x, n_row, n_col, noise_dim+out_cond_dim)
    x = Deconv2DBlock(x, filters=1024, kernel_size=(4, 4),
                      strides=(1, 1), padding='valid')

    x = Deconv2DBlock(x, filters=512, kernel_size=(5, 5),   # (8, 8, 512)
                      strides=(2, 2))
    x = Deconv2DBlock(x, filters=256, kernel_size=(5, 5),   # (16, 16, 256)
                      strides=(2, 2))
    x = Deconv2DBlock(x, filters=128, kernel_size=(5, 5),   # (32, 32, 128)
                      strides=(2, 2))
    x = Deconv2DBlock(x, filters=64, kernel_size=(5, 5),    # (64, 64, 64)
                      strides=(2, 2))

    x = Deconv2DBlock(x, filters=img_shape[-1], kernel_size=(5, 5), # (64, 64, 3)
                      strides=(1, 1), isLast=True)
    G = Activation('sigmoid', name='GENERATOR_OUTPUT')(x)

    model = Model(inputs=[noise, cond], outputs=G)
    return model


def Discriminator(img_shape, cond_dim=2400):
    cond, out_cond, out_cond_dim = _Descriptor(cond_dim, name='CONDITION_for_D', useReLU=True)
    n_row     = img_shape[0]
    n_col     = img_shape[1]
    n_channel = 64

    img = Input(shape=img_shape, name='IMAGE_INPUT')
    x   = img
    while True:
        step_row = 2 if (n_row >= 6) else 1
        step_col = 2 if (n_col >= 6) else 1
        if step_row * step_col == 1:
            # n_row and n_col are in {3, 4, 5}.
            break

        x = Conv2D(filters=n_channel, kernel_size=(5, 5),
                   strides=(step_row, step_col), padding='same',
                   kernel_initializer='he_uniform')(x)
        x = LeakyReLU(alpha=LReLU_alpha)(x)
        n_row //= step_row
        n_col //= step_col
        n_channel *= 2 if (step_row * step_col == 4) else 1

    extracted_img = Conv2D(filters=out_cond_dim, kernel_size=(1, 1),
                           kernel_initializer='he_uniform', name='EXTRACTED_IMAGE')(x)

    rep_cond = RepeatVector(n_row * n_col)(out_cond)
    rep_cond = Reshape(target_shape=(n_row, n_col, -1))(rep_cond)
    x        = Concatenate(axis=-1, name='CONCAT_for_D')([extracted_img, rep_cond])

    x = Conv2D(filters=2*out_cond_dim, kernel_size=(1, 1),
               activation='relu',
               kernel_initializer='he_uniform')(x)
    x = Flatten()(x)
    x = Dense(units=256, activation='relu')(x)
    D = Dense(units=1, name='DISCRIMINATOR_OUTPUT')(x)

    model = Model(inputs=[img, cond], outputs=D)
    return model


def GAN(G, D, cond_dim=2400, noise_dim=128):
    cond  = Input(shape=(cond_dim, ), name='CONDITION_for_GD')
    noise = Input(shape=(noise_dim, ), name='NOISE_for_GD')

    G_out = G([noise, cond])
    D_out = D([G_out, cond])

    model = Model(inputs=[noise, cond], outputs=D_out)
    model.compile(loss=loss_for_G, optimizer=myOpt)
    return model

def iW_D(D, img_shape, cond_dim=2400, lmbd=10.):
    real_img   = Input(shape=img_shape, name='REAL_IMG')
    fake_img   = Input(shape=img_shape, name='FAKE_IMG')
    right_cond = Input(shape=(cond_dim, ), name='RIGHT_COND')
    wrong_cond = Input(shape=(cond_dim, ), name='WRONG_COND')  # w.r.t. real_img.

    pos   = D([real_img, right_cond])
    neg1  = D([fake_img, right_cond])
    neg2  = D([real_img, wrong_cond])
    neg   = Average()([neg1, neg2])
    score = Subtract(name='Score_by_D')([pos, neg])

    fuzzy_img = Interpolation(name='FUZZY_IMG')([real_img, fake_img])
    penalty1  = D([fuzzy_img, right_cond])
    gradnorm1 = GradNorm()([penalty1, fuzzy_img, right_cond])

    fuzzy_cond = Interpolation(name='FUZZY_COND')([right_cond, wrong_cond])
    penalty2   = D([real_img, fuzzy_cond])
    gradnorm2  = GradNorm()([penalty2, real_img, fuzzy_cond])

    model = Model(inputs=[real_img, fake_img, right_cond, wrong_cond], outputs=[score, gradnorm1, gradnorm2])
    model.compile(loss=[loss_for_D, 'mse', 'mse'], optimizer=myOpt, loss_weights=[1.0, lmbd/2., lmbd/2.])
    return model

def loss_for_G(y_true, y_pred):
    # (fake_img, right_cond).
    return - K.mean(y_pred)

def loss_for_D(y_true, y_pred):
    # Primary calculation is in iW_D().
    # y_pred is score.
    return - K.mean(y_pred)

from keras.engine.topology import Layer
class GradNorm(Layer):
    # def __init__(self, **kwargs):
    #     super(GradNorm, self).__init__(**kwargs)

    # def build(self, input_shapes):
    #     super(GradNorm, self).build(input_shapes)

    def call(self, inputs):
        target = inputs[0]
        wrt    = inputs[1: ]
        grads  = K.gradients(target, wrt)
        # assert len(grads) == 1
        inner_prod = K.zeros_like(target)
        inner_prod = K.sum(K.batch_flatten(inner_prod), axis=1, keepdims=True)
        for grad in grads:
            inner_prod += K.sum(K.square(K.batch_flatten(grad)), axis=1, keepdims=True)
        return K.sqrt(inner_prod)

    def compute_output_shape(self, input_shapes):
        return (input_shapes[1][0], 1)

from keras.layers.merge import _Merge
class Interpolation(_Merge):
    def _merge_function(self, inputs):
        assert len(inputs) == 2

        shape      = inputs[0].shape.as_list()
        tfShape    = K.shape(inputs[0])
        proportion = K.random_uniform(tfShape[ :1], minval=0., maxval=1.)
        for _ in range(1, len(shape)):
            proportion = K.expand_dims(proportion, axis=-1)

        return proportion * inputs[0] + (1 - proportion) * inputs[1]
