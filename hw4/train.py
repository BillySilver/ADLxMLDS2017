from model_setup import *
from train_init import *
import sys
import time
import numpy as np

valid_img_ids = []
for img_id in range(len(img_attrs)):
    flag = False
    for attr in ['hair', 'eyes']:
        if len(img_attrs[img_id][attr]) > 1:
            flag = False
            break
        if len(img_attrs[img_id][attr]) == 1:
            flag = True
    if flag:
        valid_img_ids += [ img_id ]
valid_img_ids = np.array(valid_img_ids)

# Categorize valid_img_ids by attributes. Balance.
# Lengths:
# [ 244, 557, 731, 619, 698, 681, 898, 1256, 1277, 1800, 2509, 2567,
#   128, 194, 226, 452, 791, 1025, 1253, 1477, 1473, 2229, 2995 ]
cate_valid_img_ids = []
for attr in ['hair', 'eyes']:
    valid_attr = valid_attrs[attr]
    cate_valid_img_ids_for_this_attr = [ [] for _ in range(len(valid_attr)) ]
    #
    for img_id in valid_img_ids:
        img_attr = img_attrs[img_id][attr]
        if len(img_attr) == 1:
            cate_valid_img_ids_for_this_attr[ valid_attr.index(img_attr[0]) ].append(img_id)
    #
    cate_valid_img_ids += cate_valid_img_ids_for_this_attr

def choose_balanced_valid_img_ids(cate_valid_img_ids, batch_sz_):
    cate_idcs = np.random.choice(len(cate_valid_img_ids), batch_sz_)
    batch_ids = [ np.random.choice(cate_valid_img_ids[cate_idx], 1) for cate_idx in cate_idcs ]
    batch_ids = np.concatenate(batch_ids)
    return batch_ids


G   = Generator(img_shape, cond_dim=cond_dim, noise_dim=noise_dim)
D   = Discriminator(img_shape, cond_dim=cond_dim)
gan = GAN(G, D, cond_dim=cond_dim, noise_dim=noise_dim)
iwd = iW_D(D, img_shape, cond_dim=cond_dim, lmbd=10.)
try:
    G.load_weights(model_path('Generator'))
    D.load_weights(model_path('Discriminator'))
    print('\n* Has loaded existed model. *\n')
except:
    G.summary()
    D.summary()
    print('\n* Create a new model. *\n')


epochs     = 600
batch_size = 64
ONES       = np.ones(shape=(batch_size, 1))
ONES_RES   = np.ones(shape=(valid_img_ids.size % batch_size, 1))    # for the last part data in one epoch.
for i_epoch in range(epochs):
    epoch_beg_time = time.time()
    print('Epoch %d/%d' % (i_epoch+1, epochs))
    losses_G = []
    losses_D = []

    for batch_beg in range(0, valid_img_ids.size, batch_size):
        batch_sz_  = batch_size if batch_beg + batch_size <= valid_img_ids.size \
                                else (valid_img_ids.size - batch_beg)
        batch_ids  = choose_balanced_valid_img_ids(cate_valid_img_ids, batch_sz_)
        batch_imgs = real_imgs[batch_ids]
        batch_right_cond_vecs, batch_wrong_cond_vecs = convert_attrs_to_cond_vecs(batch_ids)

        ONES_ptr = ONES if batch_ids.size == batch_size else ONES_RES

        # Train D.
        for _ in range(1):
            batch_noise = CommonNoiseGenerator(size=(batch_ids.size, noise_dim))
            fake_imgs = G.predict([batch_noise, batch_right_cond_vecs])
            loss_D = iwd.train_on_batch(x=[batch_imgs, fake_imgs, batch_right_cond_vecs, batch_wrong_cond_vecs],
                                        y=[ONES_ptr, ONES_ptr, ONES_ptr])
            losses_D += [ loss_D[0] ]   # sum of weighted loss.

        # Train G.
        batch_noise = CommonNoiseGenerator(size=(batch_ids.size, noise_dim))
        loss_G = gan.train_on_batch(x=[batch_noise, batch_right_cond_vecs], y=ONES_ptr)
        losses_G += [ loss_G ]

        batch_end  = batch_beg + batch_ids.size
        epoch_time = time.time() - epoch_beg_time
        percent    = float(batch_end) / valid_img_ids.size
        eta        = epoch_time / percent * (1. - percent)
        if batch_beg != 0:
            sys.stdout.write('\033[F')  # back to previous line.
            sys.stdout.write('\033[K')  # clear line.
        print('%d/%d - ETA: %ds' % (batch_end, valid_img_ids.size, eta), end='')
        print(' - loss_G: %.4f' % np.mean(losses_G), end='')
        print(' - loss_D: %.4f' % np.mean(losses_D), end='')
        print('', flush=True)

    epoch_time = time.time() - epoch_beg_time
    sys.stdout.write('\033[F')  # back to previous line.
    sys.stdout.write('\033[K')  # clear line.
    print('%d/%d - %ds' % (valid_img_ids.size, valid_img_ids.size, epoch_time), end='')
    print(' - loss_G: %.4f' % np.mean(losses_G), end='')
    print(' - loss_D: %.4f' % np.mean(losses_D), end='')
    print('', flush=True)

    G.save_weights(model_path('Generator'))
    D.save_weights(model_path('Discriminator'))
