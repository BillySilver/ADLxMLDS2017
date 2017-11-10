# For workstation.
import os
# Choose GPU.
os.environ['CUDA_VISIBLE_DEVICES'] = '1'
# Disable all debugging logs from TensorFlow.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# Limit GPU Memory usage.
from keras import backend as K
if 'tensorflow' == K.backend():
    config = K.tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = K.tf.Session(config=config)
    K.set_session(sess)

from model_cnn import *
