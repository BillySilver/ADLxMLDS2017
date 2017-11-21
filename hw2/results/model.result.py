____________________________________________________________________________________________________
Layer (type)                     Output Shape          Param #     Connected to                     
====================================================================================================
Labels_in (InputLayer)           (None, 41, 6132)      0                                            
____________________________________________________________________________________________________
Encoder_in (InputLayer)          (None, 80, 4096)      0                                            
____________________________________________________________________________________________________
bos_padding_1 (BOSPadding)       (None, 41, 6132)      0           Labels_in[0][0]                  
____________________________________________________________________________________________________
Encoder_out (LSTM)               (None, 80, 1024)      20975616    Encoder_in[0][0]                 
____________________________________________________________________________________________________
Decoder (RecurrentWrapper)       (None, 41, 6132)      39796726.0  bos_padding_1[0][0]              
                                                                   Encoder_out[0][0]                
====================================================================================================
Total params: 60,772,342
Trainable params: 60,772,341
Non-trainable params: 1
____________________________________________________________________________________________________

* Create a new model. *

* Epoch 1/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 49s - loss: 6.4932 - orgCE: 1.3805 - myAcc: 0.2071 - acc: 0.6139 - val_loss: 5.7415 - val_orgCE: 1.2017 - val_myAcc: 0.2941 - val_acc: 0.8520
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 5.6186 - orgCE: 1.1876 - myAcc: 0.2861 - acc: 0.8490 - val_loss: 5.5422 - val_orgCE: 1.1874 - val_myAcc: 0.3061 - val_acc: 0.8512
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 5.4816 - orgCE: 1.1795 - myAcc: 0.2508 - acc: 0.8382 - val_loss: 5.4878 - val_orgCE: 1.1776 - val_myAcc: 0.2252 - val_acc: 0.8328
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 5.3785 - orgCE: 1.1305 - myAcc: 0.2285 - acc: 0.8372 - val_loss: 5.4989 - val_orgCE: 1.1748 - val_myAcc: 0.2252 - val_acc: 0.8343
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 5.2450 - orgCE: 1.0993 - myAcc: 0.2278 - acc: 0.8377 - val_loss: 5.3216 - val_orgCE: 1.1257 - val_myAcc: 0.2272 - val_acc: 0.8365
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 5.1395 - orgCE: 1.0985 - myAcc: 0.2297 - acc: 0.8343 - val_loss: 5.1049 - val_orgCE: 1.0554 - val_myAcc: 0.2435 - val_acc: 0.8432
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.9513 - orgCE: 1.0714 - myAcc: 0.2225 - acc: 0.8310 - val_loss: 4.9346 - val_orgCE: 1.0474 - val_myAcc: 0.2417 - val_acc: 0.8389
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.7218 - orgCE: 1.0028 - myAcc: 0.2622 - acc: 0.8427 - val_loss: 4.7567 - val_orgCE: 0.9961 - val_myAcc: 0.3039 - val_acc: 0.8542
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.3923 - orgCE: 0.9282 - myAcc: 0.3115 - acc: 0.8541 - val_loss: 4.5819 - val_orgCE: 0.9507 - val_myAcc: 0.3154 - val_acc: 0.8574
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.4216 - orgCE: 0.9350 - myAcc: 0.3038 - acc: 0.8523 - val_loss: 4.6597 - val_orgCE: 1.0017 - val_myAcc: 0.3006 - val_acc: 0.8496
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 4.3072 - orgCE: 0.9181 - myAcc: 0.3054 - acc: 0.8516 - val_loss: 4.4778 - val_orgCE: 0.9347 - val_myAcc: 0.3147 - val_acc: 0.8553
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 4.2761 - orgCE: 0.8941 - myAcc: 0.3149 - acc: 0.8563 - val_loss: 4.4873 - val_orgCE: 0.9671 - val_myAcc: 0.3198 - val_acc: 0.8531
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 4.2983 - orgCE: 0.9124 - myAcc: 0.3049 - acc: 0.8519 - val_loss: 4.5365 - val_orgCE: 0.9863 - val_myAcc: 0.3223 - val_acc: 0.8524
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.2911 - orgCE: 0.9251 - myAcc: 0.3059 - acc: 0.8501 - val_loss: 4.5636 - val_orgCE: 0.9844 - val_myAcc: 0.2970 - val_acc: 0.8475
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 4.2600 - orgCE: 0.9040 - myAcc: 0.3052 - acc: 0.8521 - val_loss: 4.4787 - val_orgCE: 0.9730 - val_myAcc: 0.3127 - val_acc: 0.8502
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.2665 - orgCE: 0.9221 - myAcc: 0.3082 - acc: 0.8502 - val_loss: 4.5267 - val_orgCE: 1.0014 - val_myAcc: 0.3092 - val_acc: 0.8467
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.1248 - orgCE: 0.8801 - myAcc: 0.3126 - acc: 0.8531 - val_loss: 4.4283 - val_orgCE: 0.9422 - val_myAcc: 0.3137 - val_acc: 0.8537
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 4.1822 - orgCE: 0.8995 - myAcc: 0.3104 - acc: 0.8511 - val_loss: 4.5237 - val_orgCE: 0.9643 - val_myAcc: 0.3059 - val_acc: 0.8512
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.0948 - orgCE: 0.8646 - myAcc: 0.3283 - acc: 0.8576 - val_loss: 4.4481 - val_orgCE: 0.9547 - val_myAcc: 0.3222 - val_acc: 0.8542
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.0748 - orgCE: 0.8633 - myAcc: 0.3261 - acc: 0.8556 - val_loss: 4.5293 - val_orgCE: 0.9753 - val_myAcc: 0.3122 - val_acc: 0.8515
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.0297 - orgCE: 0.8578 - myAcc: 0.3325 - acc: 0.8574 - val_loss: 4.4643 - val_orgCE: 0.9672 - val_myAcc: 0.3158 - val_acc: 0.8516
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.0133 - orgCE: 0.8578 - myAcc: 0.3396 - acc: 0.8563 - val_loss: 4.3843 - val_orgCE: 0.9343 - val_myAcc: 0.3258 - val_acc: 0.8535
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.9867 - orgCE: 0.8611 - myAcc: 0.3410 - acc: 0.8547 - val_loss: 4.4852 - val_orgCE: 0.9683 - val_myAcc: 0.3123 - val_acc: 0.8446
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.9328 - orgCE: 0.8369 - myAcc: 0.3471 - acc: 0.8564 - val_loss: 4.3410 - val_orgCE: 0.9229 - val_myAcc: 0.3154 - val_acc: 0.8423
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.9324 - orgCE: 0.8424 - myAcc: 0.3449 - acc: 0.8524 - val_loss: 4.3833 - val_orgCE: 0.9400 - val_myAcc: 0.3089 - val_acc: 0.8366
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.8637 - orgCE: 0.8325 - myAcc: 0.3545 - acc: 0.8553 - val_loss: 4.3537 - val_orgCE: 0.9244 - val_myAcc: 0.3054 - val_acc: 0.8442
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.8641 - orgCE: 0.8350 - myAcc: 0.3498 - acc: 0.8521 - val_loss: 4.5146 - val_orgCE: 0.9459 - val_myAcc: 0.2944 - val_acc: 0.8470
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.8857 - orgCE: 0.8450 - myAcc: 0.3498 - acc: 0.8519 - val_loss: 4.3540 - val_orgCE: 0.9318 - val_myAcc: 0.3122 - val_acc: 0.8437
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.8827 - orgCE: 0.8414 - myAcc: 0.3537 - acc: 0.8535 - val_loss: 4.4428 - val_orgCE: 0.9767 - val_myAcc: 0.3154 - val_acc: 0.8399
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.8246 - orgCE: 0.8234 - myAcc: 0.3565 - acc: 0.8547 - val_loss: 4.4329 - val_orgCE: 0.9569 - val_myAcc: 0.3077 - val_acc: 0.8502
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.7317 - orgCE: 0.7933 - myAcc: 0.3670 - acc: 0.8558 - val_loss: 4.3768 - val_orgCE: 0.9125 - val_myAcc: 0.3214 - val_acc: 0.8559
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.7795 - orgCE: 0.8136 - myAcc: 0.3666 - acc: 0.8580 - val_loss: 4.4574 - val_orgCE: 0.9691 - val_myAcc: 0.3096 - val_acc: 0.8460
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.7066 - orgCE: 0.7947 - myAcc: 0.3660 - acc: 0.8576 - val_loss: 4.2602 - val_orgCE: 0.8916 - val_myAcc: 0.3354 - val_acc: 0.8525
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.6621 - orgCE: 0.7744 - myAcc: 0.3775 - acc: 0.8612 - val_loss: 4.5350 - val_orgCE: 0.9883 - val_myAcc: 0.3063 - val_acc: 0.8462
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.6634 - orgCE: 0.7809 - myAcc: 0.3683 - acc: 0.8599 - val_loss: 4.5903 - val_orgCE: 0.9905 - val_myAcc: 0.2908 - val_acc: 0.8447
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.6642 - orgCE: 0.7920 - myAcc: 0.3680 - acc: 0.8574 - val_loss: 4.4966 - val_orgCE: 0.9485 - val_myAcc: 0.3068 - val_acc: 0.8444
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.6561 - orgCE: 0.7906 - myAcc: 0.3720 - acc: 0.8581 - val_loss: 4.3838 - val_orgCE: 0.9502 - val_myAcc: 0.2959 - val_acc: 0.8308
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.6510 - orgCE: 0.7991 - myAcc: 0.3747 - acc: 0.8553 - val_loss: 4.4201 - val_orgCE: 0.9400 - val_myAcc: 0.3115 - val_acc: 0.8485
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.6211 - orgCE: 0.7744 - myAcc: 0.3752 - acc: 0.8621 - val_loss: 4.3659 - val_orgCE: 0.9254 - val_myAcc: 0.3077 - val_acc: 0.8506
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.5693 - orgCE: 0.7641 - myAcc: 0.3816 - acc: 0.8627 - val_loss: 4.4242 - val_orgCE: 0.9359 - val_myAcc: 0.3180 - val_acc: 0.8516
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.5088 - orgCE: 0.7478 - myAcc: 0.3869 - acc: 0.8656 - val_loss: 4.4929 - val_orgCE: 0.9955 - val_myAcc: 0.2988 - val_acc: 0.8402
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.5130 - orgCE: 0.7404 - myAcc: 0.3887 - acc: 0.8660 - val_loss: 4.4141 - val_orgCE: 0.9323 - val_myAcc: 0.3106 - val_acc: 0.8426
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.5270 - orgCE: 0.7484 - myAcc: 0.3890 - acc: 0.8635 - val_loss: 4.4853 - val_orgCE: 0.9555 - val_myAcc: 0.3105 - val_acc: 0.8505
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4919 - orgCE: 0.7382 - myAcc: 0.3830 - acc: 0.8639 - val_loss: 4.4554 - val_orgCE: 0.9216 - val_myAcc: 0.3035 - val_acc: 0.8521
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4510 - orgCE: 0.7221 - myAcc: 0.3995 - acc: 0.8682 - val_loss: 4.5432 - val_orgCE: 1.0140 - val_myAcc: 0.3225 - val_acc: 0.8485
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4247 - orgCE: 0.7282 - myAcc: 0.3951 - acc: 0.8646 - val_loss: 4.5677 - val_orgCE: 0.9928 - val_myAcc: 0.2937 - val_acc: 0.8448
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.4887 - orgCE: 0.7472 - myAcc: 0.3911 - acc: 0.8633 - val_loss: 4.4487 - val_orgCE: 0.9286 - val_myAcc: 0.3010 - val_acc: 0.8508
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4035 - orgCE: 0.7218 - myAcc: 0.3978 - acc: 0.8668 - val_loss: 4.4408 - val_orgCE: 0.9737 - val_myAcc: 0.3109 - val_acc: 0.8437
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4409 - orgCE: 0.7294 - myAcc: 0.3944 - acc: 0.8656 - val_loss: 4.5607 - val_orgCE: 0.9907 - val_myAcc: 0.2924 - val_acc: 0.8419
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4012 - orgCE: 0.7366 - myAcc: 0.3933 - acc: 0.8604 - val_loss: 4.4558 - val_orgCE: 0.9410 - val_myAcc: 0.2975 - val_acc: 0.8492
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4193 - orgCE: 0.7293 - myAcc: 0.3949 - acc: 0.8646 - val_loss: 4.4178 - val_orgCE: 0.9284 - val_myAcc: 0.3046 - val_acc: 0.8519
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4125 - orgCE: 0.7302 - myAcc: 0.3937 - acc: 0.8633 - val_loss: 4.4320 - val_orgCE: 0.9257 - val_myAcc: 0.3024 - val_acc: 0.8536
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.3157 - orgCE: 0.6998 - myAcc: 0.4075 - acc: 0.8695 - val_loss: 4.5798 - val_orgCE: 0.9667 - val_myAcc: 0.2954 - val_acc: 0.8429
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.2968 - orgCE: 0.6873 - myAcc: 0.4057 - acc: 0.8705 - val_loss: 4.5261 - val_orgCE: 0.9767 - val_myAcc: 0.2909 - val_acc: 0.8394
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.3846 - orgCE: 0.7312 - myAcc: 0.3967 - acc: 0.8626 - val_loss: 4.3427 - val_orgCE: 0.9073 - val_myAcc: 0.3086 - val_acc: 0.8490
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.3342 - orgCE: 0.7072 - myAcc: 0.3975 - acc: 0.8654 - val_loss: 4.5587 - val_orgCE: 1.0003 - val_myAcc: 0.2987 - val_acc: 0.8417
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.2924 - orgCE: 0.6909 - myAcc: 0.4124 - acc: 0.8703 - val_loss: 4.4631 - val_orgCE: 0.9234 - val_myAcc: 0.3024 - val_acc: 0.8469
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.3396 - orgCE: 0.7201 - myAcc: 0.3984 - acc: 0.8639 - val_loss: 4.4880 - val_orgCE: 0.9485 - val_myAcc: 0.3000 - val_acc: 0.8470
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.3325 - orgCE: 0.7258 - myAcc: 0.4025 - acc: 0.8630 - val_loss: 4.5716 - val_orgCE: 0.9737 - val_myAcc: 0.2905 - val_acc: 0.8438
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.2733 - orgCE: 0.6824 - myAcc: 0.4065 - acc: 0.8707 - val_loss: 4.3757 - val_orgCE: 0.9095 - val_myAcc: 0.3169 - val_acc: 0.8532
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.2035 - orgCE: 0.6771 - myAcc: 0.4206 - acc: 0.8709 - val_loss: 4.5566 - val_orgCE: 0.9585 - val_myAcc: 0.2966 - val_acc: 0.8472
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.3208 - orgCE: 0.7211 - myAcc: 0.4014 - acc: 0.8627 - val_loss: 4.5370 - val_orgCE: 0.9820 - val_myAcc: 0.2883 - val_acc: 0.8398
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.2507 - orgCE: 0.7081 - myAcc: 0.4097 - acc: 0.8646 - val_loss: 4.4810 - val_orgCE: 0.9651 - val_myAcc: 0.3158 - val_acc: 0.8488
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.2023 - orgCE: 0.6723 - myAcc: 0.4145 - acc: 0.8708 - val_loss: 4.5828 - val_orgCE: 0.9781 - val_myAcc: 0.3015 - val_acc: 0.8447
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1842 - orgCE: 0.6739 - myAcc: 0.4190 - acc: 0.8700 - val_loss: 4.7156 - val_orgCE: 1.0454 - val_myAcc: 0.2727 - val_acc: 0.8325
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.2691 - orgCE: 0.7035 - myAcc: 0.4117 - acc: 0.8661 - val_loss: 4.4930 - val_orgCE: 0.9725 - val_myAcc: 0.2959 - val_acc: 0.8417
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.2087 - orgCE: 0.6830 - myAcc: 0.4135 - acc: 0.8669 - val_loss: 4.6841 - val_orgCE: 1.0274 - val_myAcc: 0.2867 - val_acc: 0.8388
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1675 - orgCE: 0.6752 - myAcc: 0.4138 - acc: 0.8670 - val_loss: 4.5947 - val_orgCE: 1.0448 - val_myAcc: 0.2863 - val_acc: 0.8343
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.1293 - orgCE: 0.6529 - myAcc: 0.4220 - acc: 0.8726 - val_loss: 4.3476 - val_orgCE: 0.9284 - val_myAcc: 0.3158 - val_acc: 0.8516
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1492 - orgCE: 0.6673 - myAcc: 0.4206 - acc: 0.8694 - val_loss: 4.6050 - val_orgCE: 0.9804 - val_myAcc: 0.2977 - val_acc: 0.8469
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0812 - orgCE: 0.6455 - myAcc: 0.4323 - acc: 0.8749 - val_loss: 4.7113 - val_orgCE: 1.0279 - val_myAcc: 0.2740 - val_acc: 0.8317
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.2533 - orgCE: 0.7122 - myAcc: 0.4063 - acc: 0.8602 - val_loss: 4.6145 - val_orgCE: 0.9770 - val_myAcc: 0.3032 - val_acc: 0.8483
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1787 - orgCE: 0.6766 - myAcc: 0.4184 - acc: 0.8653 - val_loss: 4.5812 - val_orgCE: 1.0169 - val_myAcc: 0.3049 - val_acc: 0.8432
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1177 - orgCE: 0.6669 - myAcc: 0.4222 - acc: 0.8683 - val_loss: 4.6284 - val_orgCE: 0.9677 - val_myAcc: 0.3056 - val_acc: 0.8492
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.0739 - orgCE: 0.6511 - myAcc: 0.4296 - acc: 0.8694 - val_loss: 4.5523 - val_orgCE: 0.9570 - val_myAcc: 0.3004 - val_acc: 0.8469
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0949 - orgCE: 0.6580 - myAcc: 0.4256 - acc: 0.8707 - val_loss: 4.5995 - val_orgCE: 0.9568 - val_myAcc: 0.2991 - val_acc: 0.8502
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1194 - orgCE: 0.6711 - myAcc: 0.4236 - acc: 0.8693 - val_loss: 4.6607 - val_orgCE: 0.9836 - val_myAcc: 0.2887 - val_acc: 0.8431
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.1131 - orgCE: 0.6637 - myAcc: 0.4232 - acc: 0.8691 - val_loss: 4.5450 - val_orgCE: 0.9748 - val_myAcc: 0.3072 - val_acc: 0.8485
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1232 - orgCE: 0.6774 - myAcc: 0.4237 - acc: 0.8668 - val_loss: 4.4627 - val_orgCE: 0.9164 - val_myAcc: 0.3087 - val_acc: 0.8500
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0189 - orgCE: 0.6319 - myAcc: 0.4369 - acc: 0.8747 - val_loss: 4.5278 - val_orgCE: 0.9503 - val_myAcc: 0.3120 - val_acc: 0.8522
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0153 - orgCE: 0.6336 - myAcc: 0.4353 - acc: 0.8755 - val_loss: 4.6189 - val_orgCE: 0.9638 - val_myAcc: 0.3056 - val_acc: 0.8504
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.0860 - orgCE: 0.6631 - myAcc: 0.4269 - acc: 0.8682 - val_loss: 4.4751 - val_orgCE: 0.9427 - val_myAcc: 0.2935 - val_acc: 0.8381
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0191 - orgCE: 0.6460 - myAcc: 0.4319 - acc: 0.8695 - val_loss: 4.5613 - val_orgCE: 0.9484 - val_myAcc: 0.3037 - val_acc: 0.8494
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0396 - orgCE: 0.6494 - myAcc: 0.4332 - acc: 0.8707 - val_loss: 4.4667 - val_orgCE: 0.9603 - val_myAcc: 0.3021 - val_acc: 0.8380
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0419 - orgCE: 0.6471 - myAcc: 0.4363 - acc: 0.8704 - val_loss: 4.5667 - val_orgCE: 0.9857 - val_myAcc: 0.2954 - val_acc: 0.8399
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0310 - orgCE: 0.6491 - myAcc: 0.4344 - acc: 0.8693 - val_loss: 4.6725 - val_orgCE: 1.0224 - val_myAcc: 0.2965 - val_acc: 0.8400
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9369 - orgCE: 0.6162 - myAcc: 0.4417 - acc: 0.8750 - val_loss: 4.5550 - val_orgCE: 0.9692 - val_myAcc: 0.3102 - val_acc: 0.8487
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0104 - orgCE: 0.6427 - myAcc: 0.4337 - acc: 0.8700 - val_loss: 4.6845 - val_orgCE: 1.0119 - val_myAcc: 0.2842 - val_acc: 0.8375
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0543 - orgCE: 0.6603 - myAcc: 0.4254 - acc: 0.8614 - val_loss: 4.7127 - val_orgCE: 1.0007 - val_myAcc: 0.2907 - val_acc: 0.8435
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9832 - orgCE: 0.6318 - myAcc: 0.4371 - acc: 0.8722 - val_loss: 4.6724 - val_orgCE: 1.0010 - val_myAcc: 0.2839 - val_acc: 0.8369
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0468 - orgCE: 0.6531 - myAcc: 0.4310 - acc: 0.8680 - val_loss: 4.4913 - val_orgCE: 0.9401 - val_myAcc: 0.3018 - val_acc: 0.8445
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0038 - orgCE: 0.6526 - myAcc: 0.4327 - acc: 0.8678 - val_loss: 4.7310 - val_orgCE: 1.0218 - val_myAcc: 0.2871 - val_acc: 0.8297
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9343 - orgCE: 0.6220 - myAcc: 0.4400 - acc: 0.8721 - val_loss: 4.5887 - val_orgCE: 0.9947 - val_myAcc: 0.2938 - val_acc: 0.8352
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0053 - orgCE: 0.6511 - myAcc: 0.4358 - acc: 0.8664 - val_loss: 4.6239 - val_orgCE: 0.9762 - val_myAcc: 0.3037 - val_acc: 0.8466
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9479 - orgCE: 0.6194 - myAcc: 0.4358 - acc: 0.8742 - val_loss: 4.7577 - val_orgCE: 1.0394 - val_myAcc: 0.2737 - val_acc: 0.8317
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.9952 - orgCE: 0.6359 - myAcc: 0.4387 - acc: 0.8674 - val_loss: 4.6388 - val_orgCE: 0.9785 - val_myAcc: 0.3054 - val_acc: 0.8495
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9935 - orgCE: 0.6468 - myAcc: 0.4340 - acc: 0.8680 - val_loss: 4.6172 - val_orgCE: 0.9811 - val_myAcc: 0.3009 - val_acc: 0.8437
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.9031 - orgCE: 0.6074 - myAcc: 0.4459 - acc: 0.8747 - val_loss: 4.5200 - val_orgCE: 0.9528 - val_myAcc: 0.2998 - val_acc: 0.8474
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9127 - orgCE: 0.6162 - myAcc: 0.4469 - acc: 0.8745 - val_loss: 4.6246 - val_orgCE: 1.0309 - val_myAcc: 0.2929 - val_acc: 0.8325
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8873 - orgCE: 0.6070 - myAcc: 0.4484 - acc: 0.8724 - val_loss: 4.7450 - val_orgCE: 1.0417 - val_myAcc: 0.2850 - val_acc: 0.8309

