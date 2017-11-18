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
1160/1160 [==============================] - 73s - loss: 5.9573 - orgCE: 1.2708 - myAcc: 0.1533 - acc: 0.4767 - val_loss: 5.2220 - val_orgCE: 1.1218 - val_myAcc: 0.2046 - val_acc: 0.8293
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 5.0728 - orgCE: 1.0597 - myAcc: 0.2482 - acc: 0.8427 - val_loss: 4.9450 - val_orgCE: 1.0616 - val_myAcc: 0.2568 - val_acc: 0.7780
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.7841 - orgCE: 1.0077 - myAcc: 0.2794 - acc: 0.8389 - val_loss: 4.7262 - val_orgCE: 0.9847 - val_myAcc: 0.3117 - val_acc: 0.8564
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.6590 - orgCE: 0.9985 - myAcc: 0.2978 - acc: 0.8491 - val_loss: 4.7377 - val_orgCE: 1.0325 - val_myAcc: 0.2985 - val_acc: 0.8468
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.5997 - orgCE: 0.9783 - myAcc: 0.2968 - acc: 0.8499 - val_loss: 4.6319 - val_orgCE: 0.9578 - val_myAcc: 0.3090 - val_acc: 0.8568
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.5516 - orgCE: 0.9757 - myAcc: 0.2975 - acc: 0.8489 - val_loss: 4.7196 - val_orgCE: 1.0413 - val_myAcc: 0.2958 - val_acc: 0.8446
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.5738 - orgCE: 0.9775 - myAcc: 0.3014 - acc: 0.8505 - val_loss: 4.6379 - val_orgCE: 0.9787 - val_myAcc: 0.3154 - val_acc: 0.8554
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.5570 - orgCE: 0.9755 - myAcc: 0.2940 - acc: 0.8482 - val_loss: 4.5080 - val_orgCE: 0.9632 - val_myAcc: 0.3098 - val_acc: 0.8521
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.4815 - orgCE: 0.9383 - myAcc: 0.3024 - acc: 0.8535 - val_loss: 4.5647 - val_orgCE: 0.9736 - val_myAcc: 0.3194 - val_acc: 0.8548
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.4829 - orgCE: 0.9432 - myAcc: 0.3012 - acc: 0.8528 - val_loss: 4.6462 - val_orgCE: 1.0100 - val_myAcc: 0.3106 - val_acc: 0.8498
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.4513 - orgCE: 0.9465 - myAcc: 0.2986 - acc: 0.8508 - val_loss: 4.5663 - val_orgCE: 0.9715 - val_myAcc: 0.3105 - val_acc: 0.8529
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.5367 - orgCE: 0.9861 - myAcc: 0.2957 - acc: 0.8467 - val_loss: 4.5148 - val_orgCE: 0.9626 - val_myAcc: 0.3168 - val_acc: 0.8541
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.4851 - orgCE: 0.9773 - myAcc: 0.2881 - acc: 0.8443 - val_loss: 4.5094 - val_orgCE: 0.9570 - val_myAcc: 0.3183 - val_acc: 0.8552
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.3491 - orgCE: 0.8993 - myAcc: 0.3078 - acc: 0.8566 - val_loss: 4.5400 - val_orgCE: 0.9343 - val_myAcc: 0.3159 - val_acc: 0.8590
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.4087 - orgCE: 0.9384 - myAcc: 0.2977 - acc: 0.8499 - val_loss: 4.5769 - val_orgCE: 0.9786 - val_myAcc: 0.3105 - val_acc: 0.8523
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.3753 - orgCE: 0.9272 - myAcc: 0.2971 - acc: 0.8489 - val_loss: 4.6600 - val_orgCE: 0.9869 - val_myAcc: 0.3127 - val_acc: 0.8543
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.3558 - orgCE: 0.9281 - myAcc: 0.3014 - acc: 0.8508 - val_loss: 4.4495 - val_orgCE: 0.9284 - val_myAcc: 0.3214 - val_acc: 0.8584
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.2670 - orgCE: 0.9063 - myAcc: 0.3059 - acc: 0.8486 - val_loss: 4.5322 - val_orgCE: 0.9765 - val_myAcc: 0.3042 - val_acc: 0.8500
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.2687 - orgCE: 0.9097 - myAcc: 0.3055 - acc: 0.8517 - val_loss: 4.5240 - val_orgCE: 0.9500 - val_myAcc: 0.3045 - val_acc: 0.8535
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.2427 - orgCE: 0.8950 - myAcc: 0.3038 - acc: 0.8528 - val_loss: 4.5583 - val_orgCE: 0.9868 - val_myAcc: 0.2999 - val_acc: 0.8482
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.2529 - orgCE: 0.9106 - myAcc: 0.3036 - acc: 0.8505 - val_loss: 4.4373 - val_orgCE: 0.9430 - val_myAcc: 0.3165 - val_acc: 0.8548
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.2310 - orgCE: 0.8898 - myAcc: 0.3070 - acc: 0.8538 - val_loss: 4.4559 - val_orgCE: 0.9512 - val_myAcc: 0.3033 - val_acc: 0.8510
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.2166 - orgCE: 0.9039 - myAcc: 0.3047 - acc: 0.8507 - val_loss: 4.4966 - val_orgCE: 1.0056 - val_myAcc: 0.2941 - val_acc: 0.8421
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.2097 - orgCE: 0.9108 - myAcc: 0.3041 - acc: 0.8491 - val_loss: 4.4724 - val_orgCE: 0.9805 - val_myAcc: 0.3050 - val_acc: 0.8474
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.1773 - orgCE: 0.8819 - myAcc: 0.3049 - acc: 0.8529 - val_loss: 4.4290 - val_orgCE: 0.9408 - val_myAcc: 0.3092 - val_acc: 0.8530
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.2273 - orgCE: 0.9162 - myAcc: 0.3005 - acc: 0.8482 - val_loss: 4.3836 - val_orgCE: 0.9226 - val_myAcc: 0.3227 - val_acc: 0.8563
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.1134 - orgCE: 0.8713 - myAcc: 0.3082 - acc: 0.8527 - val_loss: 4.3887 - val_orgCE: 0.9264 - val_myAcc: 0.3188 - val_acc: 0.8558
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.1793 - orgCE: 0.8969 - myAcc: 0.3028 - acc: 0.8499 - val_loss: 4.3795 - val_orgCE: 0.9335 - val_myAcc: 0.3148 - val_acc: 0.8538
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.1084 - orgCE: 0.8682 - myAcc: 0.3115 - acc: 0.8542 - val_loss: 4.4209 - val_orgCE: 0.9620 - val_myAcc: 0.3108 - val_acc: 0.8500
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.1201 - orgCE: 0.8798 - myAcc: 0.3066 - acc: 0.8516 - val_loss: 4.3514 - val_orgCE: 0.9003 - val_myAcc: 0.3238 - val_acc: 0.8600
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.1459 - orgCE: 0.8851 - myAcc: 0.3089 - acc: 0.8522 - val_loss: 4.3372 - val_orgCE: 0.9109 - val_myAcc: 0.3182 - val_acc: 0.8564
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.0800 - orgCE: 0.8704 - myAcc: 0.3146 - acc: 0.8536 - val_loss: 4.4730 - val_orgCE: 0.9688 - val_myAcc: 0.3136 - val_acc: 0.8511
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.1256 - orgCE: 0.9022 - myAcc: 0.3064 - acc: 0.8482 - val_loss: 4.3033 - val_orgCE: 0.9009 - val_myAcc: 0.3217 - val_acc: 0.8573
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.0676 - orgCE: 0.8735 - myAcc: 0.3101 - acc: 0.8516 - val_loss: 4.4042 - val_orgCE: 0.9485 - val_myAcc: 0.3212 - val_acc: 0.8537
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.0282 - orgCE: 0.8478 - myAcc: 0.3181 - acc: 0.8562 - val_loss: 4.4289 - val_orgCE: 0.9789 - val_myAcc: 0.3036 - val_acc: 0.8460
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.0429 - orgCE: 0.8643 - myAcc: 0.3195 - acc: 0.8540 - val_loss: 4.3172 - val_orgCE: 0.9305 - val_myAcc: 0.3188 - val_acc: 0.8531
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.0543 - orgCE: 0.8678 - myAcc: 0.3151 - acc: 0.8532 - val_loss: 4.5730 - val_orgCE: 1.0246 - val_myAcc: 0.2991 - val_acc: 0.8425
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.0312 - orgCE: 0.8654 - myAcc: 0.3186 - acc: 0.8532 - val_loss: 4.2846 - val_orgCE: 0.8956 - val_myAcc: 0.3276 - val_acc: 0.8592
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.0013 - orgCE: 0.8459 - myAcc: 0.3207 - acc: 0.8561 - val_loss: 4.2700 - val_orgCE: 0.8831 - val_myAcc: 0.3160 - val_acc: 0.8576
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.0068 - orgCE: 0.8497 - myAcc: 0.3163 - acc: 0.8544 - val_loss: 4.3220 - val_orgCE: 0.9141 - val_myAcc: 0.3164 - val_acc: 0.8551
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.0339 - orgCE: 0.8643 - myAcc: 0.3107 - acc: 0.8519 - val_loss: 4.2491 - val_orgCE: 0.8831 - val_myAcc: 0.3241 - val_acc: 0.8591
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 4.0524 - orgCE: 0.8919 - myAcc: 0.3069 - acc: 0.8466 - val_loss: 4.4337 - val_orgCE: 0.9541 - val_myAcc: 0.3037 - val_acc: 0.8501
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.9783 - orgCE: 0.8400 - myAcc: 0.3237 - acc: 0.8569 - val_loss: 4.1566 - val_orgCE: 0.8679 - val_myAcc: 0.3313 - val_acc: 0.8601
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.9305 - orgCE: 0.8325 - myAcc: 0.3306 - acc: 0.8579 - val_loss: 4.4780 - val_orgCE: 0.9980 - val_myAcc: 0.3071 - val_acc: 0.8456
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.9740 - orgCE: 0.8538 - myAcc: 0.3130 - acc: 0.8521 - val_loss: 4.3061 - val_orgCE: 0.9205 - val_myAcc: 0.3112 - val_acc: 0.8526
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.9227 - orgCE: 0.8462 - myAcc: 0.3210 - acc: 0.8532 - val_loss: 4.3489 - val_orgCE: 0.9526 - val_myAcc: 0.2980 - val_acc: 0.8460
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.9360 - orgCE: 0.8389 - myAcc: 0.3242 - acc: 0.8557 - val_loss: 4.3358 - val_orgCE: 0.9416 - val_myAcc: 0.3183 - val_acc: 0.8515
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8856 - orgCE: 0.8214 - myAcc: 0.3273 - acc: 0.8574 - val_loss: 4.3513 - val_orgCE: 0.9423 - val_myAcc: 0.3121 - val_acc: 0.8509
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.9335 - orgCE: 0.8484 - myAcc: 0.3159 - acc: 0.8520 - val_loss: 4.2698 - val_orgCE: 0.8822 - val_myAcc: 0.3214 - val_acc: 0.8595
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8913 - orgCE: 0.8306 - myAcc: 0.3257 - acc: 0.8553 - val_loss: 4.3899 - val_orgCE: 0.9238 - val_myAcc: 0.3190 - val_acc: 0.8568
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8666 - orgCE: 0.8195 - myAcc: 0.3300 - acc: 0.8576 - val_loss: 4.3216 - val_orgCE: 0.8914 - val_myAcc: 0.3174 - val_acc: 0.8580
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8820 - orgCE: 0.8373 - myAcc: 0.3316 - acc: 0.8546 - val_loss: 4.4394 - val_orgCE: 0.9852 - val_myAcc: 0.3056 - val_acc: 0.8458
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.9124 - orgCE: 0.8554 - myAcc: 0.3176 - acc: 0.8498 - val_loss: 4.3998 - val_orgCE: 0.9663 - val_myAcc: 0.3075 - val_acc: 0.8476
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8954 - orgCE: 0.8342 - myAcc: 0.3281 - acc: 0.8557 - val_loss: 4.3190 - val_orgCE: 0.9113 - val_myAcc: 0.3201 - val_acc: 0.8551
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8399 - orgCE: 0.8163 - myAcc: 0.3348 - acc: 0.8578 - val_loss: 4.2700 - val_orgCE: 0.9166 - val_myAcc: 0.3255 - val_acc: 0.8549
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8051 - orgCE: 0.8089 - myAcc: 0.3334 - acc: 0.8579 - val_loss: 4.2751 - val_orgCE: 0.8970 - val_myAcc: 0.3301 - val_acc: 0.8590
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8537 - orgCE: 0.8267 - myAcc: 0.3317 - acc: 0.8556 - val_loss: 4.1769 - val_orgCE: 0.8795 - val_myAcc: 0.3421 - val_acc: 0.8605
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8777 - orgCE: 0.8320 - myAcc: 0.3281 - acc: 0.8551 - val_loss: 4.2986 - val_orgCE: 0.9209 - val_myAcc: 0.3215 - val_acc: 0.8544
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8041 - orgCE: 0.8030 - myAcc: 0.3265 - acc: 0.8572 - val_loss: 4.3444 - val_orgCE: 0.9137 - val_myAcc: 0.3234 - val_acc: 0.8572
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8049 - orgCE: 0.8037 - myAcc: 0.3263 - acc: 0.8571 - val_loss: 4.3439 - val_orgCE: 0.9179 - val_myAcc: 0.3220 - val_acc: 0.8563
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8336 - orgCE: 0.8193 - myAcc: 0.3276 - acc: 0.8554 - val_loss: 4.2076 - val_orgCE: 0.8721 - val_myAcc: 0.3299 - val_acc: 0.8608
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8141 - orgCE: 0.8144 - myAcc: 0.3296 - acc: 0.8560 - val_loss: 4.2592 - val_orgCE: 0.9025 - val_myAcc: 0.3344 - val_acc: 0.8581
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8090 - orgCE: 0.8117 - myAcc: 0.3246 - acc: 0.8550 - val_loss: 4.4723 - val_orgCE: 0.9838 - val_myAcc: 0.3143 - val_acc: 0.8484
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8267 - orgCE: 0.8190 - myAcc: 0.3242 - acc: 0.8546 - val_loss: 4.3259 - val_orgCE: 0.9300 - val_myAcc: 0.3104 - val_acc: 0.8506
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8117 - orgCE: 0.8152 - myAcc: 0.3285 - acc: 0.8556 - val_loss: 4.2598 - val_orgCE: 0.9028 - val_myAcc: 0.3178 - val_acc: 0.8545
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.8258 - orgCE: 0.8299 - myAcc: 0.3287 - acc: 0.8536 - val_loss: 4.2051 - val_orgCE: 0.8787 - val_myAcc: 0.3297 - val_acc: 0.8597
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.7257 - orgCE: 0.7932 - myAcc: 0.3412 - acc: 0.8588 - val_loss: 4.2259 - val_orgCE: 0.8734 - val_myAcc: 0.3229 - val_acc: 0.8589
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 71s - loss: 3.7500 - orgCE: 0.8038 - myAcc: 0.3281 - acc: 0.8550 - val_loss: 4.3318 - val_orgCE: 0.9196 - val_myAcc: 0.3137 - val_acc: 0.8531
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6978 - orgCE: 0.7855 - myAcc: 0.3409 - acc: 0.8588 - val_loss: 4.2473 - val_orgCE: 0.9078 - val_myAcc: 0.3264 - val_acc: 0.8549
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.7877 - orgCE: 0.8088 - myAcc: 0.3316 - acc: 0.8561 - val_loss: 4.3352 - val_orgCE: 0.9130 - val_myAcc: 0.3189 - val_acc: 0.8554
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.7353 - orgCE: 0.7983 - myAcc: 0.3355 - acc: 0.8564 - val_loss: 4.2123 - val_orgCE: 0.8912 - val_myAcc: 0.3352 - val_acc: 0.8579
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.7343 - orgCE: 0.7907 - myAcc: 0.3333 - acc: 0.8578 - val_loss: 4.2238 - val_orgCE: 0.8970 - val_myAcc: 0.3267 - val_acc: 0.8564
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.7727 - orgCE: 0.8190 - myAcc: 0.3260 - acc: 0.8527 - val_loss: 4.2077 - val_orgCE: 0.8943 - val_myAcc: 0.3202 - val_acc: 0.8551
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6977 - orgCE: 0.7926 - myAcc: 0.3392 - acc: 0.8572 - val_loss: 4.4000 - val_orgCE: 0.9589 - val_myAcc: 0.3167 - val_acc: 0.8497
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6801 - orgCE: 0.7797 - myAcc: 0.3399 - acc: 0.8597 - val_loss: 4.2525 - val_orgCE: 0.8936 - val_myAcc: 0.3398 - val_acc: 0.8606
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.7389 - orgCE: 0.8036 - myAcc: 0.3284 - acc: 0.8544 - val_loss: 4.2484 - val_orgCE: 0.9023 - val_myAcc: 0.3186 - val_acc: 0.8532
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.7421 - orgCE: 0.8061 - myAcc: 0.3332 - acc: 0.8553 - val_loss: 4.2703 - val_orgCE: 0.9089 - val_myAcc: 0.3253 - val_acc: 0.8560
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6442 - orgCE: 0.7687 - myAcc: 0.3431 - acc: 0.8601 - val_loss: 4.3241 - val_orgCE: 0.9288 - val_myAcc: 0.3096 - val_acc: 0.8510
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6513 - orgCE: 0.7818 - myAcc: 0.3390 - acc: 0.8574 - val_loss: 4.3729 - val_orgCE: 0.9735 - val_myAcc: 0.3055 - val_acc: 0.8439
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6678 - orgCE: 0.7757 - myAcc: 0.3392 - acc: 0.8591 - val_loss: 4.3092 - val_orgCE: 0.9087 - val_myAcc: 0.3200 - val_acc: 0.8559
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6626 - orgCE: 0.7744 - myAcc: 0.3445 - acc: 0.8606 - val_loss: 4.2102 - val_orgCE: 0.9007 - val_myAcc: 0.3288 - val_acc: 0.8555
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6776 - orgCE: 0.7906 - myAcc: 0.3327 - acc: 0.8555 - val_loss: 4.2244 - val_orgCE: 0.8852 - val_myAcc: 0.3289 - val_acc: 0.8589
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.7435 - orgCE: 0.8132 - myAcc: 0.3275 - acc: 0.8532 - val_loss: 4.2495 - val_orgCE: 0.9125 - val_myAcc: 0.3342 - val_acc: 0.8552
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6455 - orgCE: 0.7741 - myAcc: 0.3415 - acc: 0.8587 - val_loss: 4.2756 - val_orgCE: 0.9159 - val_myAcc: 0.3227 - val_acc: 0.8532
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6557 - orgCE: 0.7801 - myAcc: 0.3390 - acc: 0.8577 - val_loss: 4.1385 - val_orgCE: 0.8604 - val_myAcc: 0.3402 - val_acc: 0.8609
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.5839 - orgCE: 0.7448 - myAcc: 0.3422 - acc: 0.8621 - val_loss: 4.4064 - val_orgCE: 0.9760 - val_myAcc: 0.2980 - val_acc: 0.8437
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6125 - orgCE: 0.7616 - myAcc: 0.3426 - acc: 0.8607 - val_loss: 4.2560 - val_orgCE: 0.9327 - val_myAcc: 0.3124 - val_acc: 0.8475
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6188 - orgCE: 0.7745 - myAcc: 0.3401 - acc: 0.8573 - val_loss: 4.3054 - val_orgCE: 0.9104 - val_myAcc: 0.3166 - val_acc: 0.8542
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6358 - orgCE: 0.7753 - myAcc: 0.3392 - acc: 0.8580 - val_loss: 4.2522 - val_orgCE: 0.8850 - val_myAcc: 0.3323 - val_acc: 0.8596
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.5782 - orgCE: 0.7473 - myAcc: 0.3415 - acc: 0.8609 - val_loss: 4.2155 - val_orgCE: 0.9068 - val_myAcc: 0.3302 - val_acc: 0.8553
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6161 - orgCE: 0.7714 - myAcc: 0.3452 - acc: 0.8593 - val_loss: 4.2402 - val_orgCE: 0.9087 - val_myAcc: 0.3195 - val_acc: 0.8531
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.5711 - orgCE: 0.7592 - myAcc: 0.3455 - acc: 0.8595 - val_loss: 4.3376 - val_orgCE: 0.9241 - val_myAcc: 0.3128 - val_acc: 0.8516
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6185 - orgCE: 0.7716 - myAcc: 0.3422 - acc: 0.8587 - val_loss: 4.3080 - val_orgCE: 0.8946 - val_myAcc: 0.3191 - val_acc: 0.8578
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6017 - orgCE: 0.7621 - myAcc: 0.3449 - acc: 0.8599 - val_loss: 4.1892 - val_orgCE: 0.8629 - val_myAcc: 0.3398 - val_acc: 0.8626
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.6298 - orgCE: 0.7700 - myAcc: 0.3375 - acc: 0.8582 - val_loss: 4.2884 - val_orgCE: 0.9167 - val_myAcc: 0.3308 - val_acc: 0.8560
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.5712 - orgCE: 0.7524 - myAcc: 0.3469 - acc: 0.8612 - val_loss: 4.2157 - val_orgCE: 0.8700 - val_myAcc: 0.3288 - val_acc: 0.8601
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.5770 - orgCE: 0.7580 - myAcc: 0.3459 - acc: 0.8604 - val_loss: 4.1199 - val_orgCE: 0.8487 - val_myAcc: 0.3495 - val_acc: 0.8645
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.5782 - orgCE: 0.7608 - myAcc: 0.3414 - acc: 0.8590 - val_loss: 4.2582 - val_orgCE: 0.9014 - val_myAcc: 0.3222 - val_acc: 0.8554
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.5295 - orgCE: 0.7430 - myAcc: 0.3457 - acc: 0.8611 - val_loss: 4.1535 - val_orgCE: 0.8870 - val_myAcc: 0.3259 - val_acc: 0.8548
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 70s - loss: 3.5459 - orgCE: 0.7472 - myAcc: 0.3421 - acc: 0.8605 - val_loss: 4.3120 - val_orgCE: 0.9104 - val_myAcc: 0.3115 - val_acc: 0.8537


# python3 bleu_eval.py sample_output_testset.txt
Originally, average bleu score is 0.27142940475061855
By another method, average bleu score is 0.6720606586575475
