_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
Encoder_in (InputLayer)      (None, 80, 4096)          0         
_________________________________________________________________
zero_padding1d_1 (ZeroPaddin (None, 121, 4096)         0         
_________________________________________________________________
Encoder_out (LSTM)           (None, 121, 1024)         20975616  
_________________________________________________________________
Decoder (RecurrentWrapper)   (None, 121, 6132)         39794676  
_________________________________________________________________
cropping1d_1 (Cropping1D)    (None, 41, 6132)          0         
=================================================================
Total params: 60,770,292
Trainable params: 60,770,292
Non-trainable params: 0
_________________________________________________________________

* Create a new model. *

* Epoch 1/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 67s - loss: 5.9852 - orgCE: 1.3032 - myAcc: 0.1322 - acc: 0.4201 - val_loss: 5.2229 - val_orgCE: 1.0803 - val_myAcc: 0.2254 - val_acc: 0.8395
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 5.1201 - orgCE: 1.1085 - myAcc: 0.2187 - acc: 0.8308 - val_loss: 4.9850 - val_orgCE: 1.0855 - val_myAcc: 0.2562 - val_acc: 0.8380
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.8154 - orgCE: 1.0248 - myAcc: 0.2686 - acc: 0.8442 - val_loss: 4.7987 - val_orgCE: 1.0546 - val_myAcc: 0.2937 - val_acc: 0.8444
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.6160 - orgCE: 0.9965 - myAcc: 0.3030 - acc: 0.8494 - val_loss: 4.7497 - val_orgCE: 1.0370 - val_myAcc: 0.3131 - val_acc: 0.8502
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 63s - loss: 4.5871 - orgCE: 0.9870 - myAcc: 0.2973 - acc: 0.8486 - val_loss: 4.6484 - val_orgCE: 0.9965 - val_myAcc: 0.3137 - val_acc: 0.8527
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.5585 - orgCE: 0.9710 - myAcc: 0.3021 - acc: 0.8509 - val_loss: 4.6568 - val_orgCE: 1.0092 - val_myAcc: 0.3136 - val_acc: 0.8512
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.5363 - orgCE: 0.9768 - myAcc: 0.2964 - acc: 0.8482 - val_loss: 4.5855 - val_orgCE: 0.9879 - val_myAcc: 0.3245 - val_acc: 0.8543
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.5217 - orgCE: 0.9631 - myAcc: 0.2936 - acc: 0.8494 - val_loss: 4.5581 - val_orgCE: 0.9490 - val_myAcc: 0.3226 - val_acc: 0.8587
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.4528 - orgCE: 0.9484 - myAcc: 0.2993 - acc: 0.8504 - val_loss: 4.5683 - val_orgCE: 0.9591 - val_myAcc: 0.3082 - val_acc: 0.8548
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.4920 - orgCE: 0.9605 - myAcc: 0.2987 - acc: 0.8499 - val_loss: 4.5405 - val_orgCE: 0.9687 - val_myAcc: 0.3082 - val_acc: 0.8519
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.3933 - orgCE: 0.9291 - myAcc: 0.2997 - acc: 0.8515 - val_loss: 4.5701 - val_orgCE: 0.9872 - val_myAcc: 0.3105 - val_acc: 0.8509
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.3483 - orgCE: 0.9313 - myAcc: 0.3020 - acc: 0.8501 - val_loss: 4.5290 - val_orgCE: 0.9584 - val_myAcc: 0.3148 - val_acc: 0.8547
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.3275 - orgCE: 0.9237 - myAcc: 0.3035 - acc: 0.8510 - val_loss: 4.7026 - val_orgCE: 1.0383 - val_myAcc: 0.2972 - val_acc: 0.8448
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.2739 - orgCE: 0.8935 - myAcc: 0.3084 - acc: 0.8551 - val_loss: 4.5275 - val_orgCE: 0.9787 - val_myAcc: 0.3114 - val_acc: 0.8509
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.2710 - orgCE: 0.9045 - myAcc: 0.3017 - acc: 0.8517 - val_loss: 4.4979 - val_orgCE: 0.9579 - val_myAcc: 0.3184 - val_acc: 0.8544
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.2380 - orgCE: 0.8990 - myAcc: 0.3042 - acc: 0.8522 - val_loss: 4.4774 - val_orgCE: 0.9774 - val_myAcc: 0.3039 - val_acc: 0.8481
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.2810 - orgCE: 0.9185 - myAcc: 0.3042 - acc: 0.8504 - val_loss: 4.3504 - val_orgCE: 0.9286 - val_myAcc: 0.3177 - val_acc: 0.8535
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 65s - loss: 4.2210 - orgCE: 0.8975 - myAcc: 0.2986 - acc: 0.8503 - val_loss: 4.4138 - val_orgCE: 0.9315 - val_myAcc: 0.3146 - val_acc: 0.8549
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 65s - loss: 4.2419 - orgCE: 0.9140 - myAcc: 0.2997 - acc: 0.8488 - val_loss: 4.5404 - val_orgCE: 0.9975 - val_myAcc: 0.2996 - val_acc: 0.8459
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.1815 - orgCE: 0.8813 - myAcc: 0.3006 - acc: 0.8524 - val_loss: 4.3565 - val_orgCE: 0.9372 - val_myAcc: 0.3024 - val_acc: 0.8498
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 65s - loss: 4.1738 - orgCE: 0.8820 - myAcc: 0.3007 - acc: 0.8516 - val_loss: 4.3600 - val_orgCE: 0.9400 - val_myAcc: 0.3099 - val_acc: 0.8511
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.1550 - orgCE: 0.8823 - myAcc: 0.3043 - acc: 0.8520 - val_loss: 4.4210 - val_orgCE: 0.9418 - val_myAcc: 0.3028 - val_acc: 0.8511
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.0998 - orgCE: 0.8616 - myAcc: 0.3100 - acc: 0.8547 - val_loss: 4.4022 - val_orgCE: 0.9303 - val_myAcc: 0.3161 - val_acc: 0.8553
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.1293 - orgCE: 0.8872 - myAcc: 0.3085 - acc: 0.8512 - val_loss: 4.4601 - val_orgCE: 0.9635 - val_myAcc: 0.3094 - val_acc: 0.8506
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.0816 - orgCE: 0.8583 - myAcc: 0.3123 - acc: 0.8552 - val_loss: 4.3999 - val_orgCE: 0.9568 - val_myAcc: 0.3175 - val_acc: 0.8516
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.0645 - orgCE: 0.8751 - myAcc: 0.3128 - acc: 0.8517 - val_loss: 4.3606 - val_orgCE: 0.9021 - val_myAcc: 0.3175 - val_acc: 0.8586
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.0920 - orgCE: 0.8751 - myAcc: 0.3150 - acc: 0.8532 - val_loss: 4.4141 - val_orgCE: 0.9227 - val_myAcc: 0.3133 - val_acc: 0.8564
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.0008 - orgCE: 0.8503 - myAcc: 0.3212 - acc: 0.8555 - val_loss: 4.2391 - val_orgCE: 0.8786 - val_myAcc: 0.3209 - val_acc: 0.8590
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.0358 - orgCE: 0.8546 - myAcc: 0.3157 - acc: 0.8548 - val_loss: 4.3608 - val_orgCE: 0.9187 - val_myAcc: 0.3105 - val_acc: 0.8548
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.0527 - orgCE: 0.8549 - myAcc: 0.3117 - acc: 0.8546 - val_loss: 4.3524 - val_orgCE: 0.9384 - val_myAcc: 0.3139 - val_acc: 0.8517
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.0338 - orgCE: 0.8650 - myAcc: 0.3144 - acc: 0.8528 - val_loss: 4.3375 - val_orgCE: 0.9303 - val_myAcc: 0.3189 - val_acc: 0.8537
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 4.0724 - orgCE: 0.8880 - myAcc: 0.3122 - acc: 0.8498 - val_loss: 4.3213 - val_orgCE: 0.9248 - val_myAcc: 0.3205 - val_acc: 0.8538
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.9990 - orgCE: 0.8582 - myAcc: 0.3165 - acc: 0.8529 - val_loss: 4.3290 - val_orgCE: 0.9218 - val_myAcc: 0.3070 - val_acc: 0.8521
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.9704 - orgCE: 0.8411 - myAcc: 0.3166 - acc: 0.8552 - val_loss: 4.3348 - val_orgCE: 0.9204 - val_myAcc: 0.3186 - val_acc: 0.8549
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.9680 - orgCE: 0.8368 - myAcc: 0.3143 - acc: 0.8552 - val_loss: 4.2787 - val_orgCE: 0.9113 - val_myAcc: 0.3212 - val_acc: 0.8554
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.8998 - orgCE: 0.8211 - myAcc: 0.3251 - acc: 0.8578 - val_loss: 4.2466 - val_orgCE: 0.8847 - val_myAcc: 0.3322 - val_acc: 0.8609
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.9731 - orgCE: 0.8525 - myAcc: 0.3187 - acc: 0.8536 - val_loss: 4.3113 - val_orgCE: 0.9264 - val_myAcc: 0.3218 - val_acc: 0.8537
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.8687 - orgCE: 0.8151 - myAcc: 0.3244 - acc: 0.8571 - val_loss: 4.3352 - val_orgCE: 0.9241 - val_myAcc: 0.3257 - val_acc: 0.8561
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.8963 - orgCE: 0.8229 - myAcc: 0.3234 - acc: 0.8568 - val_loss: 4.3824 - val_orgCE: 0.9533 - val_myAcc: 0.3180 - val_acc: 0.8512
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.9658 - orgCE: 0.8538 - myAcc: 0.3136 - acc: 0.8513 - val_loss: 4.2693 - val_orgCE: 0.8837 - val_myAcc: 0.3137 - val_acc: 0.8579
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.9276 - orgCE: 0.8335 - myAcc: 0.3171 - acc: 0.8546 - val_loss: 4.3611 - val_orgCE: 0.9321 - val_myAcc: 0.3170 - val_acc: 0.8540
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.8636 - orgCE: 0.8126 - myAcc: 0.3228 - acc: 0.8572 - val_loss: 4.3485 - val_orgCE: 0.9118 - val_myAcc: 0.3215 - val_acc: 0.8577
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.8959 - orgCE: 0.8384 - myAcc: 0.3200 - acc: 0.8533 - val_loss: 4.2964 - val_orgCE: 0.9165 - val_myAcc: 0.3179 - val_acc: 0.8534
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.8734 - orgCE: 0.8162 - myAcc: 0.3282 - acc: 0.8582 - val_loss: 4.3656 - val_orgCE: 0.9331 - val_myAcc: 0.3154 - val_acc: 0.8528
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.8439 - orgCE: 0.8119 - myAcc: 0.3225 - acc: 0.8565 - val_loss: 4.2375 - val_orgCE: 0.8911 - val_myAcc: 0.3223 - val_acc: 0.8569
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.7834 - orgCE: 0.8055 - myAcc: 0.3303 - acc: 0.8568 - val_loss: 4.2798 - val_orgCE: 0.8870 - val_myAcc: 0.3219 - val_acc: 0.8591
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.8519 - orgCE: 0.8234 - myAcc: 0.3206 - acc: 0.8544 - val_loss: 4.3854 - val_orgCE: 0.9507 - val_myAcc: 0.3208 - val_acc: 0.8526
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.8418 - orgCE: 0.8156 - myAcc: 0.3260 - acc: 0.8566 - val_loss: 4.1983 - val_orgCE: 0.9060 - val_myAcc: 0.3330 - val_acc: 0.8559
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.7755 - orgCE: 0.8056 - myAcc: 0.3289 - acc: 0.8565 - val_loss: 4.2832 - val_orgCE: 0.9172 - val_myAcc: 0.3144 - val_acc: 0.8528
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.7901 - orgCE: 0.7870 - myAcc: 0.3333 - acc: 0.8608 - val_loss: 4.2856 - val_orgCE: 0.9091 - val_myAcc: 0.3200 - val_acc: 0.8558
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.8277 - orgCE: 0.8159 - myAcc: 0.3241 - acc: 0.8554 - val_loss: 4.2325 - val_orgCE: 0.8993 - val_myAcc: 0.3219 - val_acc: 0.8556
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.8023 - orgCE: 0.8214 - myAcc: 0.3218 - acc: 0.8529 - val_loss: 4.2200 - val_orgCE: 0.8865 - val_myAcc: 0.3318 - val_acc: 0.8590
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.7756 - orgCE: 0.7994 - myAcc: 0.3249 - acc: 0.8565 - val_loss: 4.2768 - val_orgCE: 0.9249 - val_myAcc: 0.3180 - val_acc: 0.8517
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.7982 - orgCE: 0.8142 - myAcc: 0.3240 - acc: 0.8544 - val_loss: 4.3080 - val_orgCE: 0.9209 - val_myAcc: 0.3067 - val_acc: 0.8513
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.7739 - orgCE: 0.8060 - myAcc: 0.3283 - acc: 0.8558 - val_loss: 4.3892 - val_orgCE: 0.9638 - val_myAcc: 0.3079 - val_acc: 0.8479
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.7023 - orgCE: 0.7815 - myAcc: 0.3412 - acc: 0.8602 - val_loss: 4.3615 - val_orgCE: 0.9365 - val_myAcc: 0.3194 - val_acc: 0.8536
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.6793 - orgCE: 0.7723 - myAcc: 0.3380 - acc: 0.8606 - val_loss: 4.2576 - val_orgCE: 0.8981 - val_myAcc: 0.3242 - val_acc: 0.8567
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.7523 - orgCE: 0.8048 - myAcc: 0.3327 - acc: 0.8563 - val_loss: 4.3090 - val_orgCE: 0.9149 - val_myAcc: 0.3089 - val_acc: 0.8524
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.7110 - orgCE: 0.7951 - myAcc: 0.3276 - acc: 0.8553 - val_loss: 4.3490 - val_orgCE: 0.9392 - val_myAcc: 0.3116 - val_acc: 0.8505
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.7020 - orgCE: 0.7920 - myAcc: 0.3297 - acc: 0.8561 - val_loss: 4.2247 - val_orgCE: 0.9008 - val_myAcc: 0.3301 - val_acc: 0.8568
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.6951 - orgCE: 0.7868 - myAcc: 0.3320 - acc: 0.8569 - val_loss: 4.2693 - val_orgCE: 0.9180 - val_myAcc: 0.3069 - val_acc: 0.8508
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.6614 - orgCE: 0.7777 - myAcc: 0.3388 - acc: 0.8589 - val_loss: 4.2467 - val_orgCE: 0.8976 - val_myAcc: 0.3247 - val_acc: 0.8560
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.6952 - orgCE: 0.7880 - myAcc: 0.3318 - acc: 0.8564 - val_loss: 4.2240 - val_orgCE: 0.8866 - val_myAcc: 0.3249 - val_acc: 0.8575
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.6723 - orgCE: 0.7831 - myAcc: 0.3330 - acc: 0.8569 - val_loss: 4.2565 - val_orgCE: 0.8945 - val_myAcc: 0.3254 - val_acc: 0.8569
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.6251 - orgCE: 0.7742 - myAcc: 0.3360 - acc: 0.8571 - val_loss: 4.3743 - val_orgCE: 0.9276 - val_myAcc: 0.3083 - val_acc: 0.8519
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.6738 - orgCE: 0.7828 - myAcc: 0.3334 - acc: 0.8569 - val_loss: 4.3110 - val_orgCE: 0.9203 - val_myAcc: 0.3112 - val_acc: 0.8524
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 65s - loss: 3.6646 - orgCE: 0.7894 - myAcc: 0.3351 - acc: 0.8558 - val_loss: 4.3792 - val_orgCE: 0.9390 - val_myAcc: 0.3145 - val_acc: 0.8526
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.7083 - orgCE: 0.8003 - myAcc: 0.3280 - acc: 0.8544 - val_loss: 4.1473 - val_orgCE: 0.8528 - val_myAcc: 0.3340 - val_acc: 0.8616
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5869 - orgCE: 0.7486 - myAcc: 0.3370 - acc: 0.8607 - val_loss: 4.2134 - val_orgCE: 0.8910 - val_myAcc: 0.3339 - val_acc: 0.8582
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5556 - orgCE: 0.7498 - myAcc: 0.3474 - acc: 0.8616 - val_loss: 4.3771 - val_orgCE: 0.9504 - val_myAcc: 0.3132 - val_acc: 0.8507
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5852 - orgCE: 0.7652 - myAcc: 0.3362 - acc: 0.8574 - val_loss: 4.3003 - val_orgCE: 0.9087 - val_myAcc: 0.3051 - val_acc: 0.8526
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.6213 - orgCE: 0.7790 - myAcc: 0.3335 - acc: 0.8557 - val_loss: 4.2660 - val_orgCE: 0.9014 - val_myAcc: 0.3292 - val_acc: 0.8569
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5565 - orgCE: 0.7522 - myAcc: 0.3497 - acc: 0.8617 - val_loss: 4.3627 - val_orgCE: 0.9528 - val_myAcc: 0.3055 - val_acc: 0.8479
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5516 - orgCE: 0.7489 - myAcc: 0.3433 - acc: 0.8606 - val_loss: 4.2292 - val_orgCE: 0.8810 - val_myAcc: 0.3260 - val_acc: 0.8590
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5802 - orgCE: 0.7574 - myAcc: 0.3440 - acc: 0.8607 - val_loss: 4.1774 - val_orgCE: 0.8888 - val_myAcc: 0.3325 - val_acc: 0.8569
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5826 - orgCE: 0.7581 - myAcc: 0.3396 - acc: 0.8596 - val_loss: 4.0864 - val_orgCE: 0.8461 - val_myAcc: 0.3380 - val_acc: 0.8614
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5697 - orgCE: 0.7579 - myAcc: 0.3390 - acc: 0.8587 - val_loss: 4.3746 - val_orgCE: 0.9393 - val_myAcc: 0.3132 - val_acc: 0.8516
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5662 - orgCE: 0.7688 - myAcc: 0.3378 - acc: 0.8562 - val_loss: 4.1808 - val_orgCE: 0.8694 - val_myAcc: 0.3360 - val_acc: 0.8604
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4951 - orgCE: 0.7360 - myAcc: 0.3502 - acc: 0.8623 - val_loss: 4.2425 - val_orgCE: 0.9209 - val_myAcc: 0.3245 - val_acc: 0.8528
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5306 - orgCE: 0.7487 - myAcc: 0.3482 - acc: 0.8607 - val_loss: 4.3052 - val_orgCE: 0.9286 - val_myAcc: 0.3230 - val_acc: 0.8529
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5126 - orgCE: 0.7387 - myAcc: 0.3463 - acc: 0.8617 - val_loss: 4.1621 - val_orgCE: 0.8836 - val_myAcc: 0.3308 - val_acc: 0.8571
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5643 - orgCE: 0.7610 - myAcc: 0.3327 - acc: 0.8569 - val_loss: 4.2259 - val_orgCE: 0.8826 - val_myAcc: 0.3396 - val_acc: 0.8615
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5235 - orgCE: 0.7336 - myAcc: 0.3470 - acc: 0.8634 - val_loss: 4.3302 - val_orgCE: 0.9488 - val_myAcc: 0.3156 - val_acc: 0.8489
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5521 - orgCE: 0.7573 - myAcc: 0.3415 - acc: 0.8584 - val_loss: 4.4143 - val_orgCE: 0.9798 - val_myAcc: 0.2980 - val_acc: 0.8436
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5457 - orgCE: 0.7542 - myAcc: 0.3439 - acc: 0.8596 - val_loss: 4.2342 - val_orgCE: 0.9140 - val_myAcc: 0.3256 - val_acc: 0.8542
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5119 - orgCE: 0.7367 - myAcc: 0.3396 - acc: 0.8610 - val_loss: 4.3643 - val_orgCE: 0.9352 - val_myAcc: 0.3059 - val_acc: 0.8495
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5230 - orgCE: 0.7514 - myAcc: 0.3386 - acc: 0.8580 - val_loss: 4.1958 - val_orgCE: 0.8802 - val_myAcc: 0.3245 - val_acc: 0.8576
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5315 - orgCE: 0.7652 - myAcc: 0.3382 - acc: 0.8560 - val_loss: 4.2810 - val_orgCE: 0.9279 - val_myAcc: 0.3090 - val_acc: 0.8493
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4740 - orgCE: 0.7414 - myAcc: 0.3469 - acc: 0.8594 - val_loss: 4.2983 - val_orgCE: 0.9353 - val_myAcc: 0.3169 - val_acc: 0.8505
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4292 - orgCE: 0.7263 - myAcc: 0.3532 - acc: 0.8622 - val_loss: 4.2551 - val_orgCE: 0.8755 - val_myAcc: 0.3253 - val_acc: 0.8593
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.5223 - orgCE: 0.7542 - myAcc: 0.3395 - acc: 0.8576 - val_loss: 4.2946 - val_orgCE: 0.9174 - val_myAcc: 0.3175 - val_acc: 0.8531
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4411 - orgCE: 0.7385 - myAcc: 0.3567 - acc: 0.8609 - val_loss: 4.2392 - val_orgCE: 0.9046 - val_myAcc: 0.3130 - val_acc: 0.8521
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4767 - orgCE: 0.7450 - myAcc: 0.3438 - acc: 0.8585 - val_loss: 4.3022 - val_orgCE: 0.9502 - val_myAcc: 0.3029 - val_acc: 0.8447
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4226 - orgCE: 0.7210 - myAcc: 0.3536 - acc: 0.8625 - val_loss: 4.2281 - val_orgCE: 0.9072 - val_myAcc: 0.3197 - val_acc: 0.8529
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4584 - orgCE: 0.7391 - myAcc: 0.3455 - acc: 0.8594 - val_loss: 4.3014 - val_orgCE: 0.9188 - val_myAcc: 0.3115 - val_acc: 0.8521
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4931 - orgCE: 0.7466 - myAcc: 0.3404 - acc: 0.8579 - val_loss: 4.2140 - val_orgCE: 0.8882 - val_myAcc: 0.3190 - val_acc: 0.8553
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4058 - orgCE: 0.7244 - myAcc: 0.3507 - acc: 0.8605 - val_loss: 4.3070 - val_orgCE: 0.9169 - val_myAcc: 0.3133 - val_acc: 0.8526
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4729 - orgCE: 0.7378 - myAcc: 0.3479 - acc: 0.8603 - val_loss: 4.2587 - val_orgCE: 0.9229 - val_myAcc: 0.3140 - val_acc: 0.8505
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4127 - orgCE: 0.7199 - myAcc: 0.3481 - acc: 0.8614 - val_loss: 4.3869 - val_orgCE: 0.9223 - val_myAcc: 0.3127 - val_acc: 0.8548
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 64s - loss: 3.4639 - orgCE: 0.7428 - myAcc: 0.3444 - acc: 0.8583 - val_loss: 4.3680 - val_orgCE: 0.9764 - val_myAcc: 0.3137 - val_acc: 0.8455


# python3 bleu_eval.py sample_output_testset.txt
Originally, average bleu score is 0.27703807422640936
By another method, average bleu score is 0.6773119086851201
