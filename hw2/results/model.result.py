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

* Has loaded existed model. *

* Epoch 1/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 47s - loss: 2.7320 - orgCE: 0.5773 - myAcc: 0.4668 - acc: 0.8720 - val_loss: 4.7708 - val_orgCE: 1.0206 - val_myAcc: 0.2893 - val_acc: 0.8310
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7377 - orgCE: 0.5876 - myAcc: 0.4665 - acc: 0.8589 - val_loss: 4.9573 - val_orgCE: 1.0613 - val_myAcc: 0.2777 - val_acc: 0.8342
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6782 - orgCE: 0.5701 - myAcc: 0.4772 - acc: 0.8709 - val_loss: 4.6782 - val_orgCE: 0.9994 - val_myAcc: 0.3017 - val_acc: 0.8458
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7286 - orgCE: 0.5830 - myAcc: 0.4675 - acc: 0.8618 - val_loss: 4.7556 - val_orgCE: 0.9959 - val_myAcc: 0.2820 - val_acc: 0.8241
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6947 - orgCE: 0.5810 - myAcc: 0.4613 - acc: 0.8609 - val_loss: 4.7208 - val_orgCE: 1.0432 - val_myAcc: 0.2945 - val_acc: 0.8291
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7081 - orgCE: 0.5728 - myAcc: 0.4697 - acc: 0.8652 - val_loss: 4.9890 - val_orgCE: 1.0668 - val_myAcc: 0.2775 - val_acc: 0.8225
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.7101 - orgCE: 0.5774 - myAcc: 0.4719 - acc: 0.8608 - val_loss: 4.7665 - val_orgCE: 1.0080 - val_myAcc: 0.2960 - val_acc: 0.7966
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6525 - orgCE: 0.5614 - myAcc: 0.4747 - acc: 0.8577 - val_loss: 4.6888 - val_orgCE: 1.0146 - val_myAcc: 0.3096 - val_acc: 0.8467
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6490 - orgCE: 0.5641 - myAcc: 0.4684 - acc: 0.8636 - val_loss: 4.9170 - val_orgCE: 1.0693 - val_myAcc: 0.2882 - val_acc: 0.8385
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6864 - orgCE: 0.5711 - myAcc: 0.4698 - acc: 0.8698 - val_loss: 4.7799 - val_orgCE: 1.0153 - val_myAcc: 0.3118 - val_acc: 0.8474
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6598 - orgCE: 0.5744 - myAcc: 0.4746 - acc: 0.8634 - val_loss: 4.7763 - val_orgCE: 1.0341 - val_myAcc: 0.2776 - val_acc: 0.8137
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6282 - orgCE: 0.5644 - myAcc: 0.4747 - acc: 0.8671 - val_loss: 4.7619 - val_orgCE: 1.0300 - val_myAcc: 0.2958 - val_acc: 0.8378
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6892 - orgCE: 0.5817 - myAcc: 0.4716 - acc: 0.8639 - val_loss: 4.8257 - val_orgCE: 1.0454 - val_myAcc: 0.2946 - val_acc: 0.8262
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6691 - orgCE: 0.5772 - myAcc: 0.4750 - acc: 0.8496 - val_loss: 4.8820 - val_orgCE: 1.0733 - val_myAcc: 0.2950 - val_acc: 0.8322
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6403 - orgCE: 0.5582 - myAcc: 0.4794 - acc: 0.8623 - val_loss: 4.8145 - val_orgCE: 1.0249 - val_myAcc: 0.2914 - val_acc: 0.8439
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6392 - orgCE: 0.5620 - myAcc: 0.4771 - acc: 0.8521 - val_loss: 4.9097 - val_orgCE: 1.0537 - val_myAcc: 0.2722 - val_acc: 0.7990
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5805 - orgCE: 0.5459 - myAcc: 0.4827 - acc: 0.8500 - val_loss: 4.7834 - val_orgCE: 1.0186 - val_myAcc: 0.2920 - val_acc: 0.8373
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6226 - orgCE: 0.5637 - myAcc: 0.4750 - acc: 0.8433 - val_loss: 4.7935 - val_orgCE: 1.0126 - val_myAcc: 0.2941 - val_acc: 0.8463
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5716 - orgCE: 0.5451 - myAcc: 0.4882 - acc: 0.8332 - val_loss: 4.8587 - val_orgCE: 1.0625 - val_myAcc: 0.2884 - val_acc: 0.6632
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6341 - orgCE: 0.5687 - myAcc: 0.4798 - acc: 0.8397 - val_loss: 4.8064 - val_orgCE: 1.0235 - val_myAcc: 0.2959 - val_acc: 0.8344
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.5927 - orgCE: 0.5573 - myAcc: 0.4770 - acc: 0.8467 - val_loss: 4.8825 - val_orgCE: 1.0402 - val_myAcc: 0.3005 - val_acc: 0.8239
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6244 - orgCE: 0.5575 - myAcc: 0.4779 - acc: 0.8388 - val_loss: 4.7488 - val_orgCE: 1.0471 - val_myAcc: 0.3014 - val_acc: 0.8410
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.6114 - orgCE: 0.5578 - myAcc: 0.4801 - acc: 0.8481 - val_loss: 4.7613 - val_orgCE: 1.0118 - val_myAcc: 0.2954 - val_acc: 0.8434
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5581 - orgCE: 0.5400 - myAcc: 0.4892 - acc: 0.8474 - val_loss: 4.8295 - val_orgCE: 1.0461 - val_myAcc: 0.3075 - val_acc: 0.8379
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5945 - orgCE: 0.5604 - myAcc: 0.4762 - acc: 0.8541 - val_loss: 5.0860 - val_orgCE: 1.0895 - val_myAcc: 0.2748 - val_acc: 0.7197
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5702 - orgCE: 0.5551 - myAcc: 0.4833 - acc: 0.8205 - val_loss: 4.7570 - val_orgCE: 1.0294 - val_myAcc: 0.3042 - val_acc: 0.8419
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5948 - orgCE: 0.5606 - myAcc: 0.4799 - acc: 0.8554 - val_loss: 4.8880 - val_orgCE: 1.0593 - val_myAcc: 0.2889 - val_acc: 0.8397
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5603 - orgCE: 0.5449 - myAcc: 0.4892 - acc: 0.8567 - val_loss: 4.8523 - val_orgCE: 1.0584 - val_myAcc: 0.2909 - val_acc: 0.7688
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5410 - orgCE: 0.5419 - myAcc: 0.4904 - acc: 0.8409 - val_loss: 4.7470 - val_orgCE: 1.0050 - val_myAcc: 0.3063 - val_acc: 0.8461
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5090 - orgCE: 0.5308 - myAcc: 0.4946 - acc: 0.8547 - val_loss: 4.9407 - val_orgCE: 1.0709 - val_myAcc: 0.2962 - val_acc: 0.8347
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4839 - orgCE: 0.5240 - myAcc: 0.4951 - acc: 0.8676 - val_loss: 4.8831 - val_orgCE: 1.0729 - val_myAcc: 0.3037 - val_acc: 0.8358
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5377 - orgCE: 0.5398 - myAcc: 0.4882 - acc: 0.8515 - val_loss: 4.9663 - val_orgCE: 1.0461 - val_myAcc: 0.2981 - val_acc: 0.8436
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.5400 - orgCE: 0.5454 - myAcc: 0.4893 - acc: 0.8358 - val_loss: 4.9322 - val_orgCE: 1.0680 - val_myAcc: 0.2843 - val_acc: 0.7406
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.5230 - orgCE: 0.5361 - myAcc: 0.4891 - acc: 0.8429 - val_loss: 5.0055 - val_orgCE: 1.0801 - val_myAcc: 0.2750 - val_acc: 0.8104
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4997 - orgCE: 0.5322 - myAcc: 0.4921 - acc: 0.8437 - val_loss: 4.8161 - val_orgCE: 1.0383 - val_myAcc: 0.3059 - val_acc: 0.8442
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4896 - orgCE: 0.5267 - myAcc: 0.4985 - acc: 0.8532 - val_loss: 5.0218 - val_orgCE: 1.0618 - val_myAcc: 0.2830 - val_acc: 0.7603
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4969 - orgCE: 0.5279 - myAcc: 0.4948 - acc: 0.8562 - val_loss: 4.8429 - val_orgCE: 1.0179 - val_myAcc: 0.2963 - val_acc: 0.8449
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4965 - orgCE: 0.5268 - myAcc: 0.4929 - acc: 0.8696 - val_loss: 4.9299 - val_orgCE: 1.0844 - val_myAcc: 0.2970 - val_acc: 0.7017
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.4720 - orgCE: 0.5194 - myAcc: 0.5000 - acc: 0.8122 - val_loss: 4.8230 - val_orgCE: 1.0320 - val_myAcc: 0.2979 - val_acc: 0.8314
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4648 - orgCE: 0.5270 - myAcc: 0.4943 - acc: 0.8544 - val_loss: 4.9524 - val_orgCE: 1.0800 - val_myAcc: 0.2901 - val_acc: 0.7950
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.5216 - orgCE: 0.5429 - myAcc: 0.4947 - acc: 0.8431 - val_loss: 4.9847 - val_orgCE: 1.0708 - val_myAcc: 0.2866 - val_acc: 0.8353
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.5306 - orgCE: 0.5485 - myAcc: 0.4887 - acc: 0.8482 - val_loss: 4.9742 - val_orgCE: 1.0875 - val_myAcc: 0.2928 - val_acc: 0.8405
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4397 - orgCE: 0.5211 - myAcc: 0.5055 - acc: 0.8558 - val_loss: 4.9323 - val_orgCE: 1.0337 - val_myAcc: 0.2997 - val_acc: 0.8461
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4934 - orgCE: 0.5426 - myAcc: 0.4963 - acc: 0.8360 - val_loss: 4.8103 - val_orgCE: 1.0496 - val_myAcc: 0.3035 - val_acc: 0.7971
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4648 - orgCE: 0.5305 - myAcc: 0.4945 - acc: 0.8235 - val_loss: 5.0269 - val_orgCE: 1.1151 - val_myAcc: 0.2917 - val_acc: 0.8216
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4441 - orgCE: 0.5167 - myAcc: 0.5025 - acc: 0.8447 - val_loss: 4.9157 - val_orgCE: 1.0501 - val_myAcc: 0.3012 - val_acc: 0.8312
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4577 - orgCE: 0.5322 - myAcc: 0.5024 - acc: 0.8421 - val_loss: 4.7875 - val_orgCE: 1.0000 - val_myAcc: 0.2974 - val_acc: 0.8208
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4604 - orgCE: 0.5242 - myAcc: 0.4998 - acc: 0.8292 - val_loss: 5.0027 - val_orgCE: 1.1212 - val_myAcc: 0.2839 - val_acc: 0.8056
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4857 - orgCE: 0.5261 - myAcc: 0.5022 - acc: 0.8652 - val_loss: 4.8761 - val_orgCE: 1.0469 - val_myAcc: 0.2830 - val_acc: 0.8182
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4283 - orgCE: 0.5214 - myAcc: 0.5042 - acc: 0.8119 - val_loss: 4.9090 - val_orgCE: 1.0493 - val_myAcc: 0.2930 - val_acc: 0.8155
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4475 - orgCE: 0.5213 - myAcc: 0.5090 - acc: 0.8566 - val_loss: 4.9163 - val_orgCE: 1.0624 - val_myAcc: 0.2968 - val_acc: 0.8057
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4400 - orgCE: 0.5216 - myAcc: 0.4998 - acc: 0.8428 - val_loss: 5.0436 - val_orgCE: 1.1034 - val_myAcc: 0.2867 - val_acc: 0.8361
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.3954 - orgCE: 0.5082 - myAcc: 0.5050 - acc: 0.8556 - val_loss: 4.9190 - val_orgCE: 1.0476 - val_myAcc: 0.2980 - val_acc: 0.8456
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4417 - orgCE: 0.5228 - myAcc: 0.4999 - acc: 0.8486 - val_loss: 4.9259 - val_orgCE: 1.0408 - val_myAcc: 0.2989 - val_acc: 0.8146
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4396 - orgCE: 0.5256 - myAcc: 0.5070 - acc: 0.8152 - val_loss: 5.0551 - val_orgCE: 1.0923 - val_myAcc: 0.2865 - val_acc: 0.8133
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4282 - orgCE: 0.5173 - myAcc: 0.5083 - acc: 0.8490 - val_loss: 4.9830 - val_orgCE: 1.0744 - val_myAcc: 0.2869 - val_acc: 0.8212
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.4251 - orgCE: 0.5201 - myAcc: 0.5029 - acc: 0.8135 - val_loss: 4.8916 - val_orgCE: 1.0430 - val_myAcc: 0.2833 - val_acc: 0.7542
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3689 - orgCE: 0.5036 - myAcc: 0.5153 - acc: 0.8182 - val_loss: 4.8538 - val_orgCE: 1.0176 - val_myAcc: 0.3050 - val_acc: 0.8149
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.4064 - orgCE: 0.5140 - myAcc: 0.5062 - acc: 0.8341 - val_loss: 4.7987 - val_orgCE: 1.0031 - val_myAcc: 0.3115 - val_acc: 0.8439
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.3727 - orgCE: 0.5032 - myAcc: 0.5124 - acc: 0.8543 - val_loss: 5.0395 - val_orgCE: 1.1319 - val_myAcc: 0.2915 - val_acc: 0.8310
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.3810 - orgCE: 0.5064 - myAcc: 0.5131 - acc: 0.8652 - val_loss: 5.0417 - val_orgCE: 1.0579 - val_myAcc: 0.2885 - val_acc: 0.8272
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.4324 - orgCE: 0.5243 - myAcc: 0.5035 - acc: 0.8533 - val_loss: 4.9498 - val_orgCE: 1.0450 - val_myAcc: 0.2933 - val_acc: 0.8141
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3695 - orgCE: 0.5046 - myAcc: 0.5150 - acc: 0.8524 - val_loss: 5.1177 - val_orgCE: 1.0865 - val_myAcc: 0.2785 - val_acc: 0.8197
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3832 - orgCE: 0.5062 - myAcc: 0.5159 - acc: 0.8320 - val_loss: 5.1004 - val_orgCE: 1.1032 - val_myAcc: 0.2703 - val_acc: 0.7348
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.4036 - orgCE: 0.5259 - myAcc: 0.5054 - acc: 0.7976 - val_loss: 4.8841 - val_orgCE: 1.0263 - val_myAcc: 0.3013 - val_acc: 0.8269
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.3311 - orgCE: 0.4919 - myAcc: 0.5170 - acc: 0.8523 - val_loss: 5.1313 - val_orgCE: 1.1310 - val_myAcc: 0.2758 - val_acc: 0.7506
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3838 - orgCE: 0.5168 - myAcc: 0.5102 - acc: 0.8045 - val_loss: 4.9362 - val_orgCE: 1.0492 - val_myAcc: 0.2974 - val_acc: 0.7400
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3825 - orgCE: 0.5016 - myAcc: 0.5102 - acc: 0.8210 - val_loss: 5.0040 - val_orgCE: 1.0420 - val_myAcc: 0.2841 - val_acc: 0.7005
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.3317 - orgCE: 0.4999 - myAcc: 0.5155 - acc: 0.7988 - val_loss: 4.8534 - val_orgCE: 1.0417 - val_myAcc: 0.3067 - val_acc: 0.7554
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.3504 - orgCE: 0.4984 - myAcc: 0.5132 - acc: 0.8087 - val_loss: 5.1064 - val_orgCE: 1.1123 - val_myAcc: 0.2644 - val_acc: 0.7655
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.3859 - orgCE: 0.5143 - myAcc: 0.5083 - acc: 0.8155 - val_loss: 4.9781 - val_orgCE: 1.0285 - val_myAcc: 0.2986 - val_acc: 0.8279
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.3905 - orgCE: 0.5202 - myAcc: 0.5068 - acc: 0.7828 - val_loss: 4.9746 - val_orgCE: 1.0501 - val_myAcc: 0.2925 - val_acc: 0.8152
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3242 - orgCE: 0.4956 - myAcc: 0.5214 - acc: 0.8231 - val_loss: 5.0315 - val_orgCE: 1.0645 - val_myAcc: 0.2871 - val_acc: 0.7915
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.3347 - orgCE: 0.4989 - myAcc: 0.5221 - acc: 0.8199 - val_loss: 4.9462 - val_orgCE: 1.0902 - val_myAcc: 0.3033 - val_acc: 0.7980
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3254 - orgCE: 0.4939 - myAcc: 0.5244 - acc: 0.8317 - val_loss: 4.9993 - val_orgCE: 1.0590 - val_myAcc: 0.2939 - val_acc: 0.7685
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 46s - loss: 2.3000 - orgCE: 0.4868 - myAcc: 0.5238 - acc: 0.8089 - val_loss: 5.0144 - val_orgCE: 1.0821 - val_myAcc: 0.2979 - val_acc: 0.7778
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3471 - orgCE: 0.5069 - myAcc: 0.5116 - acc: 0.8187 - val_loss: 5.0145 - val_orgCE: 1.0655 - val_myAcc: 0.2932 - val_acc: 0.6974
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3622 - orgCE: 0.5112 - myAcc: 0.5097 - acc: 0.8044 - val_loss: 4.9976 - val_orgCE: 1.0451 - val_myAcc: 0.2972 - val_acc: 0.6030
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3838 - orgCE: 0.5080 - myAcc: 0.5100 - acc: 0.7810 - val_loss: 4.9622 - val_orgCE: 1.0554 - val_myAcc: 0.2992 - val_acc: 0.7571
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2915 - orgCE: 0.4801 - myAcc: 0.5238 - acc: 0.8125 - val_loss: 4.9456 - val_orgCE: 1.0660 - val_myAcc: 0.2977 - val_acc: 0.7234
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2847 - orgCE: 0.4863 - myAcc: 0.5248 - acc: 0.8441 - val_loss: 5.0646 - val_orgCE: 1.0710 - val_myAcc: 0.2977 - val_acc: 0.7978
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3196 - orgCE: 0.4935 - myAcc: 0.5198 - acc: 0.8246 - val_loss: 5.0015 - val_orgCE: 1.1020 - val_myAcc: 0.2822 - val_acc: 0.8288
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3538 - orgCE: 0.5087 - myAcc: 0.5161 - acc: 0.8012 - val_loss: 4.9794 - val_orgCE: 1.0781 - val_myAcc: 0.3000 - val_acc: 0.8306
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2905 - orgCE: 0.4881 - myAcc: 0.5228 - acc: 0.8131 - val_loss: 5.0446 - val_orgCE: 1.0700 - val_myAcc: 0.2961 - val_acc: 0.8320
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.2972 - orgCE: 0.4880 - myAcc: 0.5269 - acc: 0.8260 - val_loss: 5.0934 - val_orgCE: 1.1053 - val_myAcc: 0.2850 - val_acc: 0.7511
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3267 - orgCE: 0.4971 - myAcc: 0.5161 - acc: 0.8114 - val_loss: 4.9541 - val_orgCE: 1.0927 - val_myAcc: 0.2986 - val_acc: 0.8278
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2847 - orgCE: 0.4909 - myAcc: 0.5219 - acc: 0.8443 - val_loss: 5.1523 - val_orgCE: 1.1373 - val_myAcc: 0.2774 - val_acc: 0.8287
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2248 - orgCE: 0.4612 - myAcc: 0.5328 - acc: 0.8642 - val_loss: 5.1901 - val_orgCE: 1.1274 - val_myAcc: 0.2868 - val_acc: 0.7929
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2646 - orgCE: 0.4777 - myAcc: 0.5302 - acc: 0.8286 - val_loss: 5.0517 - val_orgCE: 1.0877 - val_myAcc: 0.2950 - val_acc: 0.8262
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 44s - loss: 2.3095 - orgCE: 0.4956 - myAcc: 0.5201 - acc: 0.8120 - val_loss: 4.8528 - val_orgCE: 1.0310 - val_myAcc: 0.3042 - val_acc: 0.7896
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3345 - orgCE: 0.5050 - myAcc: 0.5153 - acc: 0.7829 - val_loss: 5.0946 - val_orgCE: 1.1022 - val_myAcc: 0.2867 - val_acc: 0.8121
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3133 - orgCE: 0.5003 - myAcc: 0.5151 - acc: 0.8445 - val_loss: 4.9022 - val_orgCE: 1.0350 - val_myAcc: 0.3046 - val_acc: 0.8399
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2430 - orgCE: 0.4776 - myAcc: 0.5251 - acc: 0.8161 - val_loss: 4.9874 - val_orgCE: 1.0532 - val_myAcc: 0.2999 - val_acc: 0.7805
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2643 - orgCE: 0.4818 - myAcc: 0.5312 - acc: 0.8278 - val_loss: 5.1994 - val_orgCE: 1.1165 - val_myAcc: 0.2772 - val_acc: 0.5177
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.3088 - orgCE: 0.4995 - myAcc: 0.5160 - acc: 0.7027 - val_loss: 5.0046 - val_orgCE: 1.0753 - val_myAcc: 0.2933 - val_acc: 0.8216
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2899 - orgCE: 0.4840 - myAcc: 0.5231 - acc: 0.8104 - val_loss: 5.1001 - val_orgCE: 1.1250 - val_myAcc: 0.2869 - val_acc: 0.6144
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2648 - orgCE: 0.4832 - myAcc: 0.5293 - acc: 0.7556 - val_loss: 4.9796 - val_orgCE: 1.0569 - val_myAcc: 0.2989 - val_acc: 0.8437
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2757 - orgCE: 0.4881 - myAcc: 0.5296 - acc: 0.8139 - val_loss: 5.0859 - val_orgCE: 1.1018 - val_myAcc: 0.2797 - val_acc: 0.7457
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2323 - orgCE: 0.4768 - myAcc: 0.5362 - acc: 0.7645 - val_loss: 4.8739 - val_orgCE: 1.0165 - val_myAcc: 0.3074 - val_acc: 0.8467
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 45s - loss: 2.2322 - orgCE: 0.4723 - myAcc: 0.5303 - acc: 0.8441 - val_loss: 4.9033 - val_orgCE: 1.0094 - val_myAcc: 0.3002 - val_acc: 0.8317


# python3 bleu_eval.py sample_output_testset.txt
Originally, average bleu score is 0.2906356392504971
By another method, average bleu score is 0.6445548993290231
