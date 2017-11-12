_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
Encoder_in (InputLayer)      (None, 80, 4096)          0         
_________________________________________________________________
zero_padding1d_1 (ZeroPaddin (None, 121, 4096)         0         
_________________________________________________________________
Encoder_out (LSTM)           (None, 121, 1024)         20975616  
_________________________________________________________________
recurrent_wrapper_1 (Recurre (None, 121, 6132)         13614068  
_________________________________________________________________
cropping1d_1 (Cropping1D)    (None, 41, 6132)          0         
=================================================================
Total params: 34,589,684
Trainable params: 34,589,684
Non-trainable params: 0
_________________________________________________________________

* Create a new model. *

* Epoch 1/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 43s - loss: 6.0097 - orgCE: 1.2920 - myAcc: 0.1480 - acc: 0.5433 - val_loss: 5.1953 - val_orgCE: 1.1099 - val_myAcc: 0.2060 - val_acc: 0.8302
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 4.9491 - orgCE: 1.0380 - myAcc: 0.2525 - acc: 0.8429 - val_loss: 4.7573 - val_orgCE: 1.0061 - val_myAcc: 0.3103 - val_acc: 0.8537
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 4.6723 - orgCE: 1.0033 - myAcc: 0.2965 - acc: 0.8481 - val_loss: 4.7554 - val_orgCE: 1.0410 - val_myAcc: 0.2948 - val_acc: 0.8453
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 4.6586 - orgCE: 1.0132 - myAcc: 0.2937 - acc: 0.8460 - val_loss: 4.5740 - val_orgCE: 0.9243 - val_myAcc: 0.3076 - val_acc: 0.8586
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 4.5762 - orgCE: 0.9824 - myAcc: 0.2931 - acc: 0.8474 - val_loss: 4.6130 - val_orgCE: 0.9886 - val_myAcc: 0.2982 - val_acc: 0.8458
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 4.4376 - orgCE: 0.9426 - myAcc: 0.3053 - acc: 0.8516 - val_loss: 4.5196 - val_orgCE: 0.9562 - val_myAcc: 0.3011 - val_acc: 0.8517
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 4.3912 - orgCE: 0.9297 - myAcc: 0.3002 - acc: 0.8516 - val_loss: 4.3867 - val_orgCE: 0.9316 - val_myAcc: 0.3205 - val_acc: 0.8556
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 4.3003 - orgCE: 0.9063 - myAcc: 0.3031 - acc: 0.8521 - val_loss: 4.5133 - val_orgCE: 0.9582 - val_myAcc: 0.3085 - val_acc: 0.8532
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 4.2015 - orgCE: 0.8743 - myAcc: 0.3102 - acc: 0.8562 - val_loss: 4.3347 - val_orgCE: 0.9156 - val_myAcc: 0.3146 - val_acc: 0.8548
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 4.2375 - orgCE: 0.9000 - myAcc: 0.2996 - acc: 0.8507 - val_loss: 4.3504 - val_orgCE: 0.8993 - val_myAcc: 0.3225 - val_acc: 0.8588
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 43s - loss: 4.1997 - orgCE: 0.8878 - myAcc: 0.3152 - acc: 0.8546 - val_loss: 4.4397 - val_orgCE: 0.9994 - val_myAcc: 0.2972 - val_acc: 0.8418
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 4.1592 - orgCE: 0.8975 - myAcc: 0.3096 - acc: 0.8501 - val_loss: 4.2926 - val_orgCE: 0.9031 - val_myAcc: 0.3309 - val_acc: 0.8592
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 4.1075 - orgCE: 0.8749 - myAcc: 0.3131 - acc: 0.8530 - val_loss: 4.3715 - val_orgCE: 0.9455 - val_myAcc: 0.3211 - val_acc: 0.8531
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 4.1115 - orgCE: 0.8809 - myAcc: 0.3069 - acc: 0.8509 - val_loss: 4.3364 - val_orgCE: 0.9414 - val_myAcc: 0.3160 - val_acc: 0.8503
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 4.0728 - orgCE: 0.8666 - myAcc: 0.3064 - acc: 0.8512 - val_loss: 4.3363 - val_orgCE: 0.9541 - val_myAcc: 0.3211 - val_acc: 0.8505
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 4.0724 - orgCE: 0.9012 - myAcc: 0.3057 - acc: 0.8455 - val_loss: 4.3812 - val_orgCE: 0.9414 - val_myAcc: 0.2996 - val_acc: 0.8479
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.9280 - orgCE: 0.8319 - myAcc: 0.3213 - acc: 0.8557 - val_loss: 4.2692 - val_orgCE: 0.9005 - val_myAcc: 0.3236 - val_acc: 0.8559
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 3.9100 - orgCE: 0.8263 - myAcc: 0.3217 - acc: 0.8558 - val_loss: 4.2176 - val_orgCE: 0.9038 - val_myAcc: 0.3214 - val_acc: 0.8534
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 3.8545 - orgCE: 0.8119 - myAcc: 0.3207 - acc: 0.8561 - val_loss: 4.2046 - val_orgCE: 0.8947 - val_myAcc: 0.3217 - val_acc: 0.8543
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.9095 - orgCE: 0.8363 - myAcc: 0.3201 - acc: 0.8535 - val_loss: 4.3444 - val_orgCE: 0.9437 - val_myAcc: 0.3148 - val_acc: 0.8503
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.8195 - orgCE: 0.8056 - myAcc: 0.3209 - acc: 0.8558 - val_loss: 4.2252 - val_orgCE: 0.8955 - val_myAcc: 0.3227 - val_acc: 0.8549
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 3.7963 - orgCE: 0.8135 - myAcc: 0.3246 - acc: 0.8542 - val_loss: 4.3032 - val_orgCE: 0.9370 - val_myAcc: 0.3154 - val_acc: 0.8500
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.8484 - orgCE: 0.8259 - myAcc: 0.3182 - acc: 0.8525 - val_loss: 4.1184 - val_orgCE: 0.8438 - val_myAcc: 0.3275 - val_acc: 0.8618
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 3.8108 - orgCE: 0.8166 - myAcc: 0.3125 - acc: 0.8518 - val_loss: 4.2066 - val_orgCE: 0.8854 - val_myAcc: 0.3135 - val_acc: 0.8554
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.7427 - orgCE: 0.7978 - myAcc: 0.3232 - acc: 0.8550 - val_loss: 4.3152 - val_orgCE: 0.9156 - val_myAcc: 0.3167 - val_acc: 0.8521
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.6765 - orgCE: 0.7767 - myAcc: 0.3265 - acc: 0.8555 - val_loss: 4.1967 - val_orgCE: 0.8747 - val_myAcc: 0.3260 - val_acc: 0.8592
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 3.6491 - orgCE: 0.7810 - myAcc: 0.3303 - acc: 0.8548 - val_loss: 4.3106 - val_orgCE: 0.9407 - val_myAcc: 0.3287 - val_acc: 0.8532
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.6200 - orgCE: 0.7763 - myAcc: 0.3253 - acc: 0.8530 - val_loss: 4.3462 - val_orgCE: 0.9584 - val_myAcc: 0.3082 - val_acc: 0.8456
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 3.6454 - orgCE: 0.7682 - myAcc: 0.3316 - acc: 0.8581 - val_loss: 4.1731 - val_orgCE: 0.8593 - val_myAcc: 0.3216 - val_acc: 0.8584
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 3.6009 - orgCE: 0.7727 - myAcc: 0.3293 - acc: 0.8538 - val_loss: 4.4034 - val_orgCE: 0.9703 - val_myAcc: 0.2901 - val_acc: 0.8420
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.5629 - orgCE: 0.7571 - myAcc: 0.3279 - acc: 0.8558 - val_loss: 4.2860 - val_orgCE: 0.9226 - val_myAcc: 0.3287 - val_acc: 0.8541
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 3.5938 - orgCE: 0.7653 - myAcc: 0.3294 - acc: 0.8558 - val_loss: 4.1521 - val_orgCE: 0.8843 - val_myAcc: 0.3398 - val_acc: 0.8584
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.4215 - orgCE: 0.7064 - myAcc: 0.3499 - acc: 0.8644 - val_loss: 4.1982 - val_orgCE: 0.8947 - val_myAcc: 0.3208 - val_acc: 0.8534
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.4791 - orgCE: 0.7386 - myAcc: 0.3404 - acc: 0.8587 - val_loss: 4.2976 - val_orgCE: 0.9232 - val_myAcc: 0.3274 - val_acc: 0.8548
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 3.4554 - orgCE: 0.7279 - myAcc: 0.3450 - acc: 0.8611 - val_loss: 4.2750 - val_orgCE: 0.9141 - val_myAcc: 0.3205 - val_acc: 0.8542
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 3.5008 - orgCE: 0.7461 - myAcc: 0.3356 - acc: 0.8561 - val_loss: 4.3212 - val_orgCE: 0.9291 - val_myAcc: 0.3124 - val_acc: 0.8505
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.4159 - orgCE: 0.7356 - myAcc: 0.3417 - acc: 0.8556 - val_loss: 4.2972 - val_orgCE: 0.9190 - val_myAcc: 0.3248 - val_acc: 0.8544
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 3.3992 - orgCE: 0.7280 - myAcc: 0.3428 - acc: 0.8579 - val_loss: 4.3375 - val_orgCE: 0.9356 - val_myAcc: 0.2993 - val_acc: 0.8480
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.3411 - orgCE: 0.7139 - myAcc: 0.3466 - acc: 0.8580 - val_loss: 4.2933 - val_orgCE: 0.9180 - val_myAcc: 0.3135 - val_acc: 0.8500
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.3219 - orgCE: 0.7074 - myAcc: 0.3524 - acc: 0.8601 - val_loss: 4.2415 - val_orgCE: 0.9089 - val_myAcc: 0.3195 - val_acc: 0.8521
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.3472 - orgCE: 0.7222 - myAcc: 0.3437 - acc: 0.8557 - val_loss: 4.3391 - val_orgCE: 0.9343 - val_myAcc: 0.3093 - val_acc: 0.8494
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 3.3063 - orgCE: 0.7026 - myAcc: 0.3499 - acc: 0.8601 - val_loss: 4.3234 - val_orgCE: 0.9223 - val_myAcc: 0.3217 - val_acc: 0.8546
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.2653 - orgCE: 0.6944 - myAcc: 0.3481 - acc: 0.8580 - val_loss: 4.2872 - val_orgCE: 0.9183 - val_myAcc: 0.3143 - val_acc: 0.8519
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 3.2131 - orgCE: 0.6877 - myAcc: 0.3548 - acc: 0.8585 - val_loss: 4.3234 - val_orgCE: 0.9253 - val_myAcc: 0.3280 - val_acc: 0.8542
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.1841 - orgCE: 0.6745 - myAcc: 0.3623 - acc: 0.8615 - val_loss: 4.3764 - val_orgCE: 0.9335 - val_myAcc: 0.3090 - val_acc: 0.8496
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.1833 - orgCE: 0.6785 - myAcc: 0.3575 - acc: 0.8601 - val_loss: 4.3056 - val_orgCE: 0.9005 - val_myAcc: 0.3187 - val_acc: 0.8528
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 3.1563 - orgCE: 0.6803 - myAcc: 0.3693 - acc: 0.8601 - val_loss: 4.3985 - val_orgCE: 0.9316 - val_myAcc: 0.3154 - val_acc: 0.8517
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.0835 - orgCE: 0.6551 - myAcc: 0.3599 - acc: 0.8599 - val_loss: 4.4940 - val_orgCE: 0.9748 - val_myAcc: 0.3090 - val_acc: 0.8475
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.1445 - orgCE: 0.6756 - myAcc: 0.3620 - acc: 0.8552 - val_loss: 4.3071 - val_orgCE: 0.9268 - val_myAcc: 0.3096 - val_acc: 0.8484
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.0755 - orgCE: 0.6581 - myAcc: 0.3722 - acc: 0.8618 - val_loss: 4.2757 - val_orgCE: 0.8984 - val_myAcc: 0.3329 - val_acc: 0.8552
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.0790 - orgCE: 0.6463 - myAcc: 0.3668 - acc: 0.8621 - val_loss: 4.3140 - val_orgCE: 0.9155 - val_myAcc: 0.3241 - val_acc: 0.8558
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.0702 - orgCE: 0.6556 - myAcc: 0.3691 - acc: 0.8513 - val_loss: 4.3105 - val_orgCE: 0.9014 - val_myAcc: 0.3146 - val_acc: 0.8522
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.0304 - orgCE: 0.6480 - myAcc: 0.3704 - acc: 0.8599 - val_loss: 4.4387 - val_orgCE: 0.9497 - val_myAcc: 0.3210 - val_acc: 0.8531
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.1145 - orgCE: 0.6744 - myAcc: 0.3557 - acc: 0.8546 - val_loss: 4.3374 - val_orgCE: 0.9235 - val_myAcc: 0.3117 - val_acc: 0.8502
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.9961 - orgCE: 0.6295 - myAcc: 0.3767 - acc: 0.8642 - val_loss: 4.4124 - val_orgCE: 0.9534 - val_myAcc: 0.3084 - val_acc: 0.8484
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.9910 - orgCE: 0.6456 - myAcc: 0.3672 - acc: 0.8598 - val_loss: 4.3787 - val_orgCE: 0.9666 - val_myAcc: 0.3112 - val_acc: 0.8442
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.9810 - orgCE: 0.6344 - myAcc: 0.3751 - acc: 0.8618 - val_loss: 4.3307 - val_orgCE: 0.9309 - val_myAcc: 0.3229 - val_acc: 0.8500
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 3.0070 - orgCE: 0.6456 - myAcc: 0.3644 - acc: 0.8595 - val_loss: 4.3095 - val_orgCE: 0.9039 - val_myAcc: 0.3165 - val_acc: 0.8523
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.9223 - orgCE: 0.6155 - myAcc: 0.3729 - acc: 0.8640 - val_loss: 4.3682 - val_orgCE: 0.9193 - val_myAcc: 0.3246 - val_acc: 0.8539
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 2.9381 - orgCE: 0.6240 - myAcc: 0.3714 - acc: 0.8587 - val_loss: 4.3991 - val_orgCE: 0.9461 - val_myAcc: 0.3140 - val_acc: 0.8492
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.8659 - orgCE: 0.6052 - myAcc: 0.3824 - acc: 0.8619 - val_loss: 4.2674 - val_orgCE: 0.9051 - val_myAcc: 0.3242 - val_acc: 0.8542
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.9172 - orgCE: 0.6166 - myAcc: 0.3806 - acc: 0.8623 - val_loss: 4.4995 - val_orgCE: 0.9828 - val_myAcc: 0.3017 - val_acc: 0.8452
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.9176 - orgCE: 0.6178 - myAcc: 0.3791 - acc: 0.8599 - val_loss: 4.3236 - val_orgCE: 0.9178 - val_myAcc: 0.3308 - val_acc: 0.8537
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.9058 - orgCE: 0.6264 - myAcc: 0.3813 - acc: 0.8596 - val_loss: 4.3570 - val_orgCE: 0.9305 - val_myAcc: 0.3091 - val_acc: 0.8496
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.8613 - orgCE: 0.6036 - myAcc: 0.3784 - acc: 0.8596 - val_loss: 4.5125 - val_orgCE: 0.9666 - val_myAcc: 0.3056 - val_acc: 0.8468
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.8058 - orgCE: 0.5939 - myAcc: 0.4035 - acc: 0.8660 - val_loss: 4.4533 - val_orgCE: 0.9305 - val_myAcc: 0.3073 - val_acc: 0.8495
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 2.8394 - orgCE: 0.6054 - myAcc: 0.3852 - acc: 0.8571 - val_loss: 4.4685 - val_orgCE: 0.9379 - val_myAcc: 0.3194 - val_acc: 0.8540
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.8420 - orgCE: 0.6026 - myAcc: 0.3869 - acc: 0.8591 - val_loss: 4.4372 - val_orgCE: 0.9618 - val_myAcc: 0.3006 - val_acc: 0.8403
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.8035 - orgCE: 0.5973 - myAcc: 0.3930 - acc: 0.8584 - val_loss: 4.4080 - val_orgCE: 0.9359 - val_myAcc: 0.3120 - val_acc: 0.8512
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.7959 - orgCE: 0.5886 - myAcc: 0.3861 - acc: 0.8602 - val_loss: 4.5163 - val_orgCE: 0.9894 - val_myAcc: 0.3108 - val_acc: 0.8421
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.8874 - orgCE: 0.6357 - myAcc: 0.3698 - acc: 0.8487 - val_loss: 4.4540 - val_orgCE: 0.9561 - val_myAcc: 0.3149 - val_acc: 0.8497
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 2.7687 - orgCE: 0.5908 - myAcc: 0.3854 - acc: 0.8585 - val_loss: 4.5030 - val_orgCE: 0.9649 - val_myAcc: 0.3062 - val_acc: 0.8489
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.7828 - orgCE: 0.6036 - myAcc: 0.3896 - acc: 0.8574 - val_loss: 4.4155 - val_orgCE: 0.9351 - val_myAcc: 0.3260 - val_acc: 0.8544
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.7285 - orgCE: 0.5756 - myAcc: 0.3943 - acc: 0.8605 - val_loss: 4.4970 - val_orgCE: 0.9688 - val_myAcc: 0.3031 - val_acc: 0.8358
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.8463 - orgCE: 0.6131 - myAcc: 0.3760 - acc: 0.8513 - val_loss: 4.4841 - val_orgCE: 0.9460 - val_myAcc: 0.3097 - val_acc: 0.8425
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.7482 - orgCE: 0.5891 - myAcc: 0.3859 - acc: 0.8554 - val_loss: 4.4067 - val_orgCE: 0.9112 - val_myAcc: 0.3234 - val_acc: 0.8553
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.6784 - orgCE: 0.5618 - myAcc: 0.3978 - acc: 0.8641 - val_loss: 4.3781 - val_orgCE: 0.9108 - val_myAcc: 0.3164 - val_acc: 0.8539
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.6986 - orgCE: 0.5742 - myAcc: 0.3887 - acc: 0.8609 - val_loss: 4.5178 - val_orgCE: 0.9765 - val_myAcc: 0.3141 - val_acc: 0.8452
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.7073 - orgCE: 0.5829 - myAcc: 0.3981 - acc: 0.8555 - val_loss: 4.3460 - val_orgCE: 0.9162 - val_myAcc: 0.3260 - val_acc: 0.8551
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 2.6750 - orgCE: 0.5656 - myAcc: 0.3998 - acc: 0.8598 - val_loss: 4.4516 - val_orgCE: 0.9383 - val_myAcc: 0.3094 - val_acc: 0.8497
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.7028 - orgCE: 0.5793 - myAcc: 0.3909 - acc: 0.8574 - val_loss: 4.5112 - val_orgCE: 0.9800 - val_myAcc: 0.3117 - val_acc: 0.8447
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.6610 - orgCE: 0.5614 - myAcc: 0.3937 - acc: 0.8575 - val_loss: 4.5445 - val_orgCE: 0.9788 - val_myAcc: 0.3217 - val_acc: 0.8437
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.6351 - orgCE: 0.5553 - myAcc: 0.3996 - acc: 0.8562 - val_loss: 4.3310 - val_orgCE: 0.9019 - val_myAcc: 0.3302 - val_acc: 0.8483
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.6242 - orgCE: 0.5565 - myAcc: 0.4026 - acc: 0.8506 - val_loss: 4.6855 - val_orgCE: 1.0111 - val_myAcc: 0.3005 - val_acc: 0.8446
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 42s - loss: 2.6472 - orgCE: 0.5660 - myAcc: 0.4005 - acc: 0.8595 - val_loss: 4.5123 - val_orgCE: 0.9894 - val_myAcc: 0.3087 - val_acc: 0.8433
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.6277 - orgCE: 0.5672 - myAcc: 0.4004 - acc: 0.8583 - val_loss: 4.4724 - val_orgCE: 0.9549 - val_myAcc: 0.3093 - val_acc: 0.8466
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.6103 - orgCE: 0.5538 - myAcc: 0.4015 - acc: 0.8595 - val_loss: 4.3629 - val_orgCE: 0.9173 - val_myAcc: 0.3361 - val_acc: 0.8556
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.6029 - orgCE: 0.5479 - myAcc: 0.3996 - acc: 0.8602 - val_loss: 4.5013 - val_orgCE: 0.9664 - val_myAcc: 0.3171 - val_acc: 0.8476
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.6713 - orgCE: 0.5697 - myAcc: 0.3924 - acc: 0.8544 - val_loss: 4.5198 - val_orgCE: 0.9666 - val_myAcc: 0.3108 - val_acc: 0.8489
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.6403 - orgCE: 0.5656 - myAcc: 0.3890 - acc: 0.8553 - val_loss: 4.3501 - val_orgCE: 0.9092 - val_myAcc: 0.3192 - val_acc: 0.8493
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.6563 - orgCE: 0.5672 - myAcc: 0.3933 - acc: 0.8513 - val_loss: 4.4820 - val_orgCE: 0.9524 - val_myAcc: 0.3130 - val_acc: 0.8474
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.6229 - orgCE: 0.5688 - myAcc: 0.3967 - acc: 0.8455 - val_loss: 4.4447 - val_orgCE: 0.9286 - val_myAcc: 0.3152 - val_acc: 0.8493
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.6006 - orgCE: 0.5565 - myAcc: 0.3992 - acc: 0.8536 - val_loss: 4.5203 - val_orgCE: 0.9598 - val_myAcc: 0.3137 - val_acc: 0.8474
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.5610 - orgCE: 0.5391 - myAcc: 0.4004 - acc: 0.8597 - val_loss: 4.4764 - val_orgCE: 0.9340 - val_myAcc: 0.3130 - val_acc: 0.8499
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.5582 - orgCE: 0.5417 - myAcc: 0.4061 - acc: 0.8616 - val_loss: 4.5145 - val_orgCE: 0.9686 - val_myAcc: 0.3097 - val_acc: 0.8458
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.5618 - orgCE: 0.5513 - myAcc: 0.3963 - acc: 0.8515 - val_loss: 4.5037 - val_orgCE: 0.9705 - val_myAcc: 0.3120 - val_acc: 0.8457
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.6204 - orgCE: 0.5563 - myAcc: 0.3872 - acc: 0.8487 - val_loss: 4.6829 - val_orgCE: 1.0591 - val_myAcc: 0.2965 - val_acc: 0.8340
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.5179 - orgCE: 0.5287 - myAcc: 0.4117 - acc: 0.8589 - val_loss: 4.5402 - val_orgCE: 0.9701 - val_myAcc: 0.3124 - val_acc: 0.8484
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 41s - loss: 2.5537 - orgCE: 0.5422 - myAcc: 0.4017 - acc: 0.8515 - val_loss: 4.5705 - val_orgCE: 1.0026 - val_myAcc: 0.3078 - val_acc: 0.8399
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 2.5641 - orgCE: 0.5481 - myAcc: 0.3970 - acc: 0.8540 - val_loss: 4.5598 - val_orgCE: 0.9784 - val_myAcc: 0.3060 - val_acc: 0.8441
