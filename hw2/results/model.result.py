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
1160/1160 [==============================] - 85s - loss: 2.5469 - orgCE: 2.5469 - myAcc: 0.7674 - acc: 0.7674 - val_loss: 1.5418 - val_orgCE: 1.5418 - val_myAcc: 0.8046 - val_acc: 0.8046
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.3224 - orgCE: 1.3224 - myAcc: 0.8132 - acc: 0.8132 - val_loss: 1.1923 - val_orgCE: 1.1923 - val_myAcc: 0.8155 - val_acc: 0.8155
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.1907 - orgCE: 1.1907 - myAcc: 0.8272 - acc: 0.8272 - val_loss: 1.1409 - val_orgCE: 1.1409 - val_myAcc: 0.8394 - val_acc: 0.8394
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.1684 - orgCE: 1.1684 - myAcc: 0.8324 - acc: 0.8324 - val_loss: 1.1472 - val_orgCE: 1.1472 - val_myAcc: 0.8360 - val_acc: 0.8360
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.1666 - orgCE: 1.1666 - myAcc: 0.8357 - acc: 0.8357 - val_loss: 1.0769 - val_orgCE: 1.0769 - val_myAcc: 0.8492 - val_acc: 0.8492
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.1136 - orgCE: 1.1136 - myAcc: 0.8422 - acc: 0.8422 - val_loss: 1.1093 - val_orgCE: 1.1093 - val_myAcc: 0.8449 - val_acc: 0.8449
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0987 - orgCE: 1.0987 - myAcc: 0.8432 - acc: 0.8432 - val_loss: 1.1722 - val_orgCE: 1.1722 - val_myAcc: 0.8447 - val_acc: 0.8447
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0568 - orgCE: 1.0568 - myAcc: 0.8515 - acc: 0.8515 - val_loss: 1.1208 - val_orgCE: 1.1208 - val_myAcc: 0.8485 - val_acc: 0.8485
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0600 - orgCE: 1.0600 - myAcc: 0.8508 - acc: 0.8508 - val_loss: 1.1084 - val_orgCE: 1.1084 - val_myAcc: 0.8501 - val_acc: 0.8501
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0683 - orgCE: 1.0683 - myAcc: 0.8492 - acc: 0.8492 - val_loss: 1.0448 - val_orgCE: 1.0448 - val_myAcc: 0.8549 - val_acc: 0.8549
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0659 - orgCE: 1.0659 - myAcc: 0.8498 - acc: 0.8498 - val_loss: 1.1192 - val_orgCE: 1.1192 - val_myAcc: 0.8468 - val_acc: 0.8468
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0305 - orgCE: 1.0305 - myAcc: 0.8527 - acc: 0.8527 - val_loss: 1.0660 - val_orgCE: 1.0660 - val_myAcc: 0.8509 - val_acc: 0.8509
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0216 - orgCE: 1.0216 - myAcc: 0.8516 - acc: 0.8516 - val_loss: 1.1147 - val_orgCE: 1.1147 - val_myAcc: 0.8458 - val_acc: 0.8458
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0365 - orgCE: 1.0365 - myAcc: 0.8509 - acc: 0.8509 - val_loss: 1.1233 - val_orgCE: 1.1233 - val_myAcc: 0.8452 - val_acc: 0.8452
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9979 - orgCE: 0.9979 - myAcc: 0.8538 - acc: 0.8538 - val_loss: 1.0312 - val_orgCE: 1.0312 - val_myAcc: 0.8549 - val_acc: 0.8549
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0371 - orgCE: 1.0371 - myAcc: 0.8493 - acc: 0.8493 - val_loss: 0.9673 - val_orgCE: 0.9673 - val_myAcc: 0.8598 - val_acc: 0.8598
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0026 - orgCE: 1.0026 - myAcc: 0.8512 - acc: 0.8512 - val_loss: 0.9801 - val_orgCE: 0.9801 - val_myAcc: 0.8608 - val_acc: 0.8608
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0012 - orgCE: 1.0012 - myAcc: 0.8505 - acc: 0.8505 - val_loss: 1.1125 - val_orgCE: 1.1125 - val_myAcc: 0.8470 - val_acc: 0.8470
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9921 - orgCE: 0.9921 - myAcc: 0.8520 - acc: 0.8520 - val_loss: 1.0352 - val_orgCE: 1.0352 - val_myAcc: 0.8530 - val_acc: 0.8530
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 1.0050 - orgCE: 1.0050 - myAcc: 0.8507 - acc: 0.8507 - val_loss: 1.0994 - val_orgCE: 1.0994 - val_myAcc: 0.8474 - val_acc: 0.8474
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9877 - orgCE: 0.9877 - myAcc: 0.8503 - acc: 0.8503 - val_loss: 1.0480 - val_orgCE: 1.0480 - val_myAcc: 0.8512 - val_acc: 0.8512
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9780 - orgCE: 0.9780 - myAcc: 0.8520 - acc: 0.8520 - val_loss: 1.1198 - val_orgCE: 1.1198 - val_myAcc: 0.8470 - val_acc: 0.8470
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9661 - orgCE: 0.9661 - myAcc: 0.8534 - acc: 0.8534 - val_loss: 1.1061 - val_orgCE: 1.1061 - val_myAcc: 0.8463 - val_acc: 0.8463
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9453 - orgCE: 0.9453 - myAcc: 0.8537 - acc: 0.8537 - val_loss: 1.1140 - val_orgCE: 1.1140 - val_myAcc: 0.8427 - val_acc: 0.8427
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9608 - orgCE: 0.9608 - myAcc: 0.8496 - acc: 0.8496 - val_loss: 0.9898 - val_orgCE: 0.9898 - val_myAcc: 0.8634 - val_acc: 0.8634
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9384 - orgCE: 0.9384 - myAcc: 0.8515 - acc: 0.8515 - val_loss: 1.0740 - val_orgCE: 1.0740 - val_myAcc: 0.8486 - val_acc: 0.8486
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9240 - orgCE: 0.9240 - myAcc: 0.8551 - acc: 0.8551 - val_loss: 1.0398 - val_orgCE: 1.0398 - val_myAcc: 0.8541 - val_acc: 0.8541
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9180 - orgCE: 0.9180 - myAcc: 0.8552 - acc: 0.8552 - val_loss: 1.1410 - val_orgCE: 1.1410 - val_myAcc: 0.8509 - val_acc: 0.8509
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9270 - orgCE: 0.9270 - myAcc: 0.8525 - acc: 0.8525 - val_loss: 1.1530 - val_orgCE: 1.1530 - val_myAcc: 0.8451 - val_acc: 0.8451
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.9274 - orgCE: 0.9274 - myAcc: 0.8522 - acc: 0.8522 - val_loss: 1.1456 - val_orgCE: 1.1456 - val_myAcc: 0.8476 - val_acc: 0.8476
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8936 - orgCE: 0.8936 - myAcc: 0.8568 - acc: 0.8568 - val_loss: 1.0763 - val_orgCE: 1.0763 - val_myAcc: 0.8493 - val_acc: 0.8493
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8925 - orgCE: 0.8925 - myAcc: 0.8561 - acc: 0.8561 - val_loss: 1.0946 - val_orgCE: 1.0946 - val_myAcc: 0.8526 - val_acc: 0.8526
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8729 - orgCE: 0.8729 - myAcc: 0.8571 - acc: 0.8571 - val_loss: 1.1825 - val_orgCE: 1.1825 - val_myAcc: 0.8421 - val_acc: 0.8421
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8377 - orgCE: 0.8377 - myAcc: 0.8625 - acc: 0.8625 - val_loss: 1.2127 - val_orgCE: 1.2127 - val_myAcc: 0.8461 - val_acc: 0.8461
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8417 - orgCE: 0.8417 - myAcc: 0.8613 - acc: 0.8613 - val_loss: 1.0683 - val_orgCE: 1.0683 - val_myAcc: 0.8522 - val_acc: 0.8522
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8310 - orgCE: 0.8310 - myAcc: 0.8621 - acc: 0.8621 - val_loss: 1.0263 - val_orgCE: 1.0263 - val_myAcc: 0.8588 - val_acc: 0.8588
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8472 - orgCE: 0.8472 - myAcc: 0.8595 - acc: 0.8595 - val_loss: 1.1799 - val_orgCE: 1.1799 - val_myAcc: 0.8476 - val_acc: 0.8476
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8348 - orgCE: 0.8348 - myAcc: 0.8617 - acc: 0.8617 - val_loss: 1.0831 - val_orgCE: 1.0831 - val_myAcc: 0.8530 - val_acc: 0.8530
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8422 - orgCE: 0.8422 - myAcc: 0.8580 - acc: 0.8580 - val_loss: 1.0960 - val_orgCE: 1.0960 - val_myAcc: 0.8511 - val_acc: 0.8511
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8361 - orgCE: 0.8361 - myAcc: 0.8590 - acc: 0.8590 - val_loss: 1.1066 - val_orgCE: 1.1066 - val_myAcc: 0.8537 - val_acc: 0.8537
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8224 - orgCE: 0.8224 - myAcc: 0.8616 - acc: 0.8616 - val_loss: 1.1193 - val_orgCE: 1.1193 - val_myAcc: 0.8537 - val_acc: 0.8537
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8040 - orgCE: 0.8040 - myAcc: 0.8632 - acc: 0.8632 - val_loss: 1.0528 - val_orgCE: 1.0528 - val_myAcc: 0.8495 - val_acc: 0.8495
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8050 - orgCE: 0.8050 - myAcc: 0.8629 - acc: 0.8629 - val_loss: 1.1100 - val_orgCE: 1.1100 - val_myAcc: 0.8449 - val_acc: 0.8449
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7967 - orgCE: 0.7967 - myAcc: 0.8640 - acc: 0.8640 - val_loss: 1.0919 - val_orgCE: 1.0919 - val_myAcc: 0.8517 - val_acc: 0.8517
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7892 - orgCE: 0.7892 - myAcc: 0.8653 - acc: 0.8653 - val_loss: 1.1511 - val_orgCE: 1.1511 - val_myAcc: 0.8439 - val_acc: 0.8439
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7824 - orgCE: 0.7824 - myAcc: 0.8661 - acc: 0.8661 - val_loss: 1.0476 - val_orgCE: 1.0476 - val_myAcc: 0.8574 - val_acc: 0.8574
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.8038 - orgCE: 0.8038 - myAcc: 0.8623 - acc: 0.8623 - val_loss: 1.1942 - val_orgCE: 1.1942 - val_myAcc: 0.8467 - val_acc: 0.8467
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7657 - orgCE: 0.7657 - myAcc: 0.8672 - acc: 0.8672 - val_loss: 1.1201 - val_orgCE: 1.1201 - val_myAcc: 0.8507 - val_acc: 0.8507
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7602 - orgCE: 0.7602 - myAcc: 0.8665 - acc: 0.8665 - val_loss: 0.9692 - val_orgCE: 0.9692 - val_myAcc: 0.8598 - val_acc: 0.8598
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7471 - orgCE: 0.7471 - myAcc: 0.8696 - acc: 0.8696 - val_loss: 1.1681 - val_orgCE: 1.1681 - val_myAcc: 0.8437 - val_acc: 0.8437
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7443 - orgCE: 0.7443 - myAcc: 0.8701 - acc: 0.8701 - val_loss: 1.0329 - val_orgCE: 1.0329 - val_myAcc: 0.8589 - val_acc: 0.8589
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7743 - orgCE: 0.7743 - myAcc: 0.8644 - acc: 0.8644 - val_loss: 1.0722 - val_orgCE: 1.0722 - val_myAcc: 0.8510 - val_acc: 0.8510
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7484 - orgCE: 0.7484 - myAcc: 0.8679 - acc: 0.8679 - val_loss: 1.2760 - val_orgCE: 1.2760 - val_myAcc: 0.8396 - val_acc: 0.8396
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7171 - orgCE: 0.7171 - myAcc: 0.8715 - acc: 0.8715 - val_loss: 1.1636 - val_orgCE: 1.1636 - val_myAcc: 0.8433 - val_acc: 0.8433
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7277 - orgCE: 0.7277 - myAcc: 0.8716 - acc: 0.8716 - val_loss: 1.1085 - val_orgCE: 1.1085 - val_myAcc: 0.8506 - val_acc: 0.8506
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7517 - orgCE: 0.7517 - myAcc: 0.8666 - acc: 0.8666 - val_loss: 1.0817 - val_orgCE: 1.0817 - val_myAcc: 0.8532 - val_acc: 0.8532
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7239 - orgCE: 0.7239 - myAcc: 0.8699 - acc: 0.8699 - val_loss: 1.0675 - val_orgCE: 1.0675 - val_myAcc: 0.8529 - val_acc: 0.8529
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7095 - orgCE: 0.7095 - myAcc: 0.8724 - acc: 0.8724 - val_loss: 1.1984 - val_orgCE: 1.1984 - val_myAcc: 0.8416 - val_acc: 0.8416
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7197 - orgCE: 0.7197 - myAcc: 0.8705 - acc: 0.8705 - val_loss: 1.0873 - val_orgCE: 1.0873 - val_myAcc: 0.8505 - val_acc: 0.8505
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7236 - orgCE: 0.7236 - myAcc: 0.8693 - acc: 0.8693 - val_loss: 1.1450 - val_orgCE: 1.1450 - val_myAcc: 0.8450 - val_acc: 0.8450
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7021 - orgCE: 0.7021 - myAcc: 0.8727 - acc: 0.8727 - val_loss: 1.1011 - val_orgCE: 1.1011 - val_myAcc: 0.8463 - val_acc: 0.8463
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7122 - orgCE: 0.7122 - myAcc: 0.8705 - acc: 0.8705 - val_loss: 1.1800 - val_orgCE: 1.1800 - val_myAcc: 0.8445 - val_acc: 0.8445
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6932 - orgCE: 0.6932 - myAcc: 0.8734 - acc: 0.8734 - val_loss: 1.1803 - val_orgCE: 1.1803 - val_myAcc: 0.8422 - val_acc: 0.8422
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7225 - orgCE: 0.7225 - myAcc: 0.8693 - acc: 0.8693 - val_loss: 1.1266 - val_orgCE: 1.1266 - val_myAcc: 0.8437 - val_acc: 0.8437
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6883 - orgCE: 0.6883 - myAcc: 0.8743 - acc: 0.8743 - val_loss: 1.1938 - val_orgCE: 1.1938 - val_myAcc: 0.8442 - val_acc: 0.8442
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6908 - orgCE: 0.6908 - myAcc: 0.8723 - acc: 0.8723 - val_loss: 1.0957 - val_orgCE: 1.0957 - val_myAcc: 0.8500 - val_acc: 0.8500
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.7112 - orgCE: 0.7112 - myAcc: 0.8698 - acc: 0.8698 - val_loss: 1.2204 - val_orgCE: 1.2204 - val_myAcc: 0.8365 - val_acc: 0.8365
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6930 - orgCE: 0.6930 - myAcc: 0.8728 - acc: 0.8728 - val_loss: 1.1336 - val_orgCE: 1.1336 - val_myAcc: 0.8498 - val_acc: 0.8498
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6827 - orgCE: 0.6827 - myAcc: 0.8719 - acc: 0.8719 - val_loss: 1.1328 - val_orgCE: 1.1328 - val_myAcc: 0.8455 - val_acc: 0.8455
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6927 - orgCE: 0.6927 - myAcc: 0.8717 - acc: 0.8717 - val_loss: 1.2245 - val_orgCE: 1.2245 - val_myAcc: 0.8382 - val_acc: 0.8382
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6723 - orgCE: 0.6723 - myAcc: 0.8751 - acc: 0.8751 - val_loss: 1.2009 - val_orgCE: 1.2009 - val_myAcc: 0.8420 - val_acc: 0.8420
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6876 - orgCE: 0.6876 - myAcc: 0.8727 - acc: 0.8727 - val_loss: 1.1969 - val_orgCE: 1.1969 - val_myAcc: 0.8449 - val_acc: 0.8449
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6656 - orgCE: 0.6656 - myAcc: 0.8762 - acc: 0.8762 - val_loss: 1.2273 - val_orgCE: 1.2273 - val_myAcc: 0.8372 - val_acc: 0.8372
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6603 - orgCE: 0.6603 - myAcc: 0.8760 - acc: 0.8760 - val_loss: 1.2616 - val_orgCE: 1.2616 - val_myAcc: 0.8369 - val_acc: 0.8369
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6637 - orgCE: 0.6637 - myAcc: 0.8759 - acc: 0.8759 - val_loss: 1.0778 - val_orgCE: 1.0778 - val_myAcc: 0.8521 - val_acc: 0.8521
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6348 - orgCE: 0.6348 - myAcc: 0.8790 - acc: 0.8790 - val_loss: 1.1202 - val_orgCE: 1.1202 - val_myAcc: 0.8426 - val_acc: 0.8426
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6530 - orgCE: 0.6530 - myAcc: 0.8770 - acc: 0.8770 - val_loss: 1.1337 - val_orgCE: 1.1337 - val_myAcc: 0.8463 - val_acc: 0.8463
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6337 - orgCE: 0.6337 - myAcc: 0.8802 - acc: 0.8802 - val_loss: 1.2389 - val_orgCE: 1.2389 - val_myAcc: 0.8339 - val_acc: 0.8339
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6771 - orgCE: 0.6771 - myAcc: 0.8728 - acc: 0.8728 - val_loss: 1.1761 - val_orgCE: 1.1761 - val_myAcc: 0.8398 - val_acc: 0.8398
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6477 - orgCE: 0.6477 - myAcc: 0.8771 - acc: 0.8771 - val_loss: 1.1292 - val_orgCE: 1.1292 - val_myAcc: 0.8468 - val_acc: 0.8468
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6493 - orgCE: 0.6493 - myAcc: 0.8776 - acc: 0.8776 - val_loss: 1.2189 - val_orgCE: 1.2189 - val_myAcc: 0.8383 - val_acc: 0.8383
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6366 - orgCE: 0.6366 - myAcc: 0.8783 - acc: 0.8783 - val_loss: 1.2546 - val_orgCE: 1.2546 - val_myAcc: 0.8371 - val_acc: 0.8371
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6514 - orgCE: 0.6514 - myAcc: 0.8770 - acc: 0.8770 - val_loss: 1.1226 - val_orgCE: 1.1226 - val_myAcc: 0.8450 - val_acc: 0.8450
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6422 - orgCE: 0.6422 - myAcc: 0.8773 - acc: 0.8773 - val_loss: 1.2076 - val_orgCE: 1.2076 - val_myAcc: 0.8379 - val_acc: 0.8379
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6431 - orgCE: 0.6431 - myAcc: 0.8778 - acc: 0.8778 - val_loss: 1.2100 - val_orgCE: 1.2100 - val_myAcc: 0.8394 - val_acc: 0.8394
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6077 - orgCE: 0.6077 - myAcc: 0.8840 - acc: 0.8840 - val_loss: 1.1728 - val_orgCE: 1.1728 - val_myAcc: 0.8428 - val_acc: 0.8428
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.5981 - orgCE: 0.5981 - myAcc: 0.8845 - acc: 0.8845 - val_loss: 1.1230 - val_orgCE: 1.1230 - val_myAcc: 0.8455 - val_acc: 0.8455
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6279 - orgCE: 0.6279 - myAcc: 0.8792 - acc: 0.8792 - val_loss: 1.1948 - val_orgCE: 1.1948 - val_myAcc: 0.8413 - val_acc: 0.8413
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6320 - orgCE: 0.6320 - myAcc: 0.8800 - acc: 0.8800 - val_loss: 1.1794 - val_orgCE: 1.1794 - val_myAcc: 0.8440 - val_acc: 0.8440
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6038 - orgCE: 0.6038 - myAcc: 0.8849 - acc: 0.8849 - val_loss: 1.2056 - val_orgCE: 1.2056 - val_myAcc: 0.8407 - val_acc: 0.8407
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6370 - orgCE: 0.6370 - myAcc: 0.8774 - acc: 0.8774 - val_loss: 1.2013 - val_orgCE: 1.2013 - val_myAcc: 0.8415 - val_acc: 0.8415
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6245 - orgCE: 0.6245 - myAcc: 0.8793 - acc: 0.8793 - val_loss: 1.1516 - val_orgCE: 1.1516 - val_myAcc: 0.8460 - val_acc: 0.8460
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6170 - orgCE: 0.6170 - myAcc: 0.8806 - acc: 0.8806 - val_loss: 1.2615 - val_orgCE: 1.2615 - val_myAcc: 0.8378 - val_acc: 0.8378
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6081 - orgCE: 0.6081 - myAcc: 0.8829 - acc: 0.8829 - val_loss: 1.1405 - val_orgCE: 1.1405 - val_myAcc: 0.8511 - val_acc: 0.8511
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.5884 - orgCE: 0.5884 - myAcc: 0.8853 - acc: 0.8853 - val_loss: 1.1662 - val_orgCE: 1.1662 - val_myAcc: 0.8445 - val_acc: 0.8445
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6028 - orgCE: 0.6028 - myAcc: 0.8841 - acc: 0.8841 - val_loss: 1.1910 - val_orgCE: 1.1910 - val_myAcc: 0.8486 - val_acc: 0.8486
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6190 - orgCE: 0.6190 - myAcc: 0.8803 - acc: 0.8803 - val_loss: 1.2113 - val_orgCE: 1.2113 - val_myAcc: 0.8428 - val_acc: 0.8428
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.5968 - orgCE: 0.5968 - myAcc: 0.8840 - acc: 0.8840 - val_loss: 1.2213 - val_orgCE: 1.2213 - val_myAcc: 0.8465 - val_acc: 0.8465
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.6047 - orgCE: 0.6047 - myAcc: 0.8823 - acc: 0.8823 - val_loss: 1.2317 - val_orgCE: 1.2317 - val_myAcc: 0.8431 - val_acc: 0.8431
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 82s - loss: 0.5999 - orgCE: 0.5999 - myAcc: 0.8844 - acc: 0.8844 - val_loss: 1.1773 - val_orgCE: 1.1773 - val_myAcc: 0.8478 - val_acc: 0.8478


# python3 bleu_eval.py sample_output_testset.txt
Originally, average bleu score is 0.28851937705807923
By another method, average bleu score is 0.6361924222270333
