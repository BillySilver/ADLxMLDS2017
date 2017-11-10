____________________________________________________________________________________________________
Layer (type)                     Output Shape          Param #     Connected to                     
====================================================================================================
Encoder_in (InputLayer)          (None, 80, 4096)      0                                            
____________________________________________________________________________________________________
Labels_in (InputLayer)           (None, 40, 6132)      0                                            
____________________________________________________________________________________________________
zero_padding1d_1 (ZeroPadding1D) (None, 120, 4096)     0           Encoder_in[0][0]                 
____________________________________________________________________________________________________
layer_bos__prev_labels_1 (Layer_ (None, 40, 6132)      0           Labels_in[0][0]                  
____________________________________________________________________________________________________
Encoder_out (LSTM)               (None, 120, 1024)     20975616    zero_padding1d_1[0][0]           
____________________________________________________________________________________________________
Labels_pad (ZeroPadding1D)       (None, 120, 6132)     0           layer_bos__prev_labels_1[0][0]   
____________________________________________________________________________________________________
Decoder_in (Concatenate)         (None, 120, 7156)     0           Encoder_out[0][0]                
                                                                   Labels_pad[0][0]                 
____________________________________________________________________________________________________
lstm_1 (LSTM)                    (None, 120, 1024)     33509376    Decoder_in[0][0]                 
____________________________________________________________________________________________________
cropping1d_1 (Cropping1D)        (None, 40, 1024)      0           lstm_1[0][0]                     
____________________________________________________________________________________________________
time_distributed_1 (TimeDistribu (None, 40, 6132)      6285300     cropping1d_1[0][0]               
====================================================================================================
Total params: 60,770,292
Trainable params: 60,770,292
Non-trainable params: 0
____________________________________________________________________________________________________

* Create a new model. *

* Epoch 1/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 59s - loss: 6.2518 - orgCE: 1.2099 - myAcc: 0.1302 - acc: 0.0253 - val_loss: 5.6402 - val_orgCE: 1.1124 - val_myAcc: 0.1647 - val_acc: 0.0324
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 5.4323 - orgCE: 1.0432 - myAcc: 0.1802 - acc: 0.0346 - val_loss: 5.2590 - val_orgCE: 0.9800 - val_myAcc: 0.2312 - val_acc: 0.0430
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 5.0477 - orgCE: 0.9691 - myAcc: 0.2521 - acc: 0.0483 - val_loss: 4.9764 - val_orgCE: 0.9179 - val_myAcc: 0.2734 - val_acc: 0.0503
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.9557 - orgCE: 0.9527 - myAcc: 0.2638 - acc: 0.0506 - val_loss: 4.9850 - val_orgCE: 0.9701 - val_myAcc: 0.2606 - val_acc: 0.0504
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.8420 - orgCE: 0.9354 - myAcc: 0.2644 - acc: 0.0511 - val_loss: 4.9127 - val_orgCE: 0.9686 - val_myAcc: 0.2656 - val_acc: 0.0521
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.7936 - orgCE: 0.9173 - myAcc: 0.2633 - acc: 0.0503 - val_loss: 4.8791 - val_orgCE: 0.9496 - val_myAcc: 0.2818 - val_acc: 0.0547
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 4.7658 - orgCE: 0.9236 - myAcc: 0.2651 - acc: 0.0512 - val_loss: 4.9488 - val_orgCE: 0.9782 - val_myAcc: 0.2666 - val_acc: 0.0526
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.7527 - orgCE: 0.9153 - myAcc: 0.2572 - acc: 0.0495 - val_loss: 4.7289 - val_orgCE: 0.8835 - val_myAcc: 0.2807 - val_acc: 0.0524
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.6962 - orgCE: 0.8985 - myAcc: 0.2656 - acc: 0.0507 - val_loss: 4.8229 - val_orgCE: 0.9348 - val_myAcc: 0.2627 - val_acc: 0.0509
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 4.6209 - orgCE: 0.8859 - myAcc: 0.2686 - acc: 0.0513 - val_loss: 4.8412 - val_orgCE: 0.9311 - val_myAcc: 0.2714 - val_acc: 0.0522
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 4.6214 - orgCE: 0.8794 - myAcc: 0.2678 - acc: 0.0509 - val_loss: 4.7969 - val_orgCE: 0.9169 - val_myAcc: 0.2595 - val_acc: 0.0495
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.5892 - orgCE: 0.8823 - myAcc: 0.2681 - acc: 0.0513 - val_loss: 4.7835 - val_orgCE: 0.9496 - val_myAcc: 0.2701 - val_acc: 0.0534
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.5795 - orgCE: 0.8840 - myAcc: 0.2596 - acc: 0.0501 - val_loss: 4.6597 - val_orgCE: 0.9049 - val_myAcc: 0.2703 - val_acc: 0.0521
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.4814 - orgCE: 0.8601 - myAcc: 0.2742 - acc: 0.0525 - val_loss: 4.6572 - val_orgCE: 0.9184 - val_myAcc: 0.2613 - val_acc: 0.0513
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.4821 - orgCE: 0.8620 - myAcc: 0.2635 - acc: 0.0505 - val_loss: 4.7331 - val_orgCE: 0.9429 - val_myAcc: 0.2594 - val_acc: 0.0516
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.4512 - orgCE: 0.8510 - myAcc: 0.2594 - acc: 0.0495 - val_loss: 4.5483 - val_orgCE: 0.8870 - val_myAcc: 0.2812 - val_acc: 0.0546
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.4206 - orgCE: 0.8641 - myAcc: 0.2603 - acc: 0.0508 - val_loss: 4.6054 - val_orgCE: 0.8978 - val_myAcc: 0.2803 - val_acc: 0.0543
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.3743 - orgCE: 0.8603 - myAcc: 0.2621 - acc: 0.0513 - val_loss: 4.5580 - val_orgCE: 0.8940 - val_myAcc: 0.2822 - val_acc: 0.0553
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.3463 - orgCE: 0.8430 - myAcc: 0.2684 - acc: 0.0519 - val_loss: 4.4528 - val_orgCE: 0.8489 - val_myAcc: 0.2919 - val_acc: 0.0553
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.3318 - orgCE: 0.8377 - myAcc: 0.2669 - acc: 0.0515 - val_loss: 4.5244 - val_orgCE: 0.8820 - val_myAcc: 0.2808 - val_acc: 0.0545
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.3339 - orgCE: 0.8482 - myAcc: 0.2736 - acc: 0.0533 - val_loss: 4.4173 - val_orgCE: 0.8492 - val_myAcc: 0.2869 - val_acc: 0.0551
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.2317 - orgCE: 0.8281 - myAcc: 0.2784 - acc: 0.0543 - val_loss: 4.4421 - val_orgCE: 0.8610 - val_myAcc: 0.2826 - val_acc: 0.0547
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.2189 - orgCE: 0.8310 - myAcc: 0.2752 - acc: 0.0541 - val_loss: 4.5352 - val_orgCE: 0.8672 - val_myAcc: 0.2869 - val_acc: 0.0546
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.1637 - orgCE: 0.8114 - myAcc: 0.2835 - acc: 0.0550 - val_loss: 4.4431 - val_orgCE: 0.8676 - val_myAcc: 0.2994 - val_acc: 0.0576
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.1081 - orgCE: 0.7982 - myAcc: 0.2926 - acc: 0.0566 - val_loss: 4.3650 - val_orgCE: 0.8402 - val_myAcc: 0.2949 - val_acc: 0.0566
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.0908 - orgCE: 0.7787 - myAcc: 0.2923 - acc: 0.0555 - val_loss: 4.4210 - val_orgCE: 0.8566 - val_myAcc: 0.2871 - val_acc: 0.0556
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.0774 - orgCE: 0.7777 - myAcc: 0.2871 - acc: 0.0547 - val_loss: 4.3542 - val_orgCE: 0.8222 - val_myAcc: 0.3012 - val_acc: 0.0566
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 4.0741 - orgCE: 0.7911 - myAcc: 0.2867 - acc: 0.0554 - val_loss: 4.2097 - val_orgCE: 0.7920 - val_myAcc: 0.3117 - val_acc: 0.0586
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.9802 - orgCE: 0.7607 - myAcc: 0.3021 - acc: 0.0575 - val_loss: 4.4392 - val_orgCE: 0.8640 - val_myAcc: 0.2807 - val_acc: 0.0545
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.9289 - orgCE: 0.7493 - myAcc: 0.3085 - acc: 0.0587 - val_loss: 4.2884 - val_orgCE: 0.8320 - val_myAcc: 0.3212 - val_acc: 0.0619
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.9689 - orgCE: 0.7778 - myAcc: 0.3009 - acc: 0.0589 - val_loss: 4.3419 - val_orgCE: 0.8355 - val_myAcc: 0.3038 - val_acc: 0.0584
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.8927 - orgCE: 0.7418 - myAcc: 0.3097 - acc: 0.0589 - val_loss: 4.3165 - val_orgCE: 0.8472 - val_myAcc: 0.3097 - val_acc: 0.0607
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 3.9205 - orgCE: 0.7695 - myAcc: 0.3060 - acc: 0.0598 - val_loss: 4.2701 - val_orgCE: 0.8468 - val_myAcc: 0.3193 - val_acc: 0.0628
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 3.8722 - orgCE: 0.7434 - myAcc: 0.3124 - acc: 0.0599 - val_loss: 4.2806 - val_orgCE: 0.8362 - val_myAcc: 0.3082 - val_acc: 0.0600
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.8800 - orgCE: 0.7686 - myAcc: 0.3134 - acc: 0.0619 - val_loss: 4.1759 - val_orgCE: 0.7943 - val_myAcc: 0.3089 - val_acc: 0.0586
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 3.7912 - orgCE: 0.7219 - myAcc: 0.3259 - acc: 0.0617 - val_loss: 4.2187 - val_orgCE: 0.7791 - val_myAcc: 0.3117 - val_acc: 0.0575
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.8339 - orgCE: 0.7442 - myAcc: 0.3140 - acc: 0.0609 - val_loss: 4.1953 - val_orgCE: 0.8298 - val_myAcc: 0.3241 - val_acc: 0.0641
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.7100 - orgCE: 0.7159 - myAcc: 0.3338 - acc: 0.0642 - val_loss: 4.0460 - val_orgCE: 0.7558 - val_myAcc: 0.3255 - val_acc: 0.0607
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.7044 - orgCE: 0.7297 - myAcc: 0.3353 - acc: 0.0658 - val_loss: 4.0767 - val_orgCE: 0.7438 - val_myAcc: 0.3279 - val_acc: 0.0596
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.7475 - orgCE: 0.7231 - myAcc: 0.3237 - acc: 0.0624 - val_loss: 4.2028 - val_orgCE: 0.8443 - val_myAcc: 0.3020 - val_acc: 0.0602
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.7304 - orgCE: 0.7289 - myAcc: 0.3269 - acc: 0.0636 - val_loss: 4.1403 - val_orgCE: 0.8198 - val_myAcc: 0.3130 - val_acc: 0.0619
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.6974 - orgCE: 0.7200 - myAcc: 0.3293 - acc: 0.0641 - val_loss: 4.1073 - val_orgCE: 0.7862 - val_myAcc: 0.3210 - val_acc: 0.0609
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.6117 - orgCE: 0.6952 - myAcc: 0.3432 - acc: 0.0659 - val_loss: 4.1606 - val_orgCE: 0.8094 - val_myAcc: 0.3249 - val_acc: 0.0632
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 3.6410 - orgCE: 0.7171 - myAcc: 0.3334 - acc: 0.0653 - val_loss: 4.0634 - val_orgCE: 0.7852 - val_myAcc: 0.3219 - val_acc: 0.0618
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.6187 - orgCE: 0.7024 - myAcc: 0.3404 - acc: 0.0659 - val_loss: 4.2302 - val_orgCE: 0.8386 - val_myAcc: 0.3107 - val_acc: 0.0615
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.6010 - orgCE: 0.6997 - myAcc: 0.3406 - acc: 0.0659 - val_loss: 4.1023 - val_orgCE: 0.8141 - val_myAcc: 0.3168 - val_acc: 0.0623
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.5802 - orgCE: 0.6808 - myAcc: 0.3451 - acc: 0.0655 - val_loss: 4.0665 - val_orgCE: 0.8011 - val_myAcc: 0.3327 - val_acc: 0.0651
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.5572 - orgCE: 0.6892 - myAcc: 0.3446 - acc: 0.0667 - val_loss: 4.0792 - val_orgCE: 0.8065 - val_myAcc: 0.3085 - val_acc: 0.0610
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.5342 - orgCE: 0.6874 - myAcc: 0.3482 - acc: 0.0676 - val_loss: 3.9690 - val_orgCE: 0.7391 - val_myAcc: 0.3329 - val_acc: 0.0620
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 3.5313 - orgCE: 0.6860 - myAcc: 0.3409 - acc: 0.0660 - val_loss: 4.0759 - val_orgCE: 0.7805 - val_myAcc: 0.3193 - val_acc: 0.0609
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.5414 - orgCE: 0.7053 - myAcc: 0.3438 - acc: 0.0683 - val_loss: 4.0700 - val_orgCE: 0.7952 - val_myAcc: 0.3211 - val_acc: 0.0627
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.4415 - orgCE: 0.6639 - myAcc: 0.3541 - acc: 0.0681 - val_loss: 4.2101 - val_orgCE: 0.8320 - val_myAcc: 0.3122 - val_acc: 0.0617
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.4408 - orgCE: 0.6566 - myAcc: 0.3555 - acc: 0.0678 - val_loss: 4.1207 - val_orgCE: 0.8039 - val_myAcc: 0.3127 - val_acc: 0.0606
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 3.4784 - orgCE: 0.6776 - myAcc: 0.3518 - acc: 0.0685 - val_loss: 4.0154 - val_orgCE: 0.7658 - val_myAcc: 0.3370 - val_acc: 0.0641
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.4058 - orgCE: 0.6450 - myAcc: 0.3611 - acc: 0.0683 - val_loss: 4.0039 - val_orgCE: 0.7862 - val_myAcc: 0.3407 - val_acc: 0.0666
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.3953 - orgCE: 0.6444 - myAcc: 0.3537 - acc: 0.0670 - val_loss: 3.9980 - val_orgCE: 0.7775 - val_myAcc: 0.3469 - val_acc: 0.0670
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 3.3488 - orgCE: 0.6440 - myAcc: 0.3658 - acc: 0.0702 - val_loss: 4.1455 - val_orgCE: 0.8079 - val_myAcc: 0.3221 - val_acc: 0.0622
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.4066 - orgCE: 0.6592 - myAcc: 0.3536 - acc: 0.0683 - val_loss: 4.0235 - val_orgCE: 0.7715 - val_myAcc: 0.3323 - val_acc: 0.0634
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.3688 - orgCE: 0.6481 - myAcc: 0.3676 - acc: 0.0706 - val_loss: 4.1888 - val_orgCE: 0.8550 - val_myAcc: 0.3179 - val_acc: 0.0649
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.3151 - orgCE: 0.6341 - myAcc: 0.3667 - acc: 0.0699 - val_loss: 4.1203 - val_orgCE: 0.8115 - val_myAcc: 0.3179 - val_acc: 0.0626
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.3767 - orgCE: 0.6545 - myAcc: 0.3609 - acc: 0.0698 - val_loss: 3.9416 - val_orgCE: 0.7390 - val_myAcc: 0.3429 - val_acc: 0.0643
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.3122 - orgCE: 0.6380 - myAcc: 0.3714 - acc: 0.0712 - val_loss: 3.9280 - val_orgCE: 0.7582 - val_myAcc: 0.3339 - val_acc: 0.0641
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.2721 - orgCE: 0.6281 - myAcc: 0.3712 - acc: 0.0711 - val_loss: 4.2269 - val_orgCE: 0.8556 - val_myAcc: 0.3290 - val_acc: 0.0659
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.2445 - orgCE: 0.6185 - myAcc: 0.3758 - acc: 0.0715 - val_loss: 4.0071 - val_orgCE: 0.7630 - val_myAcc: 0.3514 - val_acc: 0.0668
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.2739 - orgCE: 0.6405 - myAcc: 0.3779 - acc: 0.0738 - val_loss: 3.9262 - val_orgCE: 0.7528 - val_myAcc: 0.3549 - val_acc: 0.0679
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.2683 - orgCE: 0.6281 - myAcc: 0.3731 - acc: 0.0714 - val_loss: 4.0071 - val_orgCE: 0.7960 - val_myAcc: 0.3437 - val_acc: 0.0677
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.2426 - orgCE: 0.6258 - myAcc: 0.3776 - acc: 0.0727 - val_loss: 3.9779 - val_orgCE: 0.7610 - val_myAcc: 0.3366 - val_acc: 0.0644
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.1611 - orgCE: 0.6101 - myAcc: 0.3864 - acc: 0.0743 - val_loss: 3.9409 - val_orgCE: 0.7454 - val_myAcc: 0.3459 - val_acc: 0.0653
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.2052 - orgCE: 0.6206 - myAcc: 0.3811 - acc: 0.0735 - val_loss: 4.0470 - val_orgCE: 0.8068 - val_myAcc: 0.3301 - val_acc: 0.0657
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.1663 - orgCE: 0.6027 - myAcc: 0.3788 - acc: 0.0718 - val_loss: 4.0127 - val_orgCE: 0.7738 - val_myAcc: 0.3412 - val_acc: 0.0657
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.1807 - orgCE: 0.6142 - myAcc: 0.3822 - acc: 0.0736 - val_loss: 3.9581 - val_orgCE: 0.7805 - val_myAcc: 0.3525 - val_acc: 0.0689
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.1271 - orgCE: 0.5938 - myAcc: 0.3857 - acc: 0.0730 - val_loss: 4.0408 - val_orgCE: 0.8030 - val_myAcc: 0.3302 - val_acc: 0.0654
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.1344 - orgCE: 0.6069 - myAcc: 0.3894 - acc: 0.0750 - val_loss: 3.9068 - val_orgCE: 0.7583 - val_myAcc: 0.3546 - val_acc: 0.0685
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.2012 - orgCE: 0.6293 - myAcc: 0.3792 - acc: 0.0742 - val_loss: 3.9377 - val_orgCE: 0.7780 - val_myAcc: 0.3407 - val_acc: 0.0668
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 3.0762 - orgCE: 0.5923 - myAcc: 0.3934 - acc: 0.0755 - val_loss: 3.8511 - val_orgCE: 0.7515 - val_myAcc: 0.3624 - val_acc: 0.0703
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.1380 - orgCE: 0.6184 - myAcc: 0.3896 - acc: 0.0767 - val_loss: 3.9784 - val_orgCE: 0.7772 - val_myAcc: 0.3393 - val_acc: 0.0662
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.1216 - orgCE: 0.6109 - myAcc: 0.3927 - acc: 0.0767 - val_loss: 4.0328 - val_orgCE: 0.7986 - val_myAcc: 0.3455 - val_acc: 0.0681
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.0861 - orgCE: 0.6009 - myAcc: 0.3927 - acc: 0.0764 - val_loss: 4.0013 - val_orgCE: 0.7701 - val_myAcc: 0.3387 - val_acc: 0.0650
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.0318 - orgCE: 0.5833 - myAcc: 0.4033 - acc: 0.0775 - val_loss: 3.9524 - val_orgCE: 0.7712 - val_myAcc: 0.3589 - val_acc: 0.0698
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.9580 - orgCE: 0.5655 - myAcc: 0.4103 - acc: 0.0782 - val_loss: 4.0112 - val_orgCE: 0.7743 - val_myAcc: 0.3371 - val_acc: 0.0639
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.0143 - orgCE: 0.5621 - myAcc: 0.4041 - acc: 0.0752 - val_loss: 4.0770 - val_orgCE: 0.7982 - val_myAcc: 0.3394 - val_acc: 0.0663
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 3.0492 - orgCE: 0.5948 - myAcc: 0.4012 - acc: 0.0781 - val_loss: 3.9277 - val_orgCE: 0.7549 - val_myAcc: 0.3449 - val_acc: 0.0663
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.0135 - orgCE: 0.5879 - myAcc: 0.3988 - acc: 0.0774 - val_loss: 3.9599 - val_orgCE: 0.7744 - val_myAcc: 0.3436 - val_acc: 0.0672
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.0268 - orgCE: 0.5954 - myAcc: 0.3986 - acc: 0.0781 - val_loss: 4.0842 - val_orgCE: 0.8221 - val_myAcc: 0.3310 - val_acc: 0.0660
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.0197 - orgCE: 0.5793 - myAcc: 0.4041 - acc: 0.0773 - val_loss: 3.8384 - val_orgCE: 0.7392 - val_myAcc: 0.3546 - val_acc: 0.0679
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.9981 - orgCE: 0.5854 - myAcc: 0.4057 - acc: 0.0790 - val_loss: 3.7758 - val_orgCE: 0.7085 - val_myAcc: 0.3639 - val_acc: 0.0679
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 3.0004 - orgCE: 0.5945 - myAcc: 0.4030 - acc: 0.0797 - val_loss: 4.0441 - val_orgCE: 0.8197 - val_myAcc: 0.3289 - val_acc: 0.0661
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.9708 - orgCE: 0.5813 - myAcc: 0.4080 - acc: 0.0795 - val_loss: 3.9087 - val_orgCE: 0.7606 - val_myAcc: 0.3650 - val_acc: 0.0709
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.9529 - orgCE: 0.5733 - myAcc: 0.4049 - acc: 0.0785 - val_loss: 3.9517 - val_orgCE: 0.7947 - val_myAcc: 0.3508 - val_acc: 0.0702
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8975 - orgCE: 0.5535 - myAcc: 0.4164 - acc: 0.0792 - val_loss: 3.9490 - val_orgCE: 0.7564 - val_myAcc: 0.3489 - val_acc: 0.0667
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 2.9158 - orgCE: 0.5615 - myAcc: 0.4168 - acc: 0.0800 - val_loss: 3.9453 - val_orgCE: 0.7898 - val_myAcc: 0.3450 - val_acc: 0.0687
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 2.9264 - orgCE: 0.5659 - myAcc: 0.4168 - acc: 0.0802 - val_loss: 3.7303 - val_orgCE: 0.7255 - val_myAcc: 0.3734 - val_acc: 0.0725
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 56s - loss: 2.8788 - orgCE: 0.5574 - myAcc: 0.4129 - acc: 0.0800 - val_loss: 3.9493 - val_orgCE: 0.7689 - val_myAcc: 0.3464 - val_acc: 0.0672
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8936 - orgCE: 0.5597 - myAcc: 0.4187 - acc: 0.0808 - val_loss: 4.0183 - val_orgCE: 0.7942 - val_myAcc: 0.3404 - val_acc: 0.0669
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.9399 - orgCE: 0.5782 - myAcc: 0.4096 - acc: 0.0805 - val_loss: 4.0281 - val_orgCE: 0.8094 - val_myAcc: 0.3469 - val_acc: 0.0696
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8444 - orgCE: 0.5552 - myAcc: 0.4277 - acc: 0.0831 - val_loss: 3.8668 - val_orgCE: 0.7743 - val_myAcc: 0.3594 - val_acc: 0.0717
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8509 - orgCE: 0.5545 - myAcc: 0.4252 - acc: 0.0825 - val_loss: 3.9218 - val_orgCE: 0.7702 - val_myAcc: 0.3642 - val_acc: 0.0714
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8101 - orgCE: 0.5422 - myAcc: 0.4300 - acc: 0.0828 - val_loss: 3.9854 - val_orgCE: 0.7887 - val_myAcc: 0.3525 - val_acc: 0.0696
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.7740 - orgCE: 0.5245 - myAcc: 0.4306 - acc: 0.0814 - val_loss: 3.9732 - val_orgCE: 0.7702 - val_myAcc: 0.3552 - val_acc: 0.0686
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 57s - loss: 2.8292 - orgCE: 0.5547 - myAcc: 0.4267 - acc: 0.0834 - val_loss: 3.8768 - val_orgCE: 0.7631 - val_myAcc: 0.3469 - val_acc: 0.0678
