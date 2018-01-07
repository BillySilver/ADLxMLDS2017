RESULTS
=======

Setting
-------

#### Common setting

* z ~ U(-1, 1) ^ 128
* 4800 dimensional condition vector to represent two attributes "hair" and "eyes".
    * the first 2400 dimensions are to describe "hair", and the rest is to "eyes".
    * null attribute is represent by a zero-vector.

#### Training ([train.py](../train.py))

* 14662 valid images
* batch size: 64
    * 230 updates per epoch
* 600 epochs
    * 138000 updates
* z for G and z for D are i.i.d. for each step

Check training history [iwgan7.valid_imgs_fixed_600.py](iwgan7.valid_imgs_fixed_600.py).

#### Testing ([generate.py](../generate.py))

* Noises for different conditions are i.i.d.
    * So the generated images may not be similar.

Demonstration
-------------

Check conditions [sample_testing_text.txt](../data/sample_testing_text.txt).

* **blue hair blue eyes**

![](sample_1_1.jpg?raw=true)
![](sample_1_2.jpg?raw=true)
![](sample_1_3.jpg?raw=true)
![](sample_1_4.jpg?raw=true)
![](sample_1_5.jpg?raw=true)

* **blue hair green eyes**

![](sample_2_1.jpg?raw=true)
![](sample_2_2.jpg?raw=true)
![](sample_2_3.jpg?raw=true)
![](sample_2_4.jpg?raw=true)
![](sample_2_5.jpg?raw=true)

* **blue hair red eyes**

![](sample_3_1.jpg?raw=true)
![](sample_3_2.jpg?raw=true)
![](sample_3_3.jpg?raw=true)
![](sample_3_4.jpg?raw=true)
![](sample_3_5.jpg?raw=true)

* **green hair blue eyes**

![](sample_4_1.jpg?raw=true)
![](sample_4_2.jpg?raw=true)
![](sample_4_3.jpg?raw=true)
![](sample_4_4.jpg?raw=true)
![](sample_4_5.jpg?raw=true)

* Special mission: **red hair green eyes**

![](sample_early_1.jpg?raw=true)
![](sample_early_2.jpg?raw=true)
![](sample_early_3.jpg?raw=true)
![](sample_early_4.jpg?raw=true)
![](sample_early_5.jpg?raw=true)
