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
Decoder_in (Concatenate)         (None, 121, 7156)     0           Encoder_out[0][0]                
                                                                   Labels_pad[0][0]                 
____________________________________________________________________________________________________
lstm_1 (LSTM)                    (None, 121, 1024)     33509376    Decoder_in[0][0]                 
____________________________________________________________________________________________________
cropping1d_1 (Cropping1D)        (None, 41, 1024)      0           lstm_1[0][0]                     
____________________________________________________________________________________________________
time_distributed_1 (TimeDistribu (None, 41, 6132)      6285300     cropping1d_1[0][0]               
====================================================================================================
Total params: 60,770,292
Trainable params: 60,770,292
Non-trainable params: 0
____________________________________________________________________________________________________

* Create a new model. *

* Epoch 1/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 60s - loss: 5.9824 - orgCE: 1.2820 - myAcc: 0.1378 - acc: 0.3378 - val_loss: 5.2858 - val_orgCE: 1.1201 - val_myAcc: 0.2086 - val_acc: 0.8323
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 5.0679 - orgCE: 1.0840 - myAcc: 0.2132 - acc: 0.8267 - val_loss: 5.0530 - val_orgCE: 1.1016 - val_myAcc: 0.2518 - val_acc: 0.6430
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.7170 - orgCE: 0.9875 - myAcc: 0.2982 - acc: 0.7245 - val_loss: 4.8031 - val_orgCE: 1.0315 - val_myAcc: 0.2869 - val_acc: 0.8448
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 4.6355 - orgCE: 0.9904 - myAcc: 0.2920 - acc: 0.8478 - val_loss: 4.7188 - val_orgCE: 1.0306 - val_myAcc: 0.3066 - val_acc: 0.8483
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.5832 - orgCE: 0.9958 - myAcc: 0.2939 - acc: 0.8461 - val_loss: 4.5974 - val_orgCE: 0.9838 - val_myAcc: 0.3123 - val_acc: 0.8519
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.4989 - orgCE: 0.9623 - myAcc: 0.2994 - acc: 0.8493 - val_loss: 4.6585 - val_orgCE: 1.0362 - val_myAcc: 0.3028 - val_acc: 0.8447
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.4490 - orgCE: 0.9430 - myAcc: 0.3048 - acc: 0.8523 - val_loss: 4.6089 - val_orgCE: 1.0007 - val_myAcc: 0.2978 - val_acc: 0.8461
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.4542 - orgCE: 0.9492 - myAcc: 0.3045 - acc: 0.8513 - val_loss: 4.4794 - val_orgCE: 0.9490 - val_myAcc: 0.3206 - val_acc: 0.8550
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.4676 - orgCE: 0.9677 - myAcc: 0.2941 - acc: 0.8462 - val_loss: 4.5708 - val_orgCE: 0.9843 - val_myAcc: 0.3053 - val_acc: 0.8501
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 4.3512 - orgCE: 0.9195 - myAcc: 0.3048 - acc: 0.8528 - val_loss: 4.4377 - val_orgCE: 0.9463 - val_myAcc: 0.3220 - val_acc: 0.8552
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.3050 - orgCE: 0.9044 - myAcc: 0.3090 - acc: 0.8546 - val_loss: 4.6276 - val_orgCE: 1.0150 - val_myAcc: 0.3011 - val_acc: 0.8464
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.3202 - orgCE: 0.9263 - myAcc: 0.3016 - acc: 0.8493 - val_loss: 4.4624 - val_orgCE: 0.9423 - val_myAcc: 0.3082 - val_acc: 0.8537
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.2564 - orgCE: 0.9206 - myAcc: 0.3020 - acc: 0.8486 - val_loss: 4.4854 - val_orgCE: 0.9726 - val_myAcc: 0.3017 - val_acc: 0.8483
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.2233 - orgCE: 0.8992 - myAcc: 0.3006 - acc: 0.8506 - val_loss: 4.4300 - val_orgCE: 0.9733 - val_myAcc: 0.3058 - val_acc: 0.8467
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 4.1414 - orgCE: 0.8729 - myAcc: 0.3103 - acc: 0.8534 - val_loss: 4.3964 - val_orgCE: 0.9467 - val_myAcc: 0.3108 - val_acc: 0.8504
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 4.1370 - orgCE: 0.8962 - myAcc: 0.3121 - acc: 0.8488 - val_loss: 4.2337 - val_orgCE: 0.8999 - val_myAcc: 0.3375 - val_acc: 0.8583
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.0256 - orgCE: 0.8513 - myAcc: 0.3242 - acc: 0.8538 - val_loss: 4.2723 - val_orgCE: 0.9474 - val_myAcc: 0.3322 - val_acc: 0.8468
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.0623 - orgCE: 0.8798 - myAcc: 0.3209 - acc: 0.8455 - val_loss: 4.2184 - val_orgCE: 0.8777 - val_myAcc: 0.3320 - val_acc: 0.8587
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.9954 - orgCE: 0.8434 - myAcc: 0.3296 - acc: 0.8540 - val_loss: 4.2374 - val_orgCE: 0.9073 - val_myAcc: 0.3418 - val_acc: 0.8568
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.9644 - orgCE: 0.8479 - myAcc: 0.3256 - acc: 0.8518 - val_loss: 4.1408 - val_orgCE: 0.8764 - val_myAcc: 0.3428 - val_acc: 0.8543
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.9678 - orgCE: 0.8481 - myAcc: 0.3287 - acc: 0.8496 - val_loss: 4.1310 - val_orgCE: 0.8823 - val_myAcc: 0.3312 - val_acc: 0.8546
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.9825 - orgCE: 0.8595 - myAcc: 0.3301 - acc: 0.8484 - val_loss: 4.1273 - val_orgCE: 0.8745 - val_myAcc: 0.3435 - val_acc: 0.8599
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.9202 - orgCE: 0.8388 - myAcc: 0.3310 - acc: 0.8528 - val_loss: 4.1054 - val_orgCE: 0.8844 - val_myAcc: 0.3449 - val_acc: 0.8504
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.8545 - orgCE: 0.8151 - myAcc: 0.3387 - acc: 0.8544 - val_loss: 4.0080 - val_orgCE: 0.8428 - val_myAcc: 0.3453 - val_acc: 0.8585
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.7906 - orgCE: 0.8114 - myAcc: 0.3462 - acc: 0.8513 - val_loss: 4.0089 - val_orgCE: 0.8209 - val_myAcc: 0.3569 - val_acc: 0.8616
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.8544 - orgCE: 0.8483 - myAcc: 0.3386 - acc: 0.8470 - val_loss: 3.9869 - val_orgCE: 0.8201 - val_myAcc: 0.3685 - val_acc: 0.8571
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.7724 - orgCE: 0.8096 - myAcc: 0.3504 - acc: 0.8532 - val_loss: 4.0811 - val_orgCE: 0.8923 - val_myAcc: 0.3606 - val_acc: 0.8563
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.7242 - orgCE: 0.7929 - myAcc: 0.3551 - acc: 0.8577 - val_loss: 4.0198 - val_orgCE: 0.8511 - val_myAcc: 0.3483 - val_acc: 0.8512
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.6543 - orgCE: 0.7652 - myAcc: 0.3625 - acc: 0.8589 - val_loss: 4.1092 - val_orgCE: 0.9011 - val_myAcc: 0.3451 - val_acc: 0.8550
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.6817 - orgCE: 0.7917 - myAcc: 0.3525 - acc: 0.8561 - val_loss: 3.9457 - val_orgCE: 0.8604 - val_myAcc: 0.3594 - val_acc: 0.8543
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.6341 - orgCE: 0.7686 - myAcc: 0.3637 - acc: 0.8602 - val_loss: 3.9010 - val_orgCE: 0.8162 - val_myAcc: 0.3674 - val_acc: 0.8648
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.6394 - orgCE: 0.7725 - myAcc: 0.3647 - acc: 0.8605 - val_loss: 3.9619 - val_orgCE: 0.8627 - val_myAcc: 0.3523 - val_acc: 0.8521
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.6647 - orgCE: 0.7876 - myAcc: 0.3635 - acc: 0.8581 - val_loss: 3.8102 - val_orgCE: 0.7844 - val_myAcc: 0.3696 - val_acc: 0.8615
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.5337 - orgCE: 0.7457 - myAcc: 0.3752 - acc: 0.8599 - val_loss: 3.8390 - val_orgCE: 0.7994 - val_myAcc: 0.3644 - val_acc: 0.8643
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.5353 - orgCE: 0.7474 - myAcc: 0.3731 - acc: 0.8608 - val_loss: 4.0026 - val_orgCE: 0.8440 - val_myAcc: 0.3639 - val_acc: 0.8632
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.4539 - orgCE: 0.7175 - myAcc: 0.3825 - acc: 0.8667 - val_loss: 3.8268 - val_orgCE: 0.8178 - val_myAcc: 0.3754 - val_acc: 0.8524
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.5386 - orgCE: 0.7725 - myAcc: 0.3723 - acc: 0.8524 - val_loss: 4.0214 - val_orgCE: 0.8600 - val_myAcc: 0.3654 - val_acc: 0.8604
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.4585 - orgCE: 0.7445 - myAcc: 0.3788 - acc: 0.8607 - val_loss: 3.8076 - val_orgCE: 0.8041 - val_myAcc: 0.3833 - val_acc: 0.8484
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.3776 - orgCE: 0.7210 - myAcc: 0.3861 - acc: 0.8542 - val_loss: 3.9453 - val_orgCE: 0.8538 - val_myAcc: 0.3670 - val_acc: 0.8599
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.4269 - orgCE: 0.7299 - myAcc: 0.3813 - acc: 0.8615 - val_loss: 3.8781 - val_orgCE: 0.8219 - val_myAcc: 0.3638 - val_acc: 0.8611
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.4164 - orgCE: 0.7341 - myAcc: 0.3840 - acc: 0.8610 - val_loss: 3.8351 - val_orgCE: 0.8075 - val_myAcc: 0.3751 - val_acc: 0.8642
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.4327 - orgCE: 0.7388 - myAcc: 0.3840 - acc: 0.8599 - val_loss: 3.8667 - val_orgCE: 0.8192 - val_myAcc: 0.3725 - val_acc: 0.8627
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.2464 - orgCE: 0.6718 - myAcc: 0.4021 - acc: 0.8702 - val_loss: 3.8073 - val_orgCE: 0.8187 - val_myAcc: 0.3803 - val_acc: 0.8570
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.3632 - orgCE: 0.7126 - myAcc: 0.3885 - acc: 0.8630 - val_loss: 3.7633 - val_orgCE: 0.8106 - val_myAcc: 0.3860 - val_acc: 0.8638
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.3449 - orgCE: 0.7123 - myAcc: 0.3905 - acc: 0.8642 - val_loss: 3.8278 - val_orgCE: 0.8228 - val_myAcc: 0.3898 - val_acc: 0.8655
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.2074 - orgCE: 0.6685 - myAcc: 0.4053 - acc: 0.8713 - val_loss: 3.7628 - val_orgCE: 0.7981 - val_myAcc: 0.3887 - val_acc: 0.8648
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.2158 - orgCE: 0.6734 - myAcc: 0.4090 - acc: 0.8714 - val_loss: 3.7140 - val_orgCE: 0.7681 - val_myAcc: 0.3910 - val_acc: 0.8688
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.2625 - orgCE: 0.7015 - myAcc: 0.3968 - acc: 0.8655 - val_loss: 3.8034 - val_orgCE: 0.8205 - val_myAcc: 0.3631 - val_acc: 0.8545
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.2611 - orgCE: 0.7033 - myAcc: 0.3969 - acc: 0.8619 - val_loss: 3.6548 - val_orgCE: 0.7518 - val_myAcc: 0.4035 - val_acc: 0.8745
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.1867 - orgCE: 0.6759 - myAcc: 0.4055 - acc: 0.8563 - val_loss: 3.8132 - val_orgCE: 0.8380 - val_myAcc: 0.3688 - val_acc: 0.8594
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.2114 - orgCE: 0.6849 - myAcc: 0.4106 - acc: 0.8600 - val_loss: 3.7952 - val_orgCE: 0.8137 - val_myAcc: 0.3720 - val_acc: 0.8605
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.1896 - orgCE: 0.6883 - myAcc: 0.4026 - acc: 0.8636 - val_loss: 3.7577 - val_orgCE: 0.8004 - val_myAcc: 0.3935 - val_acc: 0.8649
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.1690 - orgCE: 0.6673 - myAcc: 0.4032 - acc: 0.8680 - val_loss: 3.7255 - val_orgCE: 0.7862 - val_myAcc: 0.3932 - val_acc: 0.8696
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.1653 - orgCE: 0.6676 - myAcc: 0.4065 - acc: 0.8680 - val_loss: 3.7195 - val_orgCE: 0.7903 - val_myAcc: 0.3897 - val_acc: 0.8562
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.1663 - orgCE: 0.6859 - myAcc: 0.4104 - acc: 0.8591 - val_loss: 3.7133 - val_orgCE: 0.7791 - val_myAcc: 0.3897 - val_acc: 0.8696
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.1029 - orgCE: 0.6554 - myAcc: 0.4123 - acc: 0.8712 - val_loss: 3.8187 - val_orgCE: 0.8357 - val_myAcc: 0.3888 - val_acc: 0.8597
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.1347 - orgCE: 0.6678 - myAcc: 0.4062 - acc: 0.8656 - val_loss: 3.7710 - val_orgCE: 0.8099 - val_myAcc: 0.3815 - val_acc: 0.8614
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.0556 - orgCE: 0.6428 - myAcc: 0.4228 - acc: 0.8681 - val_loss: 3.7495 - val_orgCE: 0.8011 - val_myAcc: 0.3873 - val_acc: 0.8611
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.0732 - orgCE: 0.6609 - myAcc: 0.4206 - acc: 0.8672 - val_loss: 3.6597 - val_orgCE: 0.7613 - val_myAcc: 0.3983 - val_acc: 0.8692
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.1526 - orgCE: 0.6901 - myAcc: 0.4069 - acc: 0.8629 - val_loss: 3.6996 - val_orgCE: 0.8105 - val_myAcc: 0.3891 - val_acc: 0.8605
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.0631 - orgCE: 0.6576 - myAcc: 0.4201 - acc: 0.8678 - val_loss: 3.7160 - val_orgCE: 0.7814 - val_myAcc: 0.3935 - val_acc: 0.8636
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.0036 - orgCE: 0.6283 - myAcc: 0.4306 - acc: 0.8739 - val_loss: 3.5471 - val_orgCE: 0.7315 - val_myAcc: 0.4129 - val_acc: 0.8717
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.9858 - orgCE: 0.6304 - myAcc: 0.4259 - acc: 0.8734 - val_loss: 3.7374 - val_orgCE: 0.7796 - val_myAcc: 0.3919 - val_acc: 0.8670
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 3.0194 - orgCE: 0.6504 - myAcc: 0.4232 - acc: 0.8679 - val_loss: 3.5468 - val_orgCE: 0.7461 - val_myAcc: 0.4032 - val_acc: 0.8678
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.9690 - orgCE: 0.6368 - myAcc: 0.4324 - acc: 0.8689 - val_loss: 3.7074 - val_orgCE: 0.7982 - val_myAcc: 0.3944 - val_acc: 0.8651
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 2.9673 - orgCE: 0.6276 - myAcc: 0.4318 - acc: 0.8743 - val_loss: 3.5240 - val_orgCE: 0.7426 - val_myAcc: 0.4017 - val_acc: 0.8606
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 2.9345 - orgCE: 0.6244 - myAcc: 0.4343 - acc: 0.8731 - val_loss: 3.6287 - val_orgCE: 0.7756 - val_myAcc: 0.3969 - val_acc: 0.8663
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.9706 - orgCE: 0.6359 - myAcc: 0.4262 - acc: 0.8714 - val_loss: 3.6473 - val_orgCE: 0.7727 - val_myAcc: 0.4042 - val_acc: 0.8680
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.9448 - orgCE: 0.6322 - myAcc: 0.4288 - acc: 0.8617 - val_loss: 3.6098 - val_orgCE: 0.7808 - val_myAcc: 0.3907 - val_acc: 0.8611
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.9462 - orgCE: 0.6322 - myAcc: 0.4292 - acc: 0.8689 - val_loss: 3.6403 - val_orgCE: 0.7971 - val_myAcc: 0.3907 - val_acc: 0.8629
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8972 - orgCE: 0.6116 - myAcc: 0.4349 - acc: 0.8752 - val_loss: 3.6282 - val_orgCE: 0.7609 - val_myAcc: 0.4017 - val_acc: 0.8705
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8972 - orgCE: 0.6182 - myAcc: 0.4375 - acc: 0.8696 - val_loss: 3.7028 - val_orgCE: 0.7923 - val_myAcc: 0.3934 - val_acc: 0.8618
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.9016 - orgCE: 0.6210 - myAcc: 0.4401 - acc: 0.8714 - val_loss: 3.7468 - val_orgCE: 0.8185 - val_myAcc: 0.3858 - val_acc: 0.8590
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8331 - orgCE: 0.5954 - myAcc: 0.4445 - acc: 0.8685 - val_loss: 3.7560 - val_orgCE: 0.8199 - val_myAcc: 0.4008 - val_acc: 0.8674
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8662 - orgCE: 0.6128 - myAcc: 0.4410 - acc: 0.8734 - val_loss: 3.6344 - val_orgCE: 0.7886 - val_myAcc: 0.4060 - val_acc: 0.8622
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 2.8255 - orgCE: 0.6064 - myAcc: 0.4452 - acc: 0.8746 - val_loss: 3.6912 - val_orgCE: 0.8012 - val_myAcc: 0.4034 - val_acc: 0.8643
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8207 - orgCE: 0.5982 - myAcc: 0.4483 - acc: 0.8745 - val_loss: 3.6567 - val_orgCE: 0.7597 - val_myAcc: 0.4061 - val_acc: 0.8632
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8726 - orgCE: 0.6199 - myAcc: 0.4387 - acc: 0.8446 - val_loss: 3.6376 - val_orgCE: 0.7728 - val_myAcc: 0.3981 - val_acc: 0.8549
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8016 - orgCE: 0.6050 - myAcc: 0.4491 - acc: 0.8740 - val_loss: 3.5762 - val_orgCE: 0.7468 - val_myAcc: 0.4039 - val_acc: 0.8628
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.7683 - orgCE: 0.5790 - myAcc: 0.4587 - acc: 0.8693 - val_loss: 3.4746 - val_orgCE: 0.7329 - val_myAcc: 0.4058 - val_acc: 0.8642
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8214 - orgCE: 0.6070 - myAcc: 0.4452 - acc: 0.8664 - val_loss: 3.7367 - val_orgCE: 0.8072 - val_myAcc: 0.3959 - val_acc: 0.8611
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 2.7855 - orgCE: 0.5994 - myAcc: 0.4487 - acc: 0.8644 - val_loss: 3.7369 - val_orgCE: 0.8167 - val_myAcc: 0.3907 - val_acc: 0.8591
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.7697 - orgCE: 0.5916 - myAcc: 0.4516 - acc: 0.8722 - val_loss: 3.4865 - val_orgCE: 0.7280 - val_myAcc: 0.4116 - val_acc: 0.8723
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.7311 - orgCE: 0.5745 - myAcc: 0.4583 - acc: 0.8782 - val_loss: 3.5625 - val_orgCE: 0.7607 - val_myAcc: 0.4045 - val_acc: 0.8626
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.6956 - orgCE: 0.5676 - myAcc: 0.4617 - acc: 0.8786 - val_loss: 3.6370 - val_orgCE: 0.7723 - val_myAcc: 0.4036 - val_acc: 0.8690
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.7487 - orgCE: 0.5907 - myAcc: 0.4523 - acc: 0.8586 - val_loss: 3.5886 - val_orgCE: 0.7618 - val_myAcc: 0.4151 - val_acc: 0.8685
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.6857 - orgCE: 0.5719 - myAcc: 0.4630 - acc: 0.8754 - val_loss: 3.6468 - val_orgCE: 0.7883 - val_myAcc: 0.4078 - val_acc: 0.8330
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.7099 - orgCE: 0.5767 - myAcc: 0.4615 - acc: 0.8712 - val_loss: 3.6965 - val_orgCE: 0.8031 - val_myAcc: 0.3980 - val_acc: 0.8643
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.6812 - orgCE: 0.5576 - myAcc: 0.4606 - acc: 0.8776 - val_loss: 3.6585 - val_orgCE: 0.7935 - val_myAcc: 0.3890 - val_acc: 0.8655
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.6546 - orgCE: 0.5491 - myAcc: 0.4644 - acc: 0.8618 - val_loss: 3.6552 - val_orgCE: 0.7759 - val_myAcc: 0.3953 - val_acc: 0.8580
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.7167 - orgCE: 0.5806 - myAcc: 0.4563 - acc: 0.8716 - val_loss: 3.6521 - val_orgCE: 0.7910 - val_myAcc: 0.4045 - val_acc: 0.8655
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.6569 - orgCE: 0.5630 - myAcc: 0.4647 - acc: 0.8769 - val_loss: 3.6501 - val_orgCE: 0.7968 - val_myAcc: 0.4005 - val_acc: 0.8648
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.6652 - orgCE: 0.5774 - myAcc: 0.4635 - acc: 0.8706 - val_loss: 3.5335 - val_orgCE: 0.7622 - val_myAcc: 0.4153 - val_acc: 0.8707
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 2.6036 - orgCE: 0.5473 - myAcc: 0.4692 - acc: 0.8453 - val_loss: 3.5993 - val_orgCE: 0.7726 - val_myAcc: 0.4090 - val_acc: 0.8655
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.6261 - orgCE: 0.5625 - myAcc: 0.4649 - acc: 0.8537 - val_loss: 3.6565 - val_orgCE: 0.7962 - val_myAcc: 0.4099 - val_acc: 0.8632
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.6104 - orgCE: 0.5538 - myAcc: 0.4667 - acc: 0.8787 - val_loss: 3.5338 - val_orgCE: 0.7332 - val_myAcc: 0.4249 - val_acc: 0.8491
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 2.6552 - orgCE: 0.5715 - myAcc: 0.4657 - acc: 0.8525 - val_loss: 3.5747 - val_orgCE: 0.7557 - val_myAcc: 0.4041 - val_acc: 0.8675
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 2.5671 - orgCE: 0.5444 - myAcc: 0.4736 - acc: 0.8776 - val_loss: 3.6203 - val_orgCE: 0.7801 - val_myAcc: 0.4042 - val_acc: 0.8230
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 58s - loss: 2.5885 - orgCE: 0.5567 - myAcc: 0.4689 - acc: 0.8572 - val_loss: 3.5597 - val_orgCE: 0.7466 - val_myAcc: 0.3923 - val_acc: 0.8629
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.5923 - orgCE: 0.5422 - myAcc: 0.4724 - acc: 0.8734 - val_loss: 3.7391 - val_orgCE: 0.8221 - val_myAcc: 0.3906 - val_acc: 0.8637
