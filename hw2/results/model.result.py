_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
Encoder_in (InputLayer)      (None, 80, 4096)          0         
_________________________________________________________________
zero_padding1d_1 (ZeroPaddin (None, 120, 4096)         0         
_________________________________________________________________
Encoder_out (LSTM)           (None, 120, 1024)         20975616  
_________________________________________________________________
lstm_1 (LSTM)                (None, 120, 1024)         8392704   
_________________________________________________________________
cropping1d_1 (Cropping1D)    (None, 40, 1024)          0         
_________________________________________________________________
time_distributed_1 (TimeDist (None, 40, 6132)          6285300   
=================================================================
Total params: 35,653,620
Trainable params: 35,653,620
Non-trainable params: 0
_________________________________________________________________

* Create a new model. *

* Epoch 1/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 40s - loss: 6.2675 - orgCE: 1.2064 - myAcc: 0.1393 - acc: 0.0269 - val_loss: 5.6486 - val_orgCE: 1.1247 - val_myAcc: 0.1692 - val_acc: 0.0334
* Epoch 2/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 37s - loss: 5.4209 - orgCE: 1.0444 - myAcc: 0.1796 - acc: 0.0347 - val_loss: 5.3139 - val_orgCE: 1.0587 - val_myAcc: 0.2116 - val_acc: 0.0420
* Epoch 3/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 37s - loss: 5.1367 - orgCE: 0.9931 - myAcc: 0.2402 - acc: 0.0464 - val_loss: 5.1160 - val_orgCE: 1.0071 - val_myAcc: 0.2620 - val_acc: 0.0516
* Epoch 4/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 37s - loss: 4.9257 - orgCE: 0.9377 - myAcc: 0.2614 - acc: 0.0498 - val_loss: 4.9067 - val_orgCE: 0.9659 - val_myAcc: 0.2770 - val_acc: 0.0546
* Epoch 5/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 37s - loss: 4.9266 - orgCE: 0.9601 - myAcc: 0.2562 - acc: 0.0498 - val_loss: 4.9765 - val_orgCE: 0.9654 - val_myAcc: 0.2585 - val_acc: 0.0502
* Epoch 6/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 37s - loss: 4.8167 - orgCE: 0.9400 - myAcc: 0.2679 - acc: 0.0522 - val_loss: 4.8755 - val_orgCE: 0.9193 - val_myAcc: 0.2593 - val_acc: 0.0488
* Epoch 7/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 37s - loss: 4.7918 - orgCE: 0.9608 - myAcc: 0.2617 - acc: 0.0523 - val_loss: 4.9411 - val_orgCE: 0.9431 - val_myAcc: 0.2675 - val_acc: 0.0509
* Epoch 8/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 37s - loss: 4.7580 - orgCE: 0.9307 - myAcc: 0.2594 - acc: 0.0506 - val_loss: 4.7878 - val_orgCE: 0.9172 - val_myAcc: 0.2837 - val_acc: 0.0543
* Epoch 9/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 37s - loss: 4.6931 - orgCE: 0.9072 - myAcc: 0.2656 - acc: 0.0511 - val_loss: 4.8164 - val_orgCE: 0.9445 - val_myAcc: 0.2742 - val_acc: 0.0535
* Epoch 10/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.6850 - orgCE: 0.9094 - myAcc: 0.2622 - acc: 0.0508 - val_loss: 4.7748 - val_orgCE: 0.9427 - val_myAcc: 0.2766 - val_acc: 0.0545
* Epoch 11/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.7447 - orgCE: 0.9283 - myAcc: 0.2578 - acc: 0.0503 - val_loss: 4.8512 - val_orgCE: 0.9393 - val_myAcc: 0.2602 - val_acc: 0.0505
* Epoch 12/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.6115 - orgCE: 0.8977 - myAcc: 0.2629 - acc: 0.0511 - val_loss: 4.9069 - val_orgCE: 0.9402 - val_myAcc: 0.2547 - val_acc: 0.0484
* Epoch 13/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.6574 - orgCE: 0.9068 - myAcc: 0.2582 - acc: 0.0502 - val_loss: 4.8675 - val_orgCE: 0.9627 - val_myAcc: 0.2643 - val_acc: 0.0522
* Epoch 14/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.5992 - orgCE: 0.8828 - myAcc: 0.2653 - acc: 0.0509 - val_loss: 4.6772 - val_orgCE: 0.9349 - val_myAcc: 0.2693 - val_acc: 0.0535
* Epoch 15/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.5321 - orgCE: 0.8644 - myAcc: 0.2652 - acc: 0.0504 - val_loss: 4.7273 - val_orgCE: 0.9147 - val_myAcc: 0.2766 - val_acc: 0.0535
* Epoch 16/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.5140 - orgCE: 0.8833 - myAcc: 0.2630 - acc: 0.0513 - val_loss: 4.5967 - val_orgCE: 0.8745 - val_myAcc: 0.2819 - val_acc: 0.0528
* Epoch 17/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.4515 - orgCE: 0.8486 - myAcc: 0.2638 - acc: 0.0503 - val_loss: 4.7886 - val_orgCE: 0.9552 - val_myAcc: 0.2672 - val_acc: 0.0532
* Epoch 18/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.4602 - orgCE: 0.8670 - myAcc: 0.2655 - acc: 0.0514 - val_loss: 4.5622 - val_orgCE: 0.8520 - val_myAcc: 0.2791 - val_acc: 0.0518
* Epoch 19/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.4171 - orgCE: 0.8617 - myAcc: 0.2672 - acc: 0.0519 - val_loss: 4.7070 - val_orgCE: 0.9015 - val_myAcc: 0.2675 - val_acc: 0.0512
* Epoch 20/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.4074 - orgCE: 0.8539 - myAcc: 0.2658 - acc: 0.0513 - val_loss: 4.6743 - val_orgCE: 0.9365 - val_myAcc: 0.2656 - val_acc: 0.0531
* Epoch 21/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.3764 - orgCE: 0.8404 - myAcc: 0.2687 - acc: 0.0514 - val_loss: 4.6474 - val_orgCE: 0.8970 - val_myAcc: 0.2690 - val_acc: 0.0516
* Epoch 22/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.3902 - orgCE: 0.8484 - myAcc: 0.2693 - acc: 0.0518 - val_loss: 4.6139 - val_orgCE: 0.8951 - val_myAcc: 0.2812 - val_acc: 0.0545
* Epoch 23/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.3271 - orgCE: 0.8296 - myAcc: 0.2737 - acc: 0.0523 - val_loss: 4.6295 - val_orgCE: 0.8973 - val_myAcc: 0.2828 - val_acc: 0.0548
* Epoch 24/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.3280 - orgCE: 0.8190 - myAcc: 0.2653 - acc: 0.0500 - val_loss: 4.7192 - val_orgCE: 0.9410 - val_myAcc: 0.2697 - val_acc: 0.0536
* Epoch 25/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.2735 - orgCE: 0.8260 - myAcc: 0.2771 - acc: 0.0533 - val_loss: 4.7336 - val_orgCE: 0.9553 - val_myAcc: 0.2675 - val_acc: 0.0538
* Epoch 26/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.3302 - orgCE: 0.8301 - myAcc: 0.2702 - acc: 0.0517 - val_loss: 4.5808 - val_orgCE: 0.8871 - val_myAcc: 0.2797 - val_acc: 0.0541
* Epoch 27/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.2821 - orgCE: 0.8245 - myAcc: 0.2770 - acc: 0.0529 - val_loss: 4.6480 - val_orgCE: 0.8969 - val_myAcc: 0.2765 - val_acc: 0.0535
* Epoch 28/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.2847 - orgCE: 0.8345 - myAcc: 0.2727 - acc: 0.0529 - val_loss: 4.5800 - val_orgCE: 0.8647 - val_myAcc: 0.2849 - val_acc: 0.0538
* Epoch 29/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.1717 - orgCE: 0.7994 - myAcc: 0.2803 - acc: 0.0533 - val_loss: 4.5388 - val_orgCE: 0.8903 - val_myAcc: 0.2649 - val_acc: 0.0517
* Epoch 30/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.1973 - orgCE: 0.8075 - myAcc: 0.2807 - acc: 0.0538 - val_loss: 4.5107 - val_orgCE: 0.8506 - val_myAcc: 0.2862 - val_acc: 0.0540
* Epoch 31/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.2302 - orgCE: 0.8218 - myAcc: 0.2736 - acc: 0.0530 - val_loss: 4.5146 - val_orgCE: 0.8326 - val_myAcc: 0.2902 - val_acc: 0.0535
* Epoch 32/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.1470 - orgCE: 0.8035 - myAcc: 0.2816 - acc: 0.0544 - val_loss: 4.4722 - val_orgCE: 0.8638 - val_myAcc: 0.2900 - val_acc: 0.0558
* Epoch 33/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.1559 - orgCE: 0.7996 - myAcc: 0.2810 - acc: 0.0539 - val_loss: 4.5236 - val_orgCE: 0.8729 - val_myAcc: 0.2808 - val_acc: 0.0538
* Epoch 34/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.1366 - orgCE: 0.7915 - myAcc: 0.2836 - acc: 0.0542 - val_loss: 4.5964 - val_orgCE: 0.8888 - val_myAcc: 0.2608 - val_acc: 0.0503
* Epoch 35/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.1058 - orgCE: 0.7871 - myAcc: 0.2821 - acc: 0.0538 - val_loss: 4.5589 - val_orgCE: 0.8964 - val_myAcc: 0.2810 - val_acc: 0.0548
* Epoch 36/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.1350 - orgCE: 0.8027 - myAcc: 0.2768 - acc: 0.0536 - val_loss: 4.5458 - val_orgCE: 0.9107 - val_myAcc: 0.2736 - val_acc: 0.0547
* Epoch 37/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.0873 - orgCE: 0.7843 - myAcc: 0.2848 - acc: 0.0545 - val_loss: 4.5783 - val_orgCE: 0.8853 - val_myAcc: 0.2715 - val_acc: 0.0523
* Epoch 38/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.0694 - orgCE: 0.7910 - myAcc: 0.2807 - acc: 0.0544 - val_loss: 4.5077 - val_orgCE: 0.8503 - val_myAcc: 0.2799 - val_acc: 0.0526
* Epoch 39/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.0973 - orgCE: 0.7818 - myAcc: 0.2774 - acc: 0.0529 - val_loss: 4.4968 - val_orgCE: 0.8385 - val_myAcc: 0.2931 - val_acc: 0.0545
* Epoch 40/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.0448 - orgCE: 0.7794 - myAcc: 0.2905 - acc: 0.0558 - val_loss: 4.5645 - val_orgCE: 0.8728 - val_myAcc: 0.2763 - val_acc: 0.0528
* Epoch 41/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.0285 - orgCE: 0.7758 - myAcc: 0.2848 - acc: 0.0547 - val_loss: 4.4021 - val_orgCE: 0.8426 - val_myAcc: 0.2849 - val_acc: 0.0542
* Epoch 42/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.0351 - orgCE: 0.7843 - myAcc: 0.2832 - acc: 0.0547 - val_loss: 4.4646 - val_orgCE: 0.8358 - val_myAcc: 0.2864 - val_acc: 0.0534
* Epoch 43/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.0391 - orgCE: 0.7882 - myAcc: 0.2778 - acc: 0.0542 - val_loss: 4.5528 - val_orgCE: 0.8733 - val_myAcc: 0.2799 - val_acc: 0.0537
* Epoch 44/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.9791 - orgCE: 0.7731 - myAcc: 0.2846 - acc: 0.0551 - val_loss: 4.4475 - val_orgCE: 0.8669 - val_myAcc: 0.2846 - val_acc: 0.0553
* Epoch 45/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.9657 - orgCE: 0.7649 - myAcc: 0.2856 - acc: 0.0550 - val_loss: 4.5870 - val_orgCE: 0.9135 - val_myAcc: 0.2745 - val_acc: 0.0547
* Epoch 46/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.9915 - orgCE: 0.7876 - myAcc: 0.2892 - acc: 0.0569 - val_loss: 4.5482 - val_orgCE: 0.8773 - val_myAcc: 0.2676 - val_acc: 0.0513
* Epoch 47/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 4.0296 - orgCE: 0.7930 - myAcc: 0.2813 - acc: 0.0552 - val_loss: 4.5690 - val_orgCE: 0.8951 - val_myAcc: 0.2672 - val_acc: 0.0522
* Epoch 48/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.9648 - orgCE: 0.7697 - myAcc: 0.2872 - acc: 0.0556 - val_loss: 4.5207 - val_orgCE: 0.8614 - val_myAcc: 0.2684 - val_acc: 0.0511
* Epoch 49/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.9632 - orgCE: 0.7716 - myAcc: 0.2872 - acc: 0.0558 - val_loss: 4.6419 - val_orgCE: 0.9135 - val_myAcc: 0.2858 - val_acc: 0.0561
* Epoch 50/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.9866 - orgCE: 0.7739 - myAcc: 0.2824 - acc: 0.0546 - val_loss: 4.4777 - val_orgCE: 0.8568 - val_myAcc: 0.2916 - val_acc: 0.0557
* Epoch 51/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.9066 - orgCE: 0.7549 - myAcc: 0.2929 - acc: 0.0566 - val_loss: 4.5942 - val_orgCE: 0.8833 - val_myAcc: 0.2710 - val_acc: 0.0521
* Epoch 52/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.9071 - orgCE: 0.7519 - myAcc: 0.2884 - acc: 0.0553 - val_loss: 4.5682 - val_orgCE: 0.8916 - val_myAcc: 0.2794 - val_acc: 0.0543
* Epoch 53/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.9032 - orgCE: 0.7682 - myAcc: 0.2892 - acc: 0.0565 - val_loss: 4.6069 - val_orgCE: 0.9119 - val_myAcc: 0.2583 - val_acc: 0.0509
* Epoch 54/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.9029 - orgCE: 0.7588 - myAcc: 0.2850 - acc: 0.0553 - val_loss: 4.4933 - val_orgCE: 0.8682 - val_myAcc: 0.2780 - val_acc: 0.0531
* Epoch 55/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.8698 - orgCE: 0.7435 - myAcc: 0.2874 - acc: 0.0550 - val_loss: 4.5132 - val_orgCE: 0.9057 - val_myAcc: 0.2861 - val_acc: 0.0568
* Epoch 56/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.8353 - orgCE: 0.7418 - myAcc: 0.2955 - acc: 0.0570 - val_loss: 4.5706 - val_orgCE: 0.9015 - val_myAcc: 0.2783 - val_acc: 0.0543
* Epoch 57/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.9183 - orgCE: 0.7730 - myAcc: 0.2906 - acc: 0.0572 - val_loss: 4.5188 - val_orgCE: 0.8681 - val_myAcc: 0.2818 - val_acc: 0.0542
* Epoch 58/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.8633 - orgCE: 0.7414 - myAcc: 0.2899 - acc: 0.0553 - val_loss: 4.4872 - val_orgCE: 0.8521 - val_myAcc: 0.2739 - val_acc: 0.0519
* Epoch 59/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.8557 - orgCE: 0.7522 - myAcc: 0.2941 - acc: 0.0573 - val_loss: 4.5497 - val_orgCE: 0.9193 - val_myAcc: 0.2715 - val_acc: 0.0546
* Epoch 60/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.8365 - orgCE: 0.7360 - myAcc: 0.2949 - acc: 0.0564 - val_loss: 4.5537 - val_orgCE: 0.9221 - val_myAcc: 0.2726 - val_acc: 0.0549
* Epoch 61/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.8002 - orgCE: 0.7344 - myAcc: 0.2979 - acc: 0.0575 - val_loss: 4.5617 - val_orgCE: 0.8854 - val_myAcc: 0.2731 - val_acc: 0.0530
* Epoch 62/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.7905 - orgCE: 0.7362 - myAcc: 0.3038 - acc: 0.0588 - val_loss: 4.4694 - val_orgCE: 0.8402 - val_myAcc: 0.2769 - val_acc: 0.0520
* Epoch 63/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.8699 - orgCE: 0.7683 - myAcc: 0.2873 - acc: 0.0569 - val_loss: 4.4618 - val_orgCE: 0.8844 - val_myAcc: 0.2853 - val_acc: 0.0560
* Epoch 64/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.7862 - orgCE: 0.7246 - myAcc: 0.3055 - acc: 0.0584 - val_loss: 4.4919 - val_orgCE: 0.8673 - val_myAcc: 0.2791 - val_acc: 0.0538
* Epoch 65/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.8354 - orgCE: 0.7542 - myAcc: 0.2884 - acc: 0.0566 - val_loss: 4.5241 - val_orgCE: 0.8972 - val_myAcc: 0.2783 - val_acc: 0.0549
* Epoch 66/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.7432 - orgCE: 0.7046 - myAcc: 0.3054 - acc: 0.0573 - val_loss: 4.4874 - val_orgCE: 0.8653 - val_myAcc: 0.2922 - val_acc: 0.0564
* Epoch 67/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.7436 - orgCE: 0.7278 - myAcc: 0.3100 - acc: 0.0602 - val_loss: 4.5895 - val_orgCE: 0.9053 - val_myAcc: 0.2727 - val_acc: 0.0537
* Epoch 68/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 37s - loss: 3.7721 - orgCE: 0.7424 - myAcc: 0.3003 - acc: 0.0588 - val_loss: 4.4547 - val_orgCE: 0.8679 - val_myAcc: 0.2902 - val_acc: 0.0562
* Epoch 69/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.7591 - orgCE: 0.7290 - myAcc: 0.2957 - acc: 0.0572 - val_loss: 4.5089 - val_orgCE: 0.8613 - val_myAcc: 0.2835 - val_acc: 0.0541
* Epoch 70/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.7074 - orgCE: 0.7277 - myAcc: 0.3106 - acc: 0.0608 - val_loss: 4.5027 - val_orgCE: 0.8771 - val_myAcc: 0.2868 - val_acc: 0.0555
* Epoch 71/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.7038 - orgCE: 0.7107 - myAcc: 0.3078 - acc: 0.0589 - val_loss: 4.5671 - val_orgCE: 0.8883 - val_myAcc: 0.2717 - val_acc: 0.0528
* Epoch 72/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.7508 - orgCE: 0.7291 - myAcc: 0.2996 - acc: 0.0581 - val_loss: 4.5698 - val_orgCE: 0.8996 - val_myAcc: 0.2691 - val_acc: 0.0526
* Epoch 73/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.7657 - orgCE: 0.7449 - myAcc: 0.2991 - acc: 0.0591 - val_loss: 4.4858 - val_orgCE: 0.8605 - val_myAcc: 0.2789 - val_acc: 0.0534
* Epoch 74/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6908 - orgCE: 0.7179 - myAcc: 0.3065 - acc: 0.0594 - val_loss: 4.4335 - val_orgCE: 0.8038 - val_myAcc: 0.2712 - val_acc: 0.0490
* Epoch 75/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.7187 - orgCE: 0.7161 - myAcc: 0.2993 - acc: 0.0575 - val_loss: 4.5733 - val_orgCE: 0.9047 - val_myAcc: 0.2638 - val_acc: 0.0521
* Epoch 76/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6970 - orgCE: 0.7205 - myAcc: 0.3046 - acc: 0.0592 - val_loss: 4.5705 - val_orgCE: 0.9341 - val_myAcc: 0.2732 - val_acc: 0.0555
* Epoch 77/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6495 - orgCE: 0.6972 - myAcc: 0.3154 - acc: 0.0600 - val_loss: 4.5569 - val_orgCE: 0.8625 - val_myAcc: 0.2680 - val_acc: 0.0507
* Epoch 78/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6296 - orgCE: 0.6963 - myAcc: 0.3088 - acc: 0.0591 - val_loss: 4.6083 - val_orgCE: 0.8769 - val_myAcc: 0.2776 - val_acc: 0.0526
* Epoch 79/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6811 - orgCE: 0.7105 - myAcc: 0.3020 - acc: 0.0581 - val_loss: 4.5385 - val_orgCE: 0.8667 - val_myAcc: 0.2845 - val_acc: 0.0541
* Epoch 80/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.7006 - orgCE: 0.7335 - myAcc: 0.3039 - acc: 0.0597 - val_loss: 4.5680 - val_orgCE: 0.8847 - val_myAcc: 0.2826 - val_acc: 0.0545
* Epoch 81/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6058 - orgCE: 0.6997 - myAcc: 0.3153 - acc: 0.0610 - val_loss: 4.5557 - val_orgCE: 0.8861 - val_myAcc: 0.2761 - val_acc: 0.0536
* Epoch 82/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6481 - orgCE: 0.7163 - myAcc: 0.3079 - acc: 0.0601 - val_loss: 4.5064 - val_orgCE: 0.8597 - val_myAcc: 0.2815 - val_acc: 0.0535
* Epoch 83/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6617 - orgCE: 0.7050 - myAcc: 0.3059 - acc: 0.0588 - val_loss: 4.5352 - val_orgCE: 0.8787 - val_myAcc: 0.2847 - val_acc: 0.0547
* Epoch 84/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6256 - orgCE: 0.6994 - myAcc: 0.3115 - acc: 0.0598 - val_loss: 4.4895 - val_orgCE: 0.8460 - val_myAcc: 0.2745 - val_acc: 0.0516
* Epoch 85/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.5748 - orgCE: 0.6797 - myAcc: 0.3190 - acc: 0.0604 - val_loss: 4.4658 - val_orgCE: 0.8428 - val_myAcc: 0.2876 - val_acc: 0.0540
* Epoch 86/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6281 - orgCE: 0.7081 - myAcc: 0.3108 - acc: 0.0604 - val_loss: 4.5847 - val_orgCE: 0.9180 - val_myAcc: 0.2709 - val_acc: 0.0539
* Epoch 87/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.5404 - orgCE: 0.6736 - myAcc: 0.3128 - acc: 0.0594 - val_loss: 4.6018 - val_orgCE: 0.8789 - val_myAcc: 0.2772 - val_acc: 0.0528
* Epoch 88/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6082 - orgCE: 0.6992 - myAcc: 0.3145 - acc: 0.0608 - val_loss: 4.4430 - val_orgCE: 0.8472 - val_myAcc: 0.2962 - val_acc: 0.0564
* Epoch 89/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.6105 - orgCE: 0.7009 - myAcc: 0.3091 - acc: 0.0600 - val_loss: 4.5705 - val_orgCE: 0.8903 - val_myAcc: 0.2763 - val_acc: 0.0536
* Epoch 90/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.5526 - orgCE: 0.6890 - myAcc: 0.3081 - acc: 0.0596 - val_loss: 4.5152 - val_orgCE: 0.8808 - val_myAcc: 0.2764 - val_acc: 0.0533
* Epoch 91/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.5895 - orgCE: 0.7002 - myAcc: 0.3083 - acc: 0.0601 - val_loss: 4.6052 - val_orgCE: 0.8887 - val_myAcc: 0.2753 - val_acc: 0.0529
* Epoch 92/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.5324 - orgCE: 0.6757 - myAcc: 0.3170 - acc: 0.0605 - val_loss: 4.5738 - val_orgCE: 0.8909 - val_myAcc: 0.2786 - val_acc: 0.0541
* Epoch 93/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.5082 - orgCE: 0.6729 - myAcc: 0.3214 - acc: 0.0615 - val_loss: 4.5426 - val_orgCE: 0.9023 - val_myAcc: 0.2747 - val_acc: 0.0545
* Epoch 94/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.5092 - orgCE: 0.6789 - myAcc: 0.3193 - acc: 0.0615 - val_loss: 4.5016 - val_orgCE: 0.8991 - val_myAcc: 0.2802 - val_acc: 0.0555
* Epoch 95/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.5513 - orgCE: 0.6938 - myAcc: 0.3113 - acc: 0.0605 - val_loss: 4.5325 - val_orgCE: 0.9006 - val_myAcc: 0.2660 - val_acc: 0.0528
* Epoch 96/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.5269 - orgCE: 0.6861 - myAcc: 0.3191 - acc: 0.0620 - val_loss: 4.5327 - val_orgCE: 0.8748 - val_myAcc: 0.2881 - val_acc: 0.0556
* Epoch 97/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.4565 - orgCE: 0.6664 - myAcc: 0.3269 - acc: 0.0629 - val_loss: 4.4425 - val_orgCE: 0.8272 - val_myAcc: 0.2841 - val_acc: 0.0528
* Epoch 98/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.4826 - orgCE: 0.6667 - myAcc: 0.3178 - acc: 0.0606 - val_loss: 4.6133 - val_orgCE: 0.9055 - val_myAcc: 0.2733 - val_acc: 0.0536
* Epoch 99/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.5020 - orgCE: 0.6797 - myAcc: 0.3162 - acc: 0.0609 - val_loss: 4.6917 - val_orgCE: 0.9348 - val_myAcc: 0.2738 - val_acc: 0.0543
* Epoch 100/100 *
Train on 1160 samples, validate on 290 samples
Epoch 1/1
1160/1160 [==============================] - 36s - loss: 3.4959 - orgCE: 0.6712 - myAcc: 0.3115 - acc: 0.0595 - val_loss: 4.4880 - val_orgCE: 0.8512 - val_myAcc: 0.2849 - val_acc: 0.0540
