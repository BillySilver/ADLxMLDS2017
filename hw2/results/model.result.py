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


# python3 bleu_eval.py sample_output_testset.txt
Originally, average bleu score is 0.2956214662604089
By another method, average bleu score is 0.6594552700638191
