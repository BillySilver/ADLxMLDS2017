____________________________________________________________________________________________________
Layer (type)                     Output Shape          Param #     Connected to                     
====================================================================================================
Encoder_in (InputLayer)          (None, 80, 4096)      0                                            
____________________________________________________________________________________________________
Labels_in (InputLayer)           (None, 41, 6132)      0                                            
____________________________________________________________________________________________________
zero_padding1d_1 (ZeroPadding1D) (None, 121, 4096)     0           Encoder_in[0][0]                 
____________________________________________________________________________________________________
layer_bos__prev_labels_1 (Layer_ (None, 41, 6132)      0           Labels_in[0][0]                  
____________________________________________________________________________________________________
Encoder_out (LSTM)               (None, 121, 1024)     20975616    zero_padding1d_1[0][0]           
____________________________________________________________________________________________________
Labels_pad (ZeroPadding1D)       (None, 121, 6132)     0           layer_bos__prev_labels_1[0][0]   
____________________________________________________________________________________________________
Decoder (RecurrentWrapper)       (None, 121, 6132)     39794676    Encoder_out[0][0]                
                                                                   Labels_pad[0][0]                 
____________________________________________________________________________________________________
cropping1d_1 (Cropping1D)        (None, 41, 6132)      0           Decoder[0][0]                    
====================================================================================================
Total params: 60,770,292
Trainable params: 60,770,292
Non-trainable params: 0
____________________________________________________________________________________________________

* Create a new model. *

* Epoch 1/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 79s - loss: 5.9321 - orgCE: 1.2691 - myAcc: 0.1537 - acc: 0.4299 - val_loss: 5.1753 - val_orgCE: 1.0600 - val_myAcc: 0.2639 - val_acc: 0.8492
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 5.0301 - orgCE: 1.0685 - myAcc: 0.2411 - acc: 0.8388 - val_loss: 5.0035 - val_orgCE: 1.0689 - val_myAcc: 0.2569 - val_acc: 0.8414
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.7822 - orgCE: 1.0202 - myAcc: 0.2843 - acc: 0.8471 - val_loss: 4.6879 - val_orgCE: 0.9896 - val_myAcc: 0.3072 - val_acc: 0.8536
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.6581 - orgCE: 0.9934 - myAcc: 0.2992 - acc: 0.8487 - val_loss: 4.6409 - val_orgCE: 0.9936 - val_myAcc: 0.3119 - val_acc: 0.8526
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.5522 - orgCE: 0.9639 - myAcc: 0.3025 - acc: 0.8520 - val_loss: 4.7481 - val_orgCE: 1.0355 - val_myAcc: 0.2959 - val_acc: 0.8463
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.5705 - orgCE: 0.9963 - myAcc: 0.3008 - acc: 0.8474 - val_loss: 4.6329 - val_orgCE: 1.0049 - val_myAcc: 0.3023 - val_acc: 0.8486
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.5280 - orgCE: 0.9618 - myAcc: 0.2937 - acc: 0.8493 - val_loss: 4.6267 - val_orgCE: 1.0074 - val_myAcc: 0.2986 - val_acc: 0.8470
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.4219 - orgCE: 0.9312 - myAcc: 0.3050 - acc: 0.8532 - val_loss: 4.6125 - val_orgCE: 0.9881 - val_myAcc: 0.3139 - val_acc: 0.8529
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.4504 - orgCE: 0.9458 - myAcc: 0.2997 - acc: 0.8508 - val_loss: 4.5099 - val_orgCE: 0.9760 - val_myAcc: 0.3262 - val_acc: 0.8540
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.3950 - orgCE: 0.9357 - myAcc: 0.2986 - acc: 0.8504 - val_loss: 4.4790 - val_orgCE: 0.9716 - val_myAcc: 0.3086 - val_acc: 0.8495
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.3947 - orgCE: 0.9311 - myAcc: 0.3000 - acc: 0.8513 - val_loss: 4.4211 - val_orgCE: 0.9310 - val_myAcc: 0.3139 - val_acc: 0.8555
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.3872 - orgCE: 0.9264 - myAcc: 0.2944 - acc: 0.8505 - val_loss: 4.6045 - val_orgCE: 1.0075 - val_myAcc: 0.2929 - val_acc: 0.8450
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.2564 - orgCE: 0.8943 - myAcc: 0.3079 - acc: 0.8541 - val_loss: 4.4975 - val_orgCE: 0.9798 - val_myAcc: 0.3073 - val_acc: 0.8487
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.2748 - orgCE: 0.9090 - myAcc: 0.3027 - acc: 0.8511 - val_loss: 4.4743 - val_orgCE: 0.9876 - val_myAcc: 0.3021 - val_acc: 0.8453
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.2070 - orgCE: 0.8983 - myAcc: 0.3068 - acc: 0.8515 - val_loss: 4.3379 - val_orgCE: 0.9041 - val_myAcc: 0.3204 - val_acc: 0.8580
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.2243 - orgCE: 0.9010 - myAcc: 0.3041 - acc: 0.8513 - val_loss: 4.3931 - val_orgCE: 0.9330 - val_myAcc: 0.3034 - val_acc: 0.8517
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.1548 - orgCE: 0.8712 - myAcc: 0.3088 - acc: 0.8548 - val_loss: 4.3618 - val_orgCE: 0.9334 - val_myAcc: 0.3139 - val_acc: 0.8530
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.1809 - orgCE: 0.9045 - myAcc: 0.3054 - acc: 0.8491 - val_loss: 4.2940 - val_orgCE: 0.9137 - val_myAcc: 0.3146 - val_acc: 0.8542
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.1556 - orgCE: 0.8948 - myAcc: 0.3063 - acc: 0.8504 - val_loss: 4.3114 - val_orgCE: 0.8986 - val_myAcc: 0.3190 - val_acc: 0.8577
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.0706 - orgCE: 0.8609 - myAcc: 0.3143 - acc: 0.8542 - val_loss: 4.2276 - val_orgCE: 0.8797 - val_myAcc: 0.3412 - val_acc: 0.8616
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.9926 - orgCE: 0.8418 - myAcc: 0.3281 - acc: 0.8574 - val_loss: 4.2810 - val_orgCE: 0.9427 - val_myAcc: 0.3261 - val_acc: 0.8502
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.9594 - orgCE: 0.8306 - myAcc: 0.3272 - acc: 0.8569 - val_loss: 4.2100 - val_orgCE: 0.9012 - val_myAcc: 0.3250 - val_acc: 0.8543
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.9606 - orgCE: 0.8368 - myAcc: 0.3262 - acc: 0.8554 - val_loss: 4.3085 - val_orgCE: 0.9369 - val_myAcc: 0.3260 - val_acc: 0.8452
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 4.0015 - orgCE: 0.8739 - myAcc: 0.3229 - acc: 0.8463 - val_loss: 4.2833 - val_orgCE: 0.9468 - val_myAcc: 0.3210 - val_acc: 0.8478
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.9810 - orgCE: 0.8480 - myAcc: 0.3244 - acc: 0.8517 - val_loss: 4.2061 - val_orgCE: 0.8929 - val_myAcc: 0.3336 - val_acc: 0.8561
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.9801 - orgCE: 0.8603 - myAcc: 0.3209 - acc: 0.8478 - val_loss: 4.2447 - val_orgCE: 0.9361 - val_myAcc: 0.3306 - val_acc: 0.8506
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.8617 - orgCE: 0.8172 - myAcc: 0.3423 - acc: 0.8538 - val_loss: 4.2293 - val_orgCE: 0.9181 - val_myAcc: 0.3430 - val_acc: 0.8468
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.8323 - orgCE: 0.8074 - myAcc: 0.3482 - acc: 0.8567 - val_loss: 4.1231 - val_orgCE: 0.8981 - val_myAcc: 0.3445 - val_acc: 0.8536
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.8452 - orgCE: 0.8092 - myAcc: 0.3385 - acc: 0.8534 - val_loss: 4.1406 - val_orgCE: 0.8893 - val_myAcc: 0.3475 - val_acc: 0.8563
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.8225 - orgCE: 0.8121 - myAcc: 0.3494 - acc: 0.8531 - val_loss: 4.1141 - val_orgCE: 0.8646 - val_myAcc: 0.3543 - val_acc: 0.8569
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.8492 - orgCE: 0.8373 - myAcc: 0.3433 - acc: 0.8524 - val_loss: 4.2046 - val_orgCE: 0.9031 - val_myAcc: 0.3401 - val_acc: 0.8505
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.7092 - orgCE: 0.7797 - myAcc: 0.3596 - acc: 0.8586 - val_loss: 3.9869 - val_orgCE: 0.8301 - val_myAcc: 0.3603 - val_acc: 0.8553
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.7048 - orgCE: 0.7920 - myAcc: 0.3609 - acc: 0.8567 - val_loss: 4.0626 - val_orgCE: 0.8626 - val_myAcc: 0.3513 - val_acc: 0.8578
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.7258 - orgCE: 0.8014 - myAcc: 0.3597 - acc: 0.8551 - val_loss: 4.1737 - val_orgCE: 0.9196 - val_myAcc: 0.3466 - val_acc: 0.8516
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.6606 - orgCE: 0.7826 - myAcc: 0.3643 - acc: 0.8562 - val_loss: 3.9302 - val_orgCE: 0.8139 - val_myAcc: 0.3571 - val_acc: 0.8602
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.6578 - orgCE: 0.7852 - myAcc: 0.3618 - acc: 0.8552 - val_loss: 3.9928 - val_orgCE: 0.8455 - val_myAcc: 0.3706 - val_acc: 0.8598
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.6319 - orgCE: 0.7779 - myAcc: 0.3663 - acc: 0.8561 - val_loss: 3.9463 - val_orgCE: 0.8220 - val_myAcc: 0.3653 - val_acc: 0.8594
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.6398 - orgCE: 0.7873 - myAcc: 0.3653 - acc: 0.8556 - val_loss: 3.9029 - val_orgCE: 0.8519 - val_myAcc: 0.3659 - val_acc: 0.8549
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.5677 - orgCE: 0.7678 - myAcc: 0.3761 - acc: 0.8586 - val_loss: 3.9034 - val_orgCE: 0.8201 - val_myAcc: 0.3773 - val_acc: 0.8652
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 68s - loss: 3.5549 - orgCE: 0.7472 - myAcc: 0.3732 - acc: 0.8624 - val_loss: 3.8264 - val_orgCE: 0.7959 - val_myAcc: 0.3791 - val_acc: 0.8646
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.5118 - orgCE: 0.7529 - myAcc: 0.3782 - acc: 0.8607 - val_loss: 3.8547 - val_orgCE: 0.8015 - val_myAcc: 0.3752 - val_acc: 0.8666
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.5757 - orgCE: 0.7756 - myAcc: 0.3670 - acc: 0.8572 - val_loss: 3.9159 - val_orgCE: 0.8269 - val_myAcc: 0.3632 - val_acc: 0.8602
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 68s - loss: 3.5354 - orgCE: 0.7541 - myAcc: 0.3759 - acc: 0.8606 - val_loss: 3.8673 - val_orgCE: 0.8335 - val_myAcc: 0.3609 - val_acc: 0.8563
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.4355 - orgCE: 0.7251 - myAcc: 0.3851 - acc: 0.8645 - val_loss: 3.8666 - val_orgCE: 0.8101 - val_myAcc: 0.3664 - val_acc: 0.8627
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 68s - loss: 3.5147 - orgCE: 0.7542 - myAcc: 0.3761 - acc: 0.8603 - val_loss: 3.9618 - val_orgCE: 0.8544 - val_myAcc: 0.3675 - val_acc: 0.8601
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.4460 - orgCE: 0.7315 - myAcc: 0.3821 - acc: 0.8639 - val_loss: 3.8087 - val_orgCE: 0.8132 - val_myAcc: 0.3723 - val_acc: 0.8613
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.3819 - orgCE: 0.7166 - myAcc: 0.3890 - acc: 0.8647 - val_loss: 3.8063 - val_orgCE: 0.7962 - val_myAcc: 0.3706 - val_acc: 0.8627
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.3782 - orgCE: 0.7242 - myAcc: 0.3938 - acc: 0.8643 - val_loss: 3.8275 - val_orgCE: 0.8010 - val_myAcc: 0.3804 - val_acc: 0.8660
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.3911 - orgCE: 0.7248 - myAcc: 0.3888 - acc: 0.8616 - val_loss: 3.8977 - val_orgCE: 0.8451 - val_myAcc: 0.3706 - val_acc: 0.8569
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.3427 - orgCE: 0.7117 - myAcc: 0.3915 - acc: 0.8647 - val_loss: 3.9039 - val_orgCE: 0.8740 - val_myAcc: 0.3587 - val_acc: 0.8483
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.3724 - orgCE: 0.7251 - myAcc: 0.3908 - acc: 0.8636 - val_loss: 3.7408 - val_orgCE: 0.7779 - val_myAcc: 0.3877 - val_acc: 0.8661
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.3188 - orgCE: 0.7077 - myAcc: 0.3904 - acc: 0.8633 - val_loss: 3.9041 - val_orgCE: 0.8466 - val_myAcc: 0.3746 - val_acc: 0.8542
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.3096 - orgCE: 0.7107 - myAcc: 0.3975 - acc: 0.8639 - val_loss: 3.8488 - val_orgCE: 0.8077 - val_myAcc: 0.3739 - val_acc: 0.8622
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 71s - loss: 3.2525 - orgCE: 0.6901 - myAcc: 0.3999 - acc: 0.8677 - val_loss: 3.9250 - val_orgCE: 0.8522 - val_myAcc: 0.3700 - val_acc: 0.8590
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.2422 - orgCE: 0.6851 - myAcc: 0.4008 - acc: 0.8663 - val_loss: 3.7055 - val_orgCE: 0.7809 - val_myAcc: 0.3915 - val_acc: 0.8645
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 68s - loss: 3.2824 - orgCE: 0.7077 - myAcc: 0.3926 - acc: 0.8597 - val_loss: 3.7679 - val_orgCE: 0.8182 - val_myAcc: 0.3770 - val_acc: 0.8601
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.2012 - orgCE: 0.6831 - myAcc: 0.4074 - acc: 0.8687 - val_loss: 3.8937 - val_orgCE: 0.8652 - val_myAcc: 0.3792 - val_acc: 0.8564
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 68s - loss: 3.2606 - orgCE: 0.7072 - myAcc: 0.4004 - acc: 0.8638 - val_loss: 3.7167 - val_orgCE: 0.7669 - val_myAcc: 0.3988 - val_acc: 0.8706
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.2533 - orgCE: 0.6979 - myAcc: 0.3985 - acc: 0.8629 - val_loss: 3.7138 - val_orgCE: 0.7885 - val_myAcc: 0.3919 - val_acc: 0.8646
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.1721 - orgCE: 0.6750 - myAcc: 0.4000 - acc: 0.8664 - val_loss: 3.7086 - val_orgCE: 0.7839 - val_myAcc: 0.3944 - val_acc: 0.8660
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.1516 - orgCE: 0.6691 - myAcc: 0.4155 - acc: 0.8701 - val_loss: 3.7683 - val_orgCE: 0.8025 - val_myAcc: 0.3840 - val_acc: 0.8622
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.1310 - orgCE: 0.6651 - myAcc: 0.4165 - acc: 0.8706 - val_loss: 3.7894 - val_orgCE: 0.8136 - val_myAcc: 0.3877 - val_acc: 0.8576
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.1514 - orgCE: 0.6738 - myAcc: 0.4094 - acc: 0.8656 - val_loss: 3.7251 - val_orgCE: 0.7979 - val_myAcc: 0.3875 - val_acc: 0.8624
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.1023 - orgCE: 0.6665 - myAcc: 0.4176 - acc: 0.8686 - val_loss: 3.7812 - val_orgCE: 0.8040 - val_myAcc: 0.3793 - val_acc: 0.8597
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.0956 - orgCE: 0.6609 - myAcc: 0.4204 - acc: 0.8707 - val_loss: 3.7816 - val_orgCE: 0.8195 - val_myAcc: 0.3908 - val_acc: 0.8649
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 68s - loss: 3.1175 - orgCE: 0.6609 - myAcc: 0.4131 - acc: 0.8671 - val_loss: 3.7458 - val_orgCE: 0.7950 - val_myAcc: 0.3817 - val_acc: 0.8602
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.0782 - orgCE: 0.6511 - myAcc: 0.4226 - acc: 0.8716 - val_loss: 3.7379 - val_orgCE: 0.8037 - val_myAcc: 0.3833 - val_acc: 0.8615
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.0555 - orgCE: 0.6533 - myAcc: 0.4249 - acc: 0.8690 - val_loss: 3.5709 - val_orgCE: 0.7406 - val_myAcc: 0.4031 - val_acc: 0.8678
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.0517 - orgCE: 0.6566 - myAcc: 0.4189 - acc: 0.8681 - val_loss: 3.6282 - val_orgCE: 0.7589 - val_myAcc: 0.4002 - val_acc: 0.8676
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 68s - loss: 2.9890 - orgCE: 0.6344 - myAcc: 0.4269 - acc: 0.8708 - val_loss: 3.7828 - val_orgCE: 0.8011 - val_myAcc: 0.3784 - val_acc: 0.8622
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.0214 - orgCE: 0.6441 - myAcc: 0.4292 - acc: 0.8713 - val_loss: 3.7948 - val_orgCE: 0.8189 - val_myAcc: 0.3847 - val_acc: 0.8570
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.0998 - orgCE: 0.6578 - myAcc: 0.4131 - acc: 0.8654 - val_loss: 3.9407 - val_orgCE: 0.8833 - val_myAcc: 0.3720 - val_acc: 0.8516
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.9589 - orgCE: 0.6274 - myAcc: 0.4278 - acc: 0.8731 - val_loss: 3.6900 - val_orgCE: 0.7751 - val_myAcc: 0.3955 - val_acc: 0.8688
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.9742 - orgCE: 0.6378 - myAcc: 0.4299 - acc: 0.8688 - val_loss: 3.7433 - val_orgCE: 0.8012 - val_myAcc: 0.3904 - val_acc: 0.8650
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.9340 - orgCE: 0.6257 - myAcc: 0.4293 - acc: 0.8667 - val_loss: 3.8107 - val_orgCE: 0.8192 - val_myAcc: 0.3763 - val_acc: 0.8621
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 2.9033 - orgCE: 0.6242 - myAcc: 0.4417 - acc: 0.8719 - val_loss: 3.8112 - val_orgCE: 0.8312 - val_myAcc: 0.3836 - val_acc: 0.8595
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 3.0142 - orgCE: 0.6467 - myAcc: 0.4229 - acc: 0.8684 - val_loss: 3.8130 - val_orgCE: 0.8236 - val_myAcc: 0.3800 - val_acc: 0.8510
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.9292 - orgCE: 0.6215 - myAcc: 0.4305 - acc: 0.8689 - val_loss: 3.7760 - val_orgCE: 0.8376 - val_myAcc: 0.3862 - val_acc: 0.8614
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.8351 - orgCE: 0.5888 - myAcc: 0.4482 - acc: 0.8780 - val_loss: 3.6537 - val_orgCE: 0.7778 - val_myAcc: 0.3947 - val_acc: 0.8663
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.8769 - orgCE: 0.6104 - myAcc: 0.4392 - acc: 0.8720 - val_loss: 3.7644 - val_orgCE: 0.8152 - val_myAcc: 0.3933 - val_acc: 0.8622
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 68s - loss: 2.8856 - orgCE: 0.6100 - myAcc: 0.4401 - acc: 0.8762 - val_loss: 3.5167 - val_orgCE: 0.7270 - val_myAcc: 0.4091 - val_acc: 0.8712
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.9098 - orgCE: 0.6193 - myAcc: 0.4357 - acc: 0.8728 - val_loss: 3.7845 - val_orgCE: 0.8395 - val_myAcc: 0.3752 - val_acc: 0.8581
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.8142 - orgCE: 0.5982 - myAcc: 0.4466 - acc: 0.8764 - val_loss: 3.6822 - val_orgCE: 0.7832 - val_myAcc: 0.3890 - val_acc: 0.8660
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.8317 - orgCE: 0.5954 - myAcc: 0.4500 - acc: 0.8782 - val_loss: 3.7555 - val_orgCE: 0.8112 - val_myAcc: 0.3778 - val_acc: 0.8633
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.8657 - orgCE: 0.6138 - myAcc: 0.4412 - acc: 0.8701 - val_loss: 3.7469 - val_orgCE: 0.8103 - val_myAcc: 0.3966 - val_acc: 0.8664
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.8240 - orgCE: 0.6074 - myAcc: 0.4461 - acc: 0.8746 - val_loss: 3.7318 - val_orgCE: 0.7911 - val_myAcc: 0.3882 - val_acc: 0.8623
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.8519 - orgCE: 0.6068 - myAcc: 0.4382 - acc: 0.8731 - val_loss: 3.5810 - val_orgCE: 0.7629 - val_myAcc: 0.4029 - val_acc: 0.8626
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.8168 - orgCE: 0.6001 - myAcc: 0.4471 - acc: 0.8751 - val_loss: 3.5550 - val_orgCE: 0.7485 - val_myAcc: 0.4099 - val_acc: 0.8690
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.7946 - orgCE: 0.5969 - myAcc: 0.4454 - acc: 0.8724 - val_loss: 3.6342 - val_orgCE: 0.7805 - val_myAcc: 0.4057 - val_acc: 0.8652
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.7549 - orgCE: 0.5828 - myAcc: 0.4551 - acc: 0.8800 - val_loss: 3.6529 - val_orgCE: 0.7746 - val_myAcc: 0.3863 - val_acc: 0.8606
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.7876 - orgCE: 0.5927 - myAcc: 0.4546 - acc: 0.8768 - val_loss: 3.7699 - val_orgCE: 0.8141 - val_myAcc: 0.3949 - val_acc: 0.8626
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.7834 - orgCE: 0.5925 - myAcc: 0.4436 - acc: 0.8758 - val_loss: 3.7569 - val_orgCE: 0.8048 - val_myAcc: 0.3851 - val_acc: 0.8643
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.7484 - orgCE: 0.5795 - myAcc: 0.4486 - acc: 0.8768 - val_loss: 3.6488 - val_orgCE: 0.7788 - val_myAcc: 0.3978 - val_acc: 0.8682
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.8199 - orgCE: 0.6064 - myAcc: 0.4392 - acc: 0.8702 - val_loss: 3.6575 - val_orgCE: 0.7997 - val_myAcc: 0.3966 - val_acc: 0.8560
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.7337 - orgCE: 0.5813 - myAcc: 0.4557 - acc: 0.8766 - val_loss: 3.6089 - val_orgCE: 0.7594 - val_myAcc: 0.4017 - val_acc: 0.8683
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.7103 - orgCE: 0.5725 - myAcc: 0.4560 - acc: 0.8801 - val_loss: 3.6407 - val_orgCE: 0.7636 - val_myAcc: 0.4056 - val_acc: 0.8632
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.7662 - orgCE: 0.5933 - myAcc: 0.4455 - acc: 0.8737 - val_loss: 3.7520 - val_orgCE: 0.8036 - val_myAcc: 0.3930 - val_acc: 0.8582
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.7361 - orgCE: 0.5838 - myAcc: 0.4536 - acc: 0.8749 - val_loss: 3.7062 - val_orgCE: 0.7925 - val_myAcc: 0.4003 - val_acc: 0.8665
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.7185 - orgCE: 0.5813 - myAcc: 0.4578 - acc: 0.8767 - val_loss: 3.5526 - val_orgCE: 0.7549 - val_myAcc: 0.4085 - val_acc: 0.8669
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 69s - loss: 2.6685 - orgCE: 0.5634 - myAcc: 0.4633 - acc: 0.8806 - val_loss: 3.7286 - val_orgCE: 0.8183 - val_myAcc: 0.3839 - val_acc: 0.8596


# python3 bleu_eval.py sample_output_testset.txt
Originally, average bleu score is 0.2929367225996487
By another method, average bleu score is 0.6843100819118944
