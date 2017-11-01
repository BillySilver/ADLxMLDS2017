# For workstation.
import os
# Use GPU 0, 1.
os.environ['CUDA_VISIBLE_DEVICES'] = '1'
# Disable all debugging logs from TensorFlow.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# Limit GPU Memory usage.
import tensorflow as tf
from keras import backend as K
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)
K.set_session(sess)

from model import *
