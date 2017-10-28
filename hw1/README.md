HOMEWORK 1: Sequence Labeling on TIMIT
======================================

## Python Packages

Python version: **3.5.2**

- numpy (1.13.3)
- Keras (2.0.7)
- tensorflow (1.3.0)
- scikit-learn (0.19.0)
- h5py (2.7.1)

## Notices

hw1_rnn.py, hw1_cnn.py, hw1_best.py 在一開始都會先 import 同個目錄下的 hw1_init.py，載入所需資料及 PCA 的記錄。

模型位於 models/ 底下。


## File descriptions

- sample.csv - template to upload your answer
- 48_39.map - map 48 phone to 39 phone
- 48phone_char.map - map 48 phone to english character
- train.lab - label of training data
- fbank.zip - fbank features of training and testing data
- mfcc.zip - mfcc features of training and testing data
- wav.zip - original sound files