* Has loaded existed model. *

* Epoch 1/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.9800 - orgCE: 0.6344 - myAcc: 0.4322 - acc: 0.8692 - val_loss: 4.5640 - val_orgCE: 0.9495 - val_myAcc: 0.3061 - val_acc: 0.8446
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9202 - orgCE: 0.6227 - myAcc: 0.4433 - acc: 0.8705 - val_loss: 4.7756 - val_orgCE: 1.0192 - val_myAcc: 0.2851 - val_acc: 0.8357
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9064 - orgCE: 0.6202 - myAcc: 0.4424 - acc: 0.8689 - val_loss: 4.6694 - val_orgCE: 0.9774 - val_myAcc: 0.2974 - val_acc: 0.8474
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9368 - orgCE: 0.6352 - myAcc: 0.4388 - acc: 0.8709 - val_loss: 4.7022 - val_orgCE: 1.0166 - val_myAcc: 0.2955 - val_acc: 0.8428
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9368 - orgCE: 0.6322 - myAcc: 0.4411 - acc: 0.8704 - val_loss: 4.6093 - val_orgCE: 0.9608 - val_myAcc: 0.3002 - val_acc: 0.8415
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8715 - orgCE: 0.6141 - myAcc: 0.4494 - acc: 0.8710 - val_loss: 4.6301 - val_orgCE: 0.9765 - val_myAcc: 0.3087 - val_acc: 0.8452
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9073 - orgCE: 0.6255 - myAcc: 0.4460 - acc: 0.8647 - val_loss: 4.7008 - val_orgCE: 1.0117 - val_myAcc: 0.2983 - val_acc: 0.8411
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8290 - orgCE: 0.6029 - myAcc: 0.4568 - acc: 0.8717 - val_loss: 4.6163 - val_orgCE: 0.9853 - val_myAcc: 0.3143 - val_acc: 0.8480
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9030 - orgCE: 0.6277 - myAcc: 0.4475 - acc: 0.8543 - val_loss: 4.6886 - val_orgCE: 0.9942 - val_myAcc: 0.2868 - val_acc: 0.8337
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.8264 - orgCE: 0.6004 - myAcc: 0.4500 - acc: 0.8695 - val_loss: 4.6306 - val_orgCE: 0.9759 - val_myAcc: 0.3055 - val_acc: 0.8500
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7390 - orgCE: 0.5749 - myAcc: 0.4673 - acc: 0.8728 - val_loss: 4.8601 - val_orgCE: 1.0587 - val_myAcc: 0.2730 - val_acc: 0.8325
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8181 - orgCE: 0.6031 - myAcc: 0.4601 - acc: 0.8636 - val_loss: 4.7222 - val_orgCE: 1.0426 - val_myAcc: 0.2863 - val_acc: 0.7239
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8630 - orgCE: 0.6125 - myAcc: 0.4535 - acc: 0.8526 - val_loss: 4.7619 - val_orgCE: 1.0342 - val_myAcc: 0.3036 - val_acc: 0.8455
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8292 - orgCE: 0.5979 - myAcc: 0.4498 - acc: 0.8742 - val_loss: 4.6947 - val_orgCE: 1.0173 - val_myAcc: 0.2844 - val_acc: 0.8368
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7943 - orgCE: 0.5978 - myAcc: 0.4603 - acc: 0.8713 - val_loss: 4.8011 - val_orgCE: 1.0348 - val_myAcc: 0.2930 - val_acc: 0.8386
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7995 - orgCE: 0.5986 - myAcc: 0.4558 - acc: 0.8690 - val_loss: 4.7357 - val_orgCE: 0.9988 - val_myAcc: 0.3033 - val_acc: 0.8370
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8495 - orgCE: 0.6083 - myAcc: 0.4531 - acc: 0.8716 - val_loss: 4.8251 - val_orgCE: 1.0367 - val_myAcc: 0.2896 - val_acc: 0.8387
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8162 - orgCE: 0.6043 - myAcc: 0.4558 - acc: 0.8733 - val_loss: 4.6154 - val_orgCE: 0.9653 - val_myAcc: 0.3159 - val_acc: 0.8455
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8009 - orgCE: 0.5980 - myAcc: 0.4526 - acc: 0.8710 - val_loss: 4.8347 - val_orgCE: 1.0480 - val_myAcc: 0.2866 - val_acc: 0.8389
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7737 - orgCE: 0.5975 - myAcc: 0.4616 - acc: 0.8676 - val_loss: 4.8221 - val_orgCE: 1.0473 - val_myAcc: 0.2817 - val_acc: 0.8323
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7634 - orgCE: 0.5884 - myAcc: 0.4665 - acc: 0.8712 - val_loss: 4.5730 - val_orgCE: 0.9625 - val_myAcc: 0.2979 - val_acc: 0.8467
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8322 - orgCE: 0.6081 - myAcc: 0.4474 - acc: 0.8696 - val_loss: 4.7750 - val_orgCE: 1.0200 - val_myAcc: 0.3013 - val_acc: 0.8449
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.7652 - orgCE: 0.5840 - myAcc: 0.4605 - acc: 0.8580 - val_loss: 4.7335 - val_orgCE: 1.0079 - val_myAcc: 0.2970 - val_acc: 0.8441
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8087 - orgCE: 0.6020 - myAcc: 0.4480 - acc: 0.8669 - val_loss: 4.8688 - val_orgCE: 1.0432 - val_myAcc: 0.2845 - val_acc: 0.8415
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7988 - orgCE: 0.6061 - myAcc: 0.4602 - acc: 0.8554 - val_loss: 4.7284 - val_orgCE: 1.0242 - val_myAcc: 0.2960 - val_acc: 0.8405
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8379 - orgCE: 0.6074 - myAcc: 0.4567 - acc: 0.8690 - val_loss: 4.7374 - val_orgCE: 1.0045 - val_myAcc: 0.2957 - val_acc: 0.8464
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.7358 - orgCE: 0.5882 - myAcc: 0.4662 - acc: 0.8643 - val_loss: 4.8789 - val_orgCE: 1.0381 - val_myAcc: 0.2772 - val_acc: 0.8343
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7781 - orgCE: 0.5995 - myAcc: 0.4586 - acc: 0.8685 - val_loss: 4.7015 - val_orgCE: 1.0511 - val_myAcc: 0.2972 - val_acc: 0.8323
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7573 - orgCE: 0.5904 - myAcc: 0.4598 - acc: 0.8659 - val_loss: 4.6996 - val_orgCE: 1.0032 - val_myAcc: 0.3011 - val_acc: 0.8433
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7506 - orgCE: 0.5889 - myAcc: 0.4618 - acc: 0.8638 - val_loss: 4.6475 - val_orgCE: 0.9892 - val_myAcc: 0.3012 - val_acc: 0.8399
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7594 - orgCE: 0.5944 - myAcc: 0.4641 - acc: 0.8659 - val_loss: 4.6696 - val_orgCE: 0.9976 - val_myAcc: 0.3107 - val_acc: 0.8439
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7263 - orgCE: 0.5839 - myAcc: 0.4641 - acc: 0.8645 - val_loss: 4.7758 - val_orgCE: 1.0598 - val_myAcc: 0.2856 - val_acc: 0.8309
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6963 - orgCE: 0.5798 - myAcc: 0.4678 - acc: 0.8651 - val_loss: 4.8356 - val_orgCE: 1.0226 - val_myAcc: 0.3003 - val_acc: 0.8454
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7637 - orgCE: 0.5966 - myAcc: 0.4654 - acc: 0.8627 - val_loss: 4.5677 - val_orgCE: 0.9483 - val_myAcc: 0.3204 - val_acc: 0.8538
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7181 - orgCE: 0.5817 - myAcc: 0.4660 - acc: 0.8640 - val_loss: 4.8457 - val_orgCE: 1.0451 - val_myAcc: 0.2810 - val_acc: 0.8315
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7286 - orgCE: 0.5793 - myAcc: 0.4702 - acc: 0.8599 - val_loss: 4.7735 - val_orgCE: 1.0294 - val_myAcc: 0.2895 - val_acc: 0.8415
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6887 - orgCE: 0.5749 - myAcc: 0.4718 - acc: 0.8665 - val_loss: 4.5961 - val_orgCE: 0.9599 - val_myAcc: 0.3126 - val_acc: 0.8532
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6352 - orgCE: 0.5578 - myAcc: 0.4791 - acc: 0.8681 - val_loss: 4.6241 - val_orgCE: 0.9675 - val_myAcc: 0.3141 - val_acc: 0.8477
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6624 - orgCE: 0.5554 - myAcc: 0.4734 - acc: 0.8771 - val_loss: 4.7849 - val_orgCE: 1.0209 - val_myAcc: 0.3059 - val_acc: 0.8475
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6197 - orgCE: 0.5529 - myAcc: 0.4742 - acc: 0.8708 - val_loss: 4.8920 - val_orgCE: 1.0600 - val_myAcc: 0.2923 - val_acc: 0.8389
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.7074 - orgCE: 0.5808 - myAcc: 0.4713 - acc: 0.8593 - val_loss: 4.6639 - val_orgCE: 0.9704 - val_myAcc: 0.3114 - val_acc: 0.8331
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.7315 - orgCE: 0.5949 - myAcc: 0.4636 - acc: 0.8517 - val_loss: 4.7392 - val_orgCE: 0.9875 - val_myAcc: 0.2954 - val_acc: 0.8402
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6780 - orgCE: 0.5642 - myAcc: 0.4750 - acc: 0.8593 - val_loss: 4.5388 - val_orgCE: 0.9823 - val_myAcc: 0.3183 - val_acc: 0.8482
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6737 - orgCE: 0.5705 - myAcc: 0.4719 - acc: 0.8743 - val_loss: 4.9676 - val_orgCE: 1.1069 - val_myAcc: 0.2662 - val_acc: 0.8285
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.7009 - orgCE: 0.5763 - myAcc: 0.4691 - acc: 0.8690 - val_loss: 4.6956 - val_orgCE: 1.0063 - val_myAcc: 0.3019 - val_acc: 0.8415
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6098 - orgCE: 0.5452 - myAcc: 0.4833 - acc: 0.8758 - val_loss: 4.7803 - val_orgCE: 1.0136 - val_myAcc: 0.2959 - val_acc: 0.8465
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6710 - orgCE: 0.5704 - myAcc: 0.4743 - acc: 0.8732 - val_loss: 4.8365 - val_orgCE: 1.0311 - val_myAcc: 0.2883 - val_acc: 0.8136
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6424 - orgCE: 0.5591 - myAcc: 0.4784 - acc: 0.8716 - val_loss: 4.9037 - val_orgCE: 1.0583 - val_myAcc: 0.2825 - val_acc: 0.8388
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6374 - orgCE: 0.5601 - myAcc: 0.4724 - acc: 0.8728 - val_loss: 4.8654 - val_orgCE: 1.0243 - val_myAcc: 0.2884 - val_acc: 0.8362
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6159 - orgCE: 0.5539 - myAcc: 0.4815 - acc: 0.8644 - val_loss: 4.7265 - val_orgCE: 0.9930 - val_myAcc: 0.3011 - val_acc: 0.8322
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6729 - orgCE: 0.5683 - myAcc: 0.4778 - acc: 0.8698 - val_loss: 4.6612 - val_orgCE: 0.9785 - val_myAcc: 0.3149 - val_acc: 0.8509
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6490 - orgCE: 0.5629 - myAcc: 0.4745 - acc: 0.8693 - val_loss: 4.8513 - val_orgCE: 1.0373 - val_myAcc: 0.2947 - val_acc: 0.8421
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.5979 - orgCE: 0.5417 - myAcc: 0.4829 - acc: 0.8816 - val_loss: 4.8500 - val_orgCE: 1.0433 - val_myAcc: 0.2907 - val_acc: 0.8420
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6761 - orgCE: 0.5752 - myAcc: 0.4722 - acc: 0.8573 - val_loss: 4.8041 - val_orgCE: 1.0157 - val_myAcc: 0.2951 - val_acc: 0.8434
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6016 - orgCE: 0.5575 - myAcc: 0.4861 - acc: 0.8711 - val_loss: 5.0398 - val_orgCE: 1.0742 - val_myAcc: 0.2767 - val_acc: 0.8180
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.6040 - orgCE: 0.5548 - myAcc: 0.4834 - acc: 0.8670 - val_loss: 4.8192 - val_orgCE: 1.0539 - val_myAcc: 0.2827 - val_acc: 0.8302
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.5923 - orgCE: 0.5526 - myAcc: 0.4848 - acc: 0.8648 - val_loss: 4.8379 - val_orgCE: 1.0458 - val_myAcc: 0.2990 - val_acc: 0.8431
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6379 - orgCE: 0.5707 - myAcc: 0.4743 - acc: 0.8646 - val_loss: 4.9365 - val_orgCE: 1.0838 - val_myAcc: 0.2842 - val_acc: 0.8329
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5859 - orgCE: 0.5453 - myAcc: 0.4872 - acc: 0.8796 - val_loss: 4.8701 - val_orgCE: 1.0444 - val_myAcc: 0.2948 - val_acc: 0.8432
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6416 - orgCE: 0.5683 - myAcc: 0.4777 - acc: 0.8714 - val_loss: 4.7253 - val_orgCE: 0.9940 - val_myAcc: 0.3060 - val_acc: 0.8387
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5807 - orgCE: 0.5437 - myAcc: 0.4892 - acc: 0.8775 - val_loss: 4.8302 - val_orgCE: 1.0526 - val_myAcc: 0.2984 - val_acc: 0.8340
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6070 - orgCE: 0.5576 - myAcc: 0.4827 - acc: 0.8628 - val_loss: 4.7567 - val_orgCE: 1.0063 - val_myAcc: 0.3052 - val_acc: 0.8468
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5183 - orgCE: 0.5256 - myAcc: 0.4963 - acc: 0.8677 - val_loss: 4.9620 - val_orgCE: 1.0624 - val_myAcc: 0.2900 - val_acc: 0.8337
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5496 - orgCE: 0.5439 - myAcc: 0.4848 - acc: 0.8685 - val_loss: 4.7096 - val_orgCE: 1.0107 - val_myAcc: 0.2995 - val_acc: 0.8407
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4751 - orgCE: 0.5155 - myAcc: 0.4973 - acc: 0.8825 - val_loss: 4.9268 - val_orgCE: 1.0482 - val_myAcc: 0.2843 - val_acc: 0.8412
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5992 - orgCE: 0.5590 - myAcc: 0.4815 - acc: 0.8657 - val_loss: 4.9041 - val_orgCE: 1.0291 - val_myAcc: 0.2879 - val_acc: 0.8337
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5534 - orgCE: 0.5376 - myAcc: 0.4909 - acc: 0.8768 - val_loss: 4.8247 - val_orgCE: 1.0374 - val_myAcc: 0.2983 - val_acc: 0.8447
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.5756 - orgCE: 0.5474 - myAcc: 0.4915 - acc: 0.8696 - val_loss: 4.8511 - val_orgCE: 1.0439 - val_myAcc: 0.2916 - val_acc: 0.8424
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.5357 - orgCE: 0.5359 - myAcc: 0.4930 - acc: 0.8768 - val_loss: 4.9054 - val_orgCE: 1.0380 - val_myAcc: 0.2968 - val_acc: 0.8345
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5882 - orgCE: 0.5571 - myAcc: 0.4870 - acc: 0.8632 - val_loss: 4.6969 - val_orgCE: 0.9794 - val_myAcc: 0.3142 - val_acc: 0.8341
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.6007 - orgCE: 0.5560 - myAcc: 0.4779 - acc: 0.8573 - val_loss: 4.8820 - val_orgCE: 1.0787 - val_myAcc: 0.3006 - val_acc: 0.8409
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5017 - orgCE: 0.5243 - myAcc: 0.4915 - acc: 0.8688 - val_loss: 4.7663 - val_orgCE: 0.9894 - val_myAcc: 0.2964 - val_acc: 0.8409
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5772 - orgCE: 0.5498 - myAcc: 0.4888 - acc: 0.8717 - val_loss: 4.8154 - val_orgCE: 1.0554 - val_myAcc: 0.2899 - val_acc: 0.8368
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5115 - orgCE: 0.5253 - myAcc: 0.4966 - acc: 0.8744 - val_loss: 4.9171 - val_orgCE: 1.0819 - val_myAcc: 0.2903 - val_acc: 0.8394
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5826 - orgCE: 0.5584 - myAcc: 0.4825 - acc: 0.8652 - val_loss: 4.9118 - val_orgCE: 1.0556 - val_myAcc: 0.2910 - val_acc: 0.8301
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5983 - orgCE: 0.5601 - myAcc: 0.4805 - acc: 0.8649 - val_loss: 4.8051 - val_orgCE: 1.0351 - val_myAcc: 0.2905 - val_acc: 0.8390
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5080 - orgCE: 0.5250 - myAcc: 0.4976 - acc: 0.8758 - val_loss: 4.9736 - val_orgCE: 1.0629 - val_myAcc: 0.2856 - val_acc: 0.8349
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5213 - orgCE: 0.5355 - myAcc: 0.4954 - acc: 0.8745 - val_loss: 4.8834 - val_orgCE: 1.0694 - val_myAcc: 0.2915 - val_acc: 0.8196
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5371 - orgCE: 0.5475 - myAcc: 0.4900 - acc: 0.8556 - val_loss: 4.9081 - val_orgCE: 1.0782 - val_myAcc: 0.2928 - val_acc: 0.8405
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5725 - orgCE: 0.5519 - myAcc: 0.4857 - acc: 0.8515 - val_loss: 5.0146 - val_orgCE: 1.0698 - val_myAcc: 0.2774 - val_acc: 0.7614
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5204 - orgCE: 0.5366 - myAcc: 0.5000 - acc: 0.8557 - val_loss: 4.9507 - val_orgCE: 1.0543 - val_myAcc: 0.2763 - val_acc: 0.8290
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5014 - orgCE: 0.5328 - myAcc: 0.4977 - acc: 0.8443 - val_loss: 4.9207 - val_orgCE: 1.0773 - val_myAcc: 0.2797 - val_acc: 0.8259
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5419 - orgCE: 0.5471 - myAcc: 0.4920 - acc: 0.8586 - val_loss: 4.8904 - val_orgCE: 1.0506 - val_myAcc: 0.3000 - val_acc: 0.7966
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5431 - orgCE: 0.5517 - myAcc: 0.4950 - acc: 0.8540 - val_loss: 4.9614 - val_orgCE: 1.0793 - val_myAcc: 0.2827 - val_acc: 0.8166
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5178 - orgCE: 0.5328 - myAcc: 0.5040 - acc: 0.8564 - val_loss: 4.9251 - val_orgCE: 1.0770 - val_myAcc: 0.2891 - val_acc: 0.8355
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.5370 - orgCE: 0.5419 - myAcc: 0.4955 - acc: 0.8610 - val_loss: 4.8264 - val_orgCE: 1.0244 - val_myAcc: 0.2950 - val_acc: 0.8100
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4653 - orgCE: 0.5210 - myAcc: 0.4972 - acc: 0.8499 - val_loss: 4.8962 - val_orgCE: 1.0325 - val_myAcc: 0.2872 - val_acc: 0.8283
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5074 - orgCE: 0.5373 - myAcc: 0.5041 - acc: 0.8531 - val_loss: 4.8968 - val_orgCE: 1.0714 - val_myAcc: 0.2937 - val_acc: 0.8341
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4588 - orgCE: 0.5239 - myAcc: 0.5018 - acc: 0.8609 - val_loss: 4.9568 - val_orgCE: 1.0560 - val_myAcc: 0.2936 - val_acc: 0.8302
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4179 - orgCE: 0.5078 - myAcc: 0.5098 - acc: 0.8696 - val_loss: 4.9830 - val_orgCE: 1.0953 - val_myAcc: 0.2782 - val_acc: 0.8212
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4818 - orgCE: 0.5261 - myAcc: 0.4985 - acc: 0.8466 - val_loss: 4.8745 - val_orgCE: 1.0498 - val_myAcc: 0.2895 - val_acc: 0.8349
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4628 - orgCE: 0.5211 - myAcc: 0.5010 - acc: 0.8555 - val_loss: 4.7897 - val_orgCE: 1.0324 - val_myAcc: 0.3107 - val_acc: 0.8458
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4992 - orgCE: 0.5346 - myAcc: 0.4958 - acc: 0.8574 - val_loss: 4.7994 - val_orgCE: 1.0253 - val_myAcc: 0.2953 - val_acc: 0.8421
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4225 - orgCE: 0.5154 - myAcc: 0.5061 - acc: 0.8525 - val_loss: 4.8435 - val_orgCE: 1.0382 - val_myAcc: 0.3005 - val_acc: 0.7967
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4628 - orgCE: 0.5215 - myAcc: 0.4994 - acc: 0.8508 - val_loss: 4.8317 - val_orgCE: 1.0197 - val_myAcc: 0.3043 - val_acc: 0.8480
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4666 - orgCE: 0.5244 - myAcc: 0.4980 - acc: 0.8546 - val_loss: 4.7271 - val_orgCE: 0.9475 - val_myAcc: 0.3122 - val_acc: 0.8519
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4880 - orgCE: 0.5327 - myAcc: 0.4991 - acc: 0.8564 - val_loss: 4.9090 - val_orgCE: 1.0417 - val_myAcc: 0.2914 - val_acc: 0.7976
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4786 - orgCE: 0.5359 - myAcc: 0.4989 - acc: 0.8558 - val_loss: 4.9016 - val_orgCE: 1.0518 - val_myAcc: 0.3016 - val_acc: 0.8204
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4595 - orgCE: 0.5281 - myAcc: 0.5020 - acc: 0.8533 - val_loss: 4.9538 - val_orgCE: 1.0659 - val_myAcc: 0.2918 - val_acc: 0.8320
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4701 - orgCE: 0.5319 - myAcc: 0.5018 - acc: 0.8594 - val_loss: 4.9957 - val_orgCE: 1.0896 - val_myAcc: 0.2829 - val_acc: 0.8177


# python3 bleu_eval.py sample_output_testset.txt
Originally, average bleu score is 0.2964199571828562
By another method, average bleu score is 0.6609003278440447
