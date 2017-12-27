RESULTS
=======

Setting
-------

#### Common setting

* z ~ U(-1, 1) ^ 128
* 2400 dimensional condition vector to summarize attributes.

#### Training ([train.py](../train.py))

* 15711 valid images
* 300+300 epochs
* z for G and z for D are i.i.d. for each step

Check training history [iwgan4.bugfix_identical_cond.py](iwgan4.bugfix_identical_cond.py).

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
