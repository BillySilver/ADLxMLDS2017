HOMEWORK 4: Generative Adversarial Networks
======================================

## Python Packages

Python version: **3.5.2**

- numpy (1.13.3)
- Keras (2.0.7)
- tensorflow (1.3.0)
- h5py (2.7.1)
- scipy (0.19.1)
- scikit-image (0.13.1)

## Notices

make_hair_eyes_vec.py 是用來產生髮色及瞳色條件轉換成 2400 維向量的對應表的程式。輸出位於 models/hair_eyes_vec.npy, models/hair_eyes_vec.txt。這個轉換會借助 [skip_thoughts](https://github.com/tensorflow/models/tree/master/research/skip_thoughts)。生成對應表之後，便不需要再度使用 make_hair_eyes_vec.py。

generate.py 一開始會先 import 同個目錄下的 common_init.py 及 model_setup.py，並載入位於 models/ 底下的條件轉換向量表 hair_eyes_vec.npy。

模型位於 models/ 底下。執行 run.sh 時若未發現 models/Generator.h5，則會自動下載。
