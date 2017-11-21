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
1160/1160 [==============================] - 49s - loss: 6.5544 - orgCE: 1.3689 - myAcc: 0.1912 - acc: 0.5183 - val_loss: 5.8426 - val_orgCE: 1.2538 - val_myAcc: 0.2490 - val_acc: 0.8389
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 5.6625 - orgCE: 1.1944 - myAcc: 0.2839 - acc: 0.8488 - val_loss: 5.6091 - val_orgCE: 1.2194 - val_myAcc: 0.2937 - val_acc: 0.8447
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 5.4525 - orgCE: 1.1428 - myAcc: 0.2964 - acc: 0.8521 - val_loss: 5.5693 - val_orgCE: 1.2303 - val_myAcc: 0.2195 - val_acc: 0.8272
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 5.3681 - orgCE: 1.1447 - myAcc: 0.2261 - acc: 0.8346 - val_loss: 5.3572 - val_orgCE: 1.1460 - val_myAcc: 0.2428 - val_acc: 0.8378
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 5.2297 - orgCE: 1.1306 - myAcc: 0.2260 - acc: 0.8323 - val_loss: 5.2511 - val_orgCE: 1.1010 - val_myAcc: 0.2366 - val_acc: 0.8397
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 5.0672 - orgCE: 1.0712 - myAcc: 0.2309 - acc: 0.8370 - val_loss: 5.0251 - val_orgCE: 1.0495 - val_myAcc: 0.2418 - val_acc: 0.8416
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.9554 - orgCE: 1.0829 - myAcc: 0.2227 - acc: 0.8297 - val_loss: 4.9348 - val_orgCE: 1.0775 - val_myAcc: 0.2296 - val_acc: 0.8316
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.6458 - orgCE: 0.9924 - myAcc: 0.2384 - acc: 0.8368 - val_loss: 4.6895 - val_orgCE: 1.0173 - val_myAcc: 0.3185 - val_acc: 0.8519
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.4912 - orgCE: 0.9623 - myAcc: 0.3002 - acc: 0.8492 - val_loss: 4.6027 - val_orgCE: 1.0011 - val_myAcc: 0.3013 - val_acc: 0.8466
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.4094 - orgCE: 0.9561 - myAcc: 0.2962 - acc: 0.8464 - val_loss: 4.5525 - val_orgCE: 0.9782 - val_myAcc: 0.3131 - val_acc: 0.8522
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.3132 - orgCE: 0.9161 - myAcc: 0.3011 - acc: 0.8512 - val_loss: 4.5686 - val_orgCE: 1.0008 - val_myAcc: 0.3050 - val_acc: 0.8475
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.3084 - orgCE: 0.9301 - myAcc: 0.3040 - acc: 0.8494 - val_loss: 4.4799 - val_orgCE: 0.9584 - val_myAcc: 0.3227 - val_acc: 0.8550
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.2070 - orgCE: 0.8885 - myAcc: 0.3048 - acc: 0.8530 - val_loss: 4.4543 - val_orgCE: 0.9547 - val_myAcc: 0.3113 - val_acc: 0.8523
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.2081 - orgCE: 0.9073 - myAcc: 0.3064 - acc: 0.8501 - val_loss: 4.4056 - val_orgCE: 0.9388 - val_myAcc: 0.3111 - val_acc: 0.8528
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.1494 - orgCE: 0.8887 - myAcc: 0.3177 - acc: 0.8534 - val_loss: 4.3716 - val_orgCE: 0.9309 - val_myAcc: 0.3203 - val_acc: 0.8552
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.0979 - orgCE: 0.8687 - myAcc: 0.3203 - acc: 0.8549 - val_loss: 4.5104 - val_orgCE: 0.9694 - val_myAcc: 0.3230 - val_acc: 0.8544
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 4.1383 - orgCE: 0.8892 - myAcc: 0.3132 - acc: 0.8519 - val_loss: 4.3993 - val_orgCE: 0.9349 - val_myAcc: 0.3231 - val_acc: 0.8554
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.0453 - orgCE: 0.8541 - myAcc: 0.3293 - acc: 0.8570 - val_loss: 4.4416 - val_orgCE: 0.9646 - val_myAcc: 0.3157 - val_acc: 0.8500
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 4.0747 - orgCE: 0.8691 - myAcc: 0.3334 - acc: 0.8557 - val_loss: 4.4831 - val_orgCE: 0.9639 - val_myAcc: 0.3053 - val_acc: 0.8485
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 4.0133 - orgCE: 0.8518 - myAcc: 0.3299 - acc: 0.8554 - val_loss: 4.5036 - val_orgCE: 0.9575 - val_myAcc: 0.3161 - val_acc: 0.8512
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.9107 - orgCE: 0.8279 - myAcc: 0.3427 - acc: 0.8563 - val_loss: 4.3733 - val_orgCE: 0.9319 - val_myAcc: 0.3260 - val_acc: 0.8533
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.9335 - orgCE: 0.8319 - myAcc: 0.3444 - acc: 0.8578 - val_loss: 4.4082 - val_orgCE: 0.9183 - val_myAcc: 0.3076 - val_acc: 0.8468
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.8631 - orgCE: 0.8138 - myAcc: 0.3522 - acc: 0.8574 - val_loss: 4.4076 - val_orgCE: 0.9455 - val_myAcc: 0.3192 - val_acc: 0.8527
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.7891 - orgCE: 0.8005 - myAcc: 0.3620 - acc: 0.8611 - val_loss: 4.4410 - val_orgCE: 0.9696 - val_myAcc: 0.3226 - val_acc: 0.8489
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.8769 - orgCE: 0.8295 - myAcc: 0.3486 - acc: 0.8565 - val_loss: 4.3119 - val_orgCE: 0.9224 - val_myAcc: 0.3256 - val_acc: 0.8546
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.7692 - orgCE: 0.8101 - myAcc: 0.3604 - acc: 0.8573 - val_loss: 4.4883 - val_orgCE: 0.9587 - val_myAcc: 0.3179 - val_acc: 0.8521
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.6977 - orgCE: 0.7776 - myAcc: 0.3689 - acc: 0.8625 - val_loss: 4.3875 - val_orgCE: 0.9372 - val_myAcc: 0.3205 - val_acc: 0.8523
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.6841 - orgCE: 0.7721 - myAcc: 0.3679 - acc: 0.8611 - val_loss: 4.3070 - val_orgCE: 0.9025 - val_myAcc: 0.3234 - val_acc: 0.8544
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.6220 - orgCE: 0.7644 - myAcc: 0.3707 - acc: 0.8614 - val_loss: 4.3641 - val_orgCE: 0.9321 - val_myAcc: 0.2977 - val_acc: 0.8386
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.6891 - orgCE: 0.7650 - myAcc: 0.3686 - acc: 0.8642 - val_loss: 4.4764 - val_orgCE: 0.9330 - val_myAcc: 0.2928 - val_acc: 0.8428
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.6125 - orgCE: 0.7594 - myAcc: 0.3764 - acc: 0.8647 - val_loss: 4.4609 - val_orgCE: 0.9264 - val_myAcc: 0.3098 - val_acc: 0.8528
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.5680 - orgCE: 0.7488 - myAcc: 0.3867 - acc: 0.8673 - val_loss: 4.3741 - val_orgCE: 0.9549 - val_myAcc: 0.3158 - val_acc: 0.8474
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.6666 - orgCE: 0.8000 - myAcc: 0.3690 - acc: 0.8565 - val_loss: 4.3057 - val_orgCE: 0.9118 - val_myAcc: 0.3151 - val_acc: 0.8515
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.5808 - orgCE: 0.7634 - myAcc: 0.3819 - acc: 0.8631 - val_loss: 4.4217 - val_orgCE: 0.9280 - val_myAcc: 0.3077 - val_acc: 0.8525
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.5829 - orgCE: 0.7678 - myAcc: 0.3773 - acc: 0.8608 - val_loss: 4.2854 - val_orgCE: 0.8853 - val_myAcc: 0.3295 - val_acc: 0.8590
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.5368 - orgCE: 0.7547 - myAcc: 0.3789 - acc: 0.8620 - val_loss: 4.3301 - val_orgCE: 0.9120 - val_myAcc: 0.3179 - val_acc: 0.8550
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.4922 - orgCE: 0.7513 - myAcc: 0.3816 - acc: 0.8617 - val_loss: 4.4458 - val_orgCE: 0.9534 - val_myAcc: 0.3112 - val_acc: 0.8511
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4517 - orgCE: 0.7226 - myAcc: 0.3934 - acc: 0.8692 - val_loss: 4.4204 - val_orgCE: 0.9569 - val_myAcc: 0.3120 - val_acc: 0.8497
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4694 - orgCE: 0.7311 - myAcc: 0.3854 - acc: 0.8669 - val_loss: 4.5076 - val_orgCE: 0.9468 - val_myAcc: 0.3057 - val_acc: 0.8514
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4324 - orgCE: 0.7226 - myAcc: 0.3949 - acc: 0.8680 - val_loss: 4.5472 - val_orgCE: 0.9846 - val_myAcc: 0.3024 - val_acc: 0.8480
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4987 - orgCE: 0.7502 - myAcc: 0.3840 - acc: 0.8623 - val_loss: 4.3900 - val_orgCE: 0.9417 - val_myAcc: 0.3063 - val_acc: 0.8402
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.3956 - orgCE: 0.7149 - myAcc: 0.3976 - acc: 0.8668 - val_loss: 4.5285 - val_orgCE: 1.0266 - val_myAcc: 0.3026 - val_acc: 0.8386
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.4257 - orgCE: 0.7298 - myAcc: 0.3885 - acc: 0.8642 - val_loss: 4.5456 - val_orgCE: 0.9758 - val_myAcc: 0.2959 - val_acc: 0.8462
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.3848 - orgCE: 0.7305 - myAcc: 0.3945 - acc: 0.8645 - val_loss: 4.4359 - val_orgCE: 0.9483 - val_myAcc: 0.3097 - val_acc: 0.8474
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.3905 - orgCE: 0.7326 - myAcc: 0.3982 - acc: 0.8652 - val_loss: 4.6632 - val_orgCE: 1.0165 - val_myAcc: 0.2756 - val_acc: 0.8271
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.3528 - orgCE: 0.7178 - myAcc: 0.3970 - acc: 0.8639 - val_loss: 4.4767 - val_orgCE: 0.9491 - val_myAcc: 0.3131 - val_acc: 0.8486
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.3180 - orgCE: 0.7050 - myAcc: 0.4054 - acc: 0.8693 - val_loss: 4.5380 - val_orgCE: 0.9980 - val_myAcc: 0.2900 - val_acc: 0.8396
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.3142 - orgCE: 0.7068 - myAcc: 0.4058 - acc: 0.8678 - val_loss: 4.4340 - val_orgCE: 0.9205 - val_myAcc: 0.3225 - val_acc: 0.8572
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.2547 - orgCE: 0.6838 - myAcc: 0.4107 - acc: 0.8708 - val_loss: 4.4734 - val_orgCE: 0.9631 - val_myAcc: 0.3032 - val_acc: 0.8488
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.2289 - orgCE: 0.6876 - myAcc: 0.4091 - acc: 0.8702 - val_loss: 4.5450 - val_orgCE: 0.9477 - val_myAcc: 0.2940 - val_acc: 0.8399
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.2591 - orgCE: 0.6897 - myAcc: 0.4058 - acc: 0.8594 - val_loss: 4.4500 - val_orgCE: 0.9330 - val_myAcc: 0.3190 - val_acc: 0.8506
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.2852 - orgCE: 0.7013 - myAcc: 0.4037 - acc: 0.8682 - val_loss: 4.4268 - val_orgCE: 0.9251 - val_myAcc: 0.3229 - val_acc: 0.8555
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.2785 - orgCE: 0.7140 - myAcc: 0.4045 - acc: 0.8659 - val_loss: 4.5017 - val_orgCE: 0.9652 - val_myAcc: 0.3025 - val_acc: 0.8346
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1816 - orgCE: 0.6706 - myAcc: 0.4222 - acc: 0.8659 - val_loss: 4.4263 - val_orgCE: 0.9402 - val_myAcc: 0.3083 - val_acc: 0.8423
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1747 - orgCE: 0.6795 - myAcc: 0.4164 - acc: 0.8680 - val_loss: 4.5268 - val_orgCE: 0.9788 - val_myAcc: 0.3111 - val_acc: 0.8447
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.1912 - orgCE: 0.6811 - myAcc: 0.4089 - acc: 0.8673 - val_loss: 4.5309 - val_orgCE: 1.0096 - val_myAcc: 0.3064 - val_acc: 0.8438
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1655 - orgCE: 0.6708 - myAcc: 0.4180 - acc: 0.8723 - val_loss: 4.3847 - val_orgCE: 0.9346 - val_myAcc: 0.3105 - val_acc: 0.8507
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.1852 - orgCE: 0.6933 - myAcc: 0.4059 - acc: 0.8645 - val_loss: 4.5858 - val_orgCE: 1.0156 - val_myAcc: 0.2862 - val_acc: 0.8378
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1658 - orgCE: 0.6749 - myAcc: 0.4196 - acc: 0.8718 - val_loss: 4.5473 - val_orgCE: 0.9728 - val_myAcc: 0.2940 - val_acc: 0.8430
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1565 - orgCE: 0.6766 - myAcc: 0.4175 - acc: 0.8699 - val_loss: 4.5746 - val_orgCE: 0.9906 - val_myAcc: 0.2965 - val_acc: 0.8448
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1176 - orgCE: 0.6550 - myAcc: 0.4238 - acc: 0.8704 - val_loss: 4.6444 - val_orgCE: 1.0156 - val_myAcc: 0.3054 - val_acc: 0.8447
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0743 - orgCE: 0.6456 - myAcc: 0.4290 - acc: 0.8743 - val_loss: 4.4646 - val_orgCE: 0.9328 - val_myAcc: 0.3074 - val_acc: 0.8519
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.1126 - orgCE: 0.6678 - myAcc: 0.4163 - acc: 0.8670 - val_loss: 4.5067 - val_orgCE: 0.9445 - val_myAcc: 0.3172 - val_acc: 0.8521
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0687 - orgCE: 0.6482 - myAcc: 0.4302 - acc: 0.8738 - val_loss: 4.4822 - val_orgCE: 0.9537 - val_myAcc: 0.3151 - val_acc: 0.8483
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0379 - orgCE: 0.6397 - myAcc: 0.4320 - acc: 0.8698 - val_loss: 4.7268 - val_orgCE: 1.0141 - val_myAcc: 0.2899 - val_acc: 0.8422
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.0515 - orgCE: 0.6485 - myAcc: 0.4273 - acc: 0.8718 - val_loss: 4.5528 - val_orgCE: 0.9671 - val_myAcc: 0.3092 - val_acc: 0.8477
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0115 - orgCE: 0.6445 - myAcc: 0.4378 - acc: 0.8735 - val_loss: 4.5466 - val_orgCE: 0.9414 - val_myAcc: 0.3021 - val_acc: 0.8514
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.0797 - orgCE: 0.6628 - myAcc: 0.4243 - acc: 0.8701 - val_loss: 4.6020 - val_orgCE: 1.0121 - val_myAcc: 0.2984 - val_acc: 0.8306
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 3.0344 - orgCE: 0.6495 - myAcc: 0.4325 - acc: 0.8624 - val_loss: 4.7865 - val_orgCE: 1.0591 - val_myAcc: 0.2814 - val_acc: 0.8204
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9869 - orgCE: 0.6341 - myAcc: 0.4339 - acc: 0.8687 - val_loss: 4.5788 - val_orgCE: 0.9901 - val_myAcc: 0.2998 - val_acc: 0.8398
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0435 - orgCE: 0.6561 - myAcc: 0.4316 - acc: 0.8700 - val_loss: 4.5352 - val_orgCE: 0.9455 - val_myAcc: 0.3070 - val_acc: 0.8445
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0058 - orgCE: 0.6335 - myAcc: 0.4341 - acc: 0.8738 - val_loss: 4.6757 - val_orgCE: 0.9747 - val_myAcc: 0.2937 - val_acc: 0.8413
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 3.0115 - orgCE: 0.6430 - myAcc: 0.4311 - acc: 0.8643 - val_loss: 4.5064 - val_orgCE: 0.9292 - val_myAcc: 0.3094 - val_acc: 0.8511
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.9775 - orgCE: 0.6436 - myAcc: 0.4370 - acc: 0.8694 - val_loss: 4.6303 - val_orgCE: 1.0093 - val_myAcc: 0.3038 - val_acc: 0.8415
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.9545 - orgCE: 0.6293 - myAcc: 0.4345 - acc: 0.8684 - val_loss: 4.6021 - val_orgCE: 0.9812 - val_myAcc: 0.2983 - val_acc: 0.8409
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9641 - orgCE: 0.6249 - myAcc: 0.4403 - acc: 0.8560 - val_loss: 4.5804 - val_orgCE: 0.9677 - val_myAcc: 0.3113 - val_acc: 0.8484
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9904 - orgCE: 0.6473 - myAcc: 0.4321 - acc: 0.8677 - val_loss: 4.6974 - val_orgCE: 1.0171 - val_myAcc: 0.2918 - val_acc: 0.8019
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.9444 - orgCE: 0.6312 - myAcc: 0.4429 - acc: 0.8434 - val_loss: 4.6037 - val_orgCE: 0.9767 - val_myAcc: 0.3038 - val_acc: 0.8473
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9749 - orgCE: 0.6435 - myAcc: 0.4368 - acc: 0.8663 - val_loss: 4.6515 - val_orgCE: 1.0121 - val_myAcc: 0.2949 - val_acc: 0.8402
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8403 - orgCE: 0.5888 - myAcc: 0.4528 - acc: 0.8765 - val_loss: 4.7551 - val_orgCE: 1.0031 - val_myAcc: 0.2876 - val_acc: 0.8451
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.9542 - orgCE: 0.6414 - myAcc: 0.4392 - acc: 0.8610 - val_loss: 4.7799 - val_orgCE: 1.0149 - val_myAcc: 0.2777 - val_acc: 0.8233
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.8976 - orgCE: 0.6211 - myAcc: 0.4484 - acc: 0.8699 - val_loss: 4.6001 - val_orgCE: 0.9839 - val_myAcc: 0.3113 - val_acc: 0.8480
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.8657 - orgCE: 0.6108 - myAcc: 0.4439 - acc: 0.8566 - val_loss: 4.7576 - val_orgCE: 1.0201 - val_myAcc: 0.2924 - val_acc: 0.8330
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8396 - orgCE: 0.6042 - myAcc: 0.4528 - acc: 0.8694 - val_loss: 4.6601 - val_orgCE: 0.9925 - val_myAcc: 0.2897 - val_acc: 0.8414
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8798 - orgCE: 0.6131 - myAcc: 0.4496 - acc: 0.8722 - val_loss: 4.5922 - val_orgCE: 0.9787 - val_myAcc: 0.3067 - val_acc: 0.8457
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.8687 - orgCE: 0.6107 - myAcc: 0.4485 - acc: 0.8683 - val_loss: 4.7882 - val_orgCE: 1.0152 - val_myAcc: 0.2729 - val_acc: 0.8347
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8623 - orgCE: 0.6068 - myAcc: 0.4493 - acc: 0.8702 - val_loss: 4.5476 - val_orgCE: 0.9520 - val_myAcc: 0.3042 - val_acc: 0.8472
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8444 - orgCE: 0.5965 - myAcc: 0.4527 - acc: 0.8712 - val_loss: 4.6316 - val_orgCE: 1.0011 - val_myAcc: 0.2975 - val_acc: 0.8423
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7813 - orgCE: 0.5909 - myAcc: 0.4549 - acc: 0.8734 - val_loss: 4.8299 - val_orgCE: 1.0242 - val_myAcc: 0.2818 - val_acc: 0.8419
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8273 - orgCE: 0.6069 - myAcc: 0.4549 - acc: 0.8682 - val_loss: 4.6940 - val_orgCE: 0.9921 - val_myAcc: 0.2946 - val_acc: 0.8428
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8139 - orgCE: 0.5978 - myAcc: 0.4508 - acc: 0.8726 - val_loss: 4.6922 - val_orgCE: 1.0199 - val_myAcc: 0.2782 - val_acc: 0.8343
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8169 - orgCE: 0.6075 - myAcc: 0.4515 - acc: 0.8606 - val_loss: 4.7489 - val_orgCE: 1.0099 - val_myAcc: 0.2866 - val_acc: 0.8410
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8286 - orgCE: 0.6094 - myAcc: 0.4540 - acc: 0.8599 - val_loss: 4.8624 - val_orgCE: 1.0417 - val_myAcc: 0.2776 - val_acc: 0.8267
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7375 - orgCE: 0.5807 - myAcc: 0.4658 - acc: 0.8739 - val_loss: 4.7283 - val_orgCE: 1.0201 - val_myAcc: 0.2935 - val_acc: 0.8423
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.7769 - orgCE: 0.5952 - myAcc: 0.4638 - acc: 0.8635 - val_loss: 4.5621 - val_orgCE: 0.9395 - val_myAcc: 0.3228 - val_acc: 0.8566
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7963 - orgCE: 0.6092 - myAcc: 0.4532 - acc: 0.8627 - val_loss: 4.6364 - val_orgCE: 0.9661 - val_myAcc: 0.3099 - val_acc: 0.8518
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7500 - orgCE: 0.5824 - myAcc: 0.4613 - acc: 0.8732 - val_loss: 4.6146 - val_orgCE: 0.9467 - val_myAcc: 0.3065 - val_acc: 0.8518
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7597 - orgCE: 0.5944 - myAcc: 0.4627 - acc: 0.8715 - val_loss: 4.6779 - val_orgCE: 0.9691 - val_myAcc: 0.2897 - val_acc: 0.8357
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.8097 - orgCE: 0.6112 - myAcc: 0.4574 - acc: 0.8604 - val_loss: 4.7080 - val_orgCE: 0.9982 - val_myAcc: 0.3059 - val_acc: 0.8474
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7921 - orgCE: 0.6006 - myAcc: 0.4516 - acc: 0.8666 - val_loss: 4.7958 - val_orgCE: 1.0199 - val_myAcc: 0.2976 - val_acc: 0.8452


# python3 bleu_eval.py sample_output_testset.txt
Originally, average bleu score is 0.2927853226653483
By another method, average bleu score is 0.6517729167254562
