____________________________________________________________________________________________________
Layer (type)                     Output Shape          Param #     Connected to                     
====================================================================================================
Encoder_in (InputLayer)          (None, 80, 4096)      0                                            
____________________________________________________________________________________________________
Labels_in (InputLayer)           (None, 41, 6132)      0                                            
____________________________________________________________________________________________________
zero_padding1d_1 (ZeroPadding1D) (None, 121, 4096)     0           Encoder_in[0][0]                 
____________________________________________________________________________________________________
bos_padding_1 (BOSPadding)       (None, 41, 6132)      0           Labels_in[0][0]                  
____________________________________________________________________________________________________
Encoder_out (LSTM)               (None, 121, 1024)     20975616    zero_padding1d_1[0][0]           
____________________________________________________________________________________________________
Labels_pad (ZeroPadding1D)       (None, 121, 6132)     0           bos_padding_1[0][0]              
____________________________________________________________________________________________________
Decoder (RecurrentWrapper)       (None, 121, 6132)     39794677.0  Encoder_out[0][0]                
                                                                   Labels_pad[0][0]                 
____________________________________________________________________________________________________
cropping1d_1 (Cropping1D)        (None, 41, 6132)      0           Decoder[0][0]                    
====================================================================================================
Total params: 60,770,293
Trainable params: 60,770,292
Non-trainable params: 1
____________________________________________________________________________________________________

* Create a new model. *

