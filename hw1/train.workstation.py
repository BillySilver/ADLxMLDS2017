# For workstation.
import os
# Use GPU 0, 1.
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'
# Disable all debugging logs from TensorFlow.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from model_rnn import *