* Epoch 1/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 83s - loss: 5.9093 - orgCE: 1.2498 - myAcc: 0.1436 - acc: 0.4265 - val_loss: 5.2104 - val_orgCE: 1.0750 - val_myAcc: 0.2186 - val_acc: 0.8388
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 5.0918 - orgCE: 1.1063 - myAcc: 0.2307 - acc: 0.8329 - val_loss: 4.8389 - val_orgCE: 1.0132 - val_myAcc: 0.2642 - val_acc: 0.8459
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 4.7560 - orgCE: 1.0182 - myAcc: 0.2845 - acc: 0.8304 - val_loss: 4.6495 - val_orgCE: 0.9737 - val_myAcc: 0.3200 - val_acc: 0.8574
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 4.6376 - orgCE: 0.9886 - myAcc: 0.2972 - acc: 0.8399 - val_loss: 4.6342 - val_orgCE: 0.9758 - val_myAcc: 0.3200 - val_acc: 0.8384
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 4.6041 - orgCE: 0.9952 - myAcc: 0.2964 - acc: 0.8464 - val_loss: 4.6468 - val_orgCE: 1.0120 - val_myAcc: 0.3041 - val_acc: 0.8479
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 4.5326 - orgCE: 0.9965 - myAcc: 0.2893 - acc: 0.8432 - val_loss: 4.6346 - val_orgCE: 0.9888 - val_myAcc: 0.2976 - val_acc: 0.8500
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 4.4665 - orgCE: 0.9711 - myAcc: 0.2956 - acc: 0.8464 - val_loss: 4.5972 - val_orgCE: 0.9843 - val_myAcc: 0.3079 - val_acc: 0.8516
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 4.4242 - orgCE: 0.9455 - myAcc: 0.3007 - acc: 0.8501 - val_loss: 4.6930 - val_orgCE: 1.0385 - val_myAcc: 0.2945 - val_acc: 0.8437
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 4.3543 - orgCE: 0.9086 - myAcc: 0.3061 - acc: 0.8549 - val_loss: 4.5695 - val_orgCE: 0.9816 - val_myAcc: 0.3119 - val_acc: 0.8519
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 4.3821 - orgCE: 0.9304 - myAcc: 0.2992 - acc: 0.8507 - val_loss: 4.5530 - val_orgCE: 0.9469 - val_myAcc: 0.3009 - val_acc: 0.8544
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 4.2965 - orgCE: 0.9144 - myAcc: 0.3053 - acc: 0.8517 - val_loss: 4.5170 - val_orgCE: 0.9564 - val_myAcc: 0.3097 - val_acc: 0.8537
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 4.2925 - orgCE: 0.9148 - myAcc: 0.3050 - acc: 0.8510 - val_loss: 4.4657 - val_orgCE: 0.9330 - val_myAcc: 0.3008 - val_acc: 0.8537
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 4.2644 - orgCE: 0.9149 - myAcc: 0.3031 - acc: 0.8501 - val_loss: 4.4340 - val_orgCE: 0.9286 - val_myAcc: 0.3129 - val_acc: 0.8560
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 4.2300 - orgCE: 0.9058 - myAcc: 0.3020 - acc: 0.8496 - val_loss: 4.3344 - val_orgCE: 0.8750 - val_myAcc: 0.3210 - val_acc: 0.8627
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 4.1262 - orgCE: 0.8635 - myAcc: 0.3145 - acc: 0.8558 - val_loss: 4.5264 - val_orgCE: 0.9852 - val_myAcc: 0.3018 - val_acc: 0.8479
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 4.0988 - orgCE: 0.8753 - myAcc: 0.3139 - acc: 0.8513 - val_loss: 4.4107 - val_orgCE: 0.9506 - val_myAcc: 0.3152 - val_acc: 0.8501
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 4.0669 - orgCE: 0.8564 - myAcc: 0.3173 - acc: 0.8541 - val_loss: 4.3339 - val_orgCE: 0.9207 - val_myAcc: 0.3121 - val_acc: 0.8516
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 4.0284 - orgCE: 0.8502 - myAcc: 0.3237 - acc: 0.8547 - val_loss: 4.3703 - val_orgCE: 0.9239 - val_myAcc: 0.3149 - val_acc: 0.8547
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.9986 - orgCE: 0.8466 - myAcc: 0.3280 - acc: 0.8527 - val_loss: 4.4936 - val_orgCE: 0.9577 - val_myAcc: 0.2913 - val_acc: 0.8480
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.9907 - orgCE: 0.8490 - myAcc: 0.3341 - acc: 0.8546 - val_loss: 4.4575 - val_orgCE: 0.9394 - val_myAcc: 0.2965 - val_acc: 0.8489
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.9070 - orgCE: 0.8280 - myAcc: 0.3361 - acc: 0.8564 - val_loss: 4.3656 - val_orgCE: 0.9072 - val_myAcc: 0.3094 - val_acc: 0.8503
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.8984 - orgCE: 0.8351 - myAcc: 0.3349 - acc: 0.8518 - val_loss: 4.5342 - val_orgCE: 0.9962 - val_myAcc: 0.2905 - val_acc: 0.8368
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.8176 - orgCE: 0.8008 - myAcc: 0.3459 - acc: 0.8569 - val_loss: 4.5153 - val_orgCE: 0.9680 - val_myAcc: 0.2874 - val_acc: 0.8435
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.8667 - orgCE: 0.8174 - myAcc: 0.3472 - acc: 0.8529 - val_loss: 4.3408 - val_orgCE: 0.9404 - val_myAcc: 0.3153 - val_acc: 0.8494
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.8553 - orgCE: 0.8289 - myAcc: 0.3459 - acc: 0.8512 - val_loss: 4.3448 - val_orgCE: 0.9439 - val_myAcc: 0.3121 - val_acc: 0.8370
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.8317 - orgCE: 0.8396 - myAcc: 0.3462 - acc: 0.8494 - val_loss: 4.4009 - val_orgCE: 0.9568 - val_myAcc: 0.3122 - val_acc: 0.8476
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.7801 - orgCE: 0.8050 - myAcc: 0.3500 - acc: 0.8549 - val_loss: 4.4830 - val_orgCE: 0.9503 - val_myAcc: 0.3055 - val_acc: 0.8510
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.6991 - orgCE: 0.7876 - myAcc: 0.3586 - acc: 0.8572 - val_loss: 4.4280 - val_orgCE: 0.9376 - val_myAcc: 0.3044 - val_acc: 0.8469
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.7039 - orgCE: 0.7925 - myAcc: 0.3522 - acc: 0.8521 - val_loss: 4.5365 - val_orgCE: 1.0200 - val_myAcc: 0.2847 - val_acc: 0.8347
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.6642 - orgCE: 0.7779 - myAcc: 0.3604 - acc: 0.8574 - val_loss: 4.4465 - val_orgCE: 0.9548 - val_myAcc: 0.3002 - val_acc: 0.8456
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.6542 - orgCE: 0.7844 - myAcc: 0.3660 - acc: 0.8575 - val_loss: 4.4922 - val_orgCE: 0.9560 - val_myAcc: 0.2882 - val_acc: 0.8440
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.6075 - orgCE: 0.7782 - myAcc: 0.3738 - acc: 0.8577 - val_loss: 4.4853 - val_orgCE: 0.9699 - val_myAcc: 0.3008 - val_acc: 0.8403
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.5535 - orgCE: 0.7467 - myAcc: 0.3773 - acc: 0.8626 - val_loss: 4.4135 - val_orgCE: 0.9395 - val_myAcc: 0.2885 - val_acc: 0.8390
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.5613 - orgCE: 0.7537 - myAcc: 0.3738 - acc: 0.8612 - val_loss: 4.5377 - val_orgCE: 0.9867 - val_myAcc: 0.2937 - val_acc: 0.8395
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.5335 - orgCE: 0.7747 - myAcc: 0.3711 - acc: 0.8553 - val_loss: 4.4981 - val_orgCE: 0.9385 - val_myAcc: 0.2968 - val_acc: 0.8448
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.5117 - orgCE: 0.7528 - myAcc: 0.3746 - acc: 0.8592 - val_loss: 4.5117 - val_orgCE: 0.9697 - val_myAcc: 0.2968 - val_acc: 0.8424
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.4386 - orgCE: 0.7341 - myAcc: 0.3832 - acc: 0.8602 - val_loss: 4.4683 - val_orgCE: 0.9545 - val_myAcc: 0.3109 - val_acc: 0.8504
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.4304 - orgCE: 0.7396 - myAcc: 0.3860 - acc: 0.8598 - val_loss: 4.5630 - val_orgCE: 0.9541 - val_myAcc: 0.2860 - val_acc: 0.8387
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.3904 - orgCE: 0.7161 - myAcc: 0.3848 - acc: 0.8602 - val_loss: 4.4006 - val_orgCE: 0.9310 - val_myAcc: 0.3009 - val_acc: 0.8452
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.4284 - orgCE: 0.7428 - myAcc: 0.3805 - acc: 0.8536 - val_loss: 4.2854 - val_orgCE: 0.9112 - val_myAcc: 0.3197 - val_acc: 0.8520
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.3585 - orgCE: 0.7093 - myAcc: 0.3923 - acc: 0.8643 - val_loss: 4.5015 - val_orgCE: 0.9357 - val_myAcc: 0.2813 - val_acc: 0.8426
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.3026 - orgCE: 0.6944 - myAcc: 0.3995 - acc: 0.8653 - val_loss: 4.5378 - val_orgCE: 0.9711 - val_myAcc: 0.3009 - val_acc: 0.8449
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.3228 - orgCE: 0.7029 - myAcc: 0.3995 - acc: 0.8627 - val_loss: 4.5294 - val_orgCE: 0.9963 - val_myAcc: 0.2900 - val_acc: 0.8373
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.2690 - orgCE: 0.6822 - myAcc: 0.3959 - acc: 0.8658 - val_loss: 4.5751 - val_orgCE: 0.9555 - val_myAcc: 0.2942 - val_acc: 0.8447
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.2820 - orgCE: 0.6989 - myAcc: 0.3999 - acc: 0.8640 - val_loss: 4.5358 - val_orgCE: 0.9333 - val_myAcc: 0.2991 - val_acc: 0.8511
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.2340 - orgCE: 0.6820 - myAcc: 0.4088 - acc: 0.8656 - val_loss: 4.7082 - val_orgCE: 1.0162 - val_myAcc: 0.2840 - val_acc: 0.8405
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.2300 - orgCE: 0.6878 - myAcc: 0.4053 - acc: 0.8664 - val_loss: 4.5748 - val_orgCE: 0.9621 - val_myAcc: 0.2861 - val_acc: 0.8425
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.2372 - orgCE: 0.6959 - myAcc: 0.4028 - acc: 0.8624 - val_loss: 4.7054 - val_orgCE: 1.0323 - val_myAcc: 0.2765 - val_acc: 0.8350
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.1703 - orgCE: 0.6814 - myAcc: 0.4082 - acc: 0.8624 - val_loss: 4.4995 - val_orgCE: 0.9469 - val_myAcc: 0.2939 - val_acc: 0.8435
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.1530 - orgCE: 0.6700 - myAcc: 0.4115 - acc: 0.8672 - val_loss: 4.6694 - val_orgCE: 1.0195 - val_myAcc: 0.2716 - val_acc: 0.8340
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.1853 - orgCE: 0.6733 - myAcc: 0.4072 - acc: 0.8669 - val_loss: 4.6188 - val_orgCE: 0.9908 - val_myAcc: 0.2911 - val_acc: 0.8399
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.1118 - orgCE: 0.6525 - myAcc: 0.4173 - acc: 0.8713 - val_loss: 4.6078 - val_orgCE: 0.9540 - val_myAcc: 0.2852 - val_acc: 0.8312
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.1349 - orgCE: 0.6658 - myAcc: 0.4189 - acc: 0.8638 - val_loss: 4.5274 - val_orgCE: 0.9550 - val_myAcc: 0.3021 - val_acc: 0.8468
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.0922 - orgCE: 0.6559 - myAcc: 0.4184 - acc: 0.8680 - val_loss: 4.7238 - val_orgCE: 1.0482 - val_myAcc: 0.2782 - val_acc: 0.8355
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.1136 - orgCE: 0.6780 - myAcc: 0.4147 - acc: 0.8648 - val_loss: 4.5117 - val_orgCE: 0.9759 - val_myAcc: 0.3002 - val_acc: 0.8445
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.0436 - orgCE: 0.6468 - myAcc: 0.4221 - acc: 0.8690 - val_loss: 4.6935 - val_orgCE: 1.0242 - val_myAcc: 0.2822 - val_acc: 0.8350
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.0687 - orgCE: 0.6470 - myAcc: 0.4254 - acc: 0.8693 - val_loss: 4.6394 - val_orgCE: 1.0129 - val_myAcc: 0.2940 - val_acc: 0.8400
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.0016 - orgCE: 0.6345 - myAcc: 0.4306 - acc: 0.8703 - val_loss: 4.7408 - val_orgCE: 1.0253 - val_myAcc: 0.2886 - val_acc: 0.8235
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 3.0027 - orgCE: 0.6371 - myAcc: 0.4247 - acc: 0.8629 - val_loss: 4.5745 - val_orgCE: 0.9824 - val_myAcc: 0.3073 - val_acc: 0.8465
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.9843 - orgCE: 0.6369 - myAcc: 0.4306 - acc: 0.8623 - val_loss: 4.6999 - val_orgCE: 0.9782 - val_myAcc: 0.2811 - val_acc: 0.8446
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 3.0021 - orgCE: 0.6437 - myAcc: 0.4250 - acc: 0.8637 - val_loss: 4.5524 - val_orgCE: 0.9951 - val_myAcc: 0.2974 - val_acc: 0.8405
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.9827 - orgCE: 0.6383 - myAcc: 0.4334 - acc: 0.8658 - val_loss: 4.6550 - val_orgCE: 1.0021 - val_myAcc: 0.2873 - val_acc: 0.8388
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.9262 - orgCE: 0.6204 - myAcc: 0.4394 - acc: 0.8725 - val_loss: 4.5888 - val_orgCE: 1.0029 - val_myAcc: 0.2881 - val_acc: 0.8353
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.9613 - orgCE: 0.6341 - myAcc: 0.4349 - acc: 0.8675 - val_loss: 4.7878 - val_orgCE: 1.0238 - val_myAcc: 0.2757 - val_acc: 0.8313
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.8840 - orgCE: 0.6089 - myAcc: 0.4415 - acc: 0.8718 - val_loss: 4.6816 - val_orgCE: 0.9711 - val_myAcc: 0.2913 - val_acc: 0.8402
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.8414 - orgCE: 0.5990 - myAcc: 0.4477 - acc: 0.8720 - val_loss: 4.8041 - val_orgCE: 0.9902 - val_myAcc: 0.2747 - val_acc: 0.8311
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.8916 - orgCE: 0.6138 - myAcc: 0.4325 - acc: 0.8688 - val_loss: 4.7568 - val_orgCE: 1.0161 - val_myAcc: 0.2746 - val_acc: 0.8219
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.8371 - orgCE: 0.6077 - myAcc: 0.4399 - acc: 0.8620 - val_loss: 4.7331 - val_orgCE: 1.0262 - val_myAcc: 0.2853 - val_acc: 0.8386
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.7661 - orgCE: 0.5818 - myAcc: 0.4536 - acc: 0.8425 - val_loss: 4.7613 - val_orgCE: 0.9855 - val_myAcc: 0.2901 - val_acc: 0.8378
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.7971 - orgCE: 0.5832 - myAcc: 0.4465 - acc: 0.8721 - val_loss: 4.9417 - val_orgCE: 1.0878 - val_myAcc: 0.2672 - val_acc: 0.8233
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.8629 - orgCE: 0.6121 - myAcc: 0.4422 - acc: 0.8626 - val_loss: 4.6622 - val_orgCE: 0.9792 - val_myAcc: 0.2877 - val_acc: 0.8407
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.8314 - orgCE: 0.6052 - myAcc: 0.4455 - acc: 0.8646 - val_loss: 4.6091 - val_orgCE: 0.9545 - val_myAcc: 0.2930 - val_acc: 0.8082
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.8157 - orgCE: 0.5963 - myAcc: 0.4437 - acc: 0.8562 - val_loss: 4.7703 - val_orgCE: 0.9977 - val_myAcc: 0.2959 - val_acc: 0.8466
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.8082 - orgCE: 0.6147 - myAcc: 0.4464 - acc: 0.8518 - val_loss: 4.9006 - val_orgCE: 1.0948 - val_myAcc: 0.2690 - val_acc: 0.8252
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.7579 - orgCE: 0.5902 - myAcc: 0.4554 - acc: 0.8696 - val_loss: 4.6387 - val_orgCE: 1.0147 - val_myAcc: 0.3147 - val_acc: 0.8425
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.7689 - orgCE: 0.5940 - myAcc: 0.4514 - acc: 0.8736 - val_loss: 4.8260 - val_orgCE: 1.0443 - val_myAcc: 0.2899 - val_acc: 0.8336
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.6706 - orgCE: 0.5666 - myAcc: 0.4662 - acc: 0.8617 - val_loss: 4.9749 - val_orgCE: 1.0704 - val_myAcc: 0.2776 - val_acc: 0.8203
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.7664 - orgCE: 0.5973 - myAcc: 0.4496 - acc: 0.8448 - val_loss: 4.9787 - val_orgCE: 1.0580 - val_myAcc: 0.2717 - val_acc: 0.8374
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.7447 - orgCE: 0.5935 - myAcc: 0.4516 - acc: 0.8567 - val_loss: 4.6761 - val_orgCE: 0.9746 - val_myAcc: 0.2838 - val_acc: 0.8220
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.7487 - orgCE: 0.5867 - myAcc: 0.4565 - acc: 0.8702 - val_loss: 4.8731 - val_orgCE: 1.0441 - val_myAcc: 0.2888 - val_acc: 0.8411
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.7226 - orgCE: 0.5773 - myAcc: 0.4599 - acc: 0.8595 - val_loss: 4.8091 - val_orgCE: 1.0187 - val_myAcc: 0.2886 - val_acc: 0.8356
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.6394 - orgCE: 0.5556 - myAcc: 0.4626 - acc: 0.8701 - val_loss: 4.8539 - val_orgCE: 1.0724 - val_myAcc: 0.2785 - val_acc: 0.8300
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.6138 - orgCE: 0.5523 - myAcc: 0.4718 - acc: 0.8760 - val_loss: 4.7369 - val_orgCE: 0.9807 - val_myAcc: 0.2999 - val_acc: 0.8482
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.7020 - orgCE: 0.5786 - myAcc: 0.4581 - acc: 0.8726 - val_loss: 4.9434 - val_orgCE: 1.0849 - val_myAcc: 0.2658 - val_acc: 0.8283
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.6312 - orgCE: 0.5624 - myAcc: 0.4680 - acc: 0.8677 - val_loss: 5.0016 - val_orgCE: 1.1015 - val_myAcc: 0.2713 - val_acc: 0.8297
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.6129 - orgCE: 0.5506 - myAcc: 0.4734 - acc: 0.8736 - val_loss: 4.7336 - val_orgCE: 0.9889 - val_myAcc: 0.3045 - val_acc: 0.8454
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.6191 - orgCE: 0.5674 - myAcc: 0.4652 - acc: 0.8637 - val_loss: 4.8451 - val_orgCE: 1.0630 - val_myAcc: 0.2971 - val_acc: 0.8384
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.6005 - orgCE: 0.5553 - myAcc: 0.4749 - acc: 0.8540 - val_loss: 5.0317 - val_orgCE: 1.0434 - val_myAcc: 0.2712 - val_acc: 0.7872
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.6026 - orgCE: 0.5582 - myAcc: 0.4716 - acc: 0.8292 - val_loss: 4.7824 - val_orgCE: 1.0268 - val_myAcc: 0.2927 - val_acc: 0.8349
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.5613 - orgCE: 0.5397 - myAcc: 0.4773 - acc: 0.8714 - val_loss: 4.9524 - val_orgCE: 1.0686 - val_myAcc: 0.2653 - val_acc: 0.8071
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.5891 - orgCE: 0.5563 - myAcc: 0.4759 - acc: 0.8589 - val_loss: 5.0474 - val_orgCE: 1.1218 - val_myAcc: 0.2764 - val_acc: 0.8272
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.5919 - orgCE: 0.5586 - myAcc: 0.4763 - acc: 0.8640 - val_loss: 4.9630 - val_orgCE: 1.0342 - val_myAcc: 0.2887 - val_acc: 0.8411
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 2.5716 - orgCE: 0.5536 - myAcc: 0.4782 - acc: 0.7869 - val_loss: 5.1362 - val_orgCE: 1.1560 - val_myAcc: 0.2567 - val_acc: 0.8015
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.5198 - orgCE: 0.5296 - myAcc: 0.4863 - acc: 0.8757 - val_loss: 4.8435 - val_orgCE: 1.0554 - val_myAcc: 0.2911 - val_acc: 0.8412
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.5346 - orgCE: 0.5394 - myAcc: 0.4779 - acc: 0.8761 - val_loss: 4.8719 - val_orgCE: 1.0283 - val_myAcc: 0.2877 - val_acc: 0.8161
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.5282 - orgCE: 0.5400 - myAcc: 0.4826 - acc: 0.8656 - val_loss: 4.9479 - val_orgCE: 1.0639 - val_myAcc: 0.2806 - val_acc: 0.8277
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.5046 - orgCE: 0.5461 - myAcc: 0.4850 - acc: 0.8444 - val_loss: 4.9968 - val_orgCE: 1.0651 - val_myAcc: 0.2715 - val_acc: 0.8324
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.5204 - orgCE: 0.5408 - myAcc: 0.4821 - acc: 0.8720 - val_loss: 5.1242 - val_orgCE: 1.0752 - val_myAcc: 0.2752 - val_acc: 0.8219
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 80s - loss: 2.5023 - orgCE: 0.5408 - myAcc: 0.4853 - acc: 0.8666 - val_loss: 4.8726 - val_orgCE: 1.0456 - val_myAcc: 0.2868 - val_acc: 0.8407
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 86s - loss: 2.4413 - orgCE: 0.5197 - myAcc: 0.4878 - acc: 0.8735 - val_loss: 4.9874 - val_orgCE: 1.0437 - val_myAcc: 0.2832 - val_acc: 0.8411


# python3 bleu_eval.py sample_output_testset.txt
Originally, average bleu score is 0.2798755598711742
By another method, average bleu score is 0.6331066698141715
