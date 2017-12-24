from model_setup import *
from train_init import *
import time
import numpy as np

valid_img_ids = []
for img_id in range(len(img_attrs)):
    flag = False
    for attr in ['hair', 'eyes']:
        if len(img_attrs[img_id][attr]) > 1:
            continue
        if len(img_attrs[img_id][attr]) == 1:
            flag = True
    if flag:
        valid_img_ids += [ img_id ]
valid_img_ids = np.array(valid_img_ids)


G   = Generator(img_shape, cond_dim=cond_dim, noise_dim=noise_dim)
D   = Discriminator(img_shape, cond_dim=cond_dim)
gan = GAN(G, D, cond_dim=cond_dim, noise_dim=noise_dim)
iwd = iW_D(D, img_shape, cond_dim=cond_dim, lmbd=10.)
try:
    G.load_weights('models/Generator.h5')
    D.load_weights('models/Discriminator.h5')
    print('\n* Has loaded existed model. *\n')
except:
    G.summary()
    D.summary()
    print('\n* Create a new model. *\n')


epochs     = 300
batch_size = 64
ONES       = np.ones(shape=(batch_size, 1))
ONES_RES   = np.ones(shape=(valid_img_ids.size % batch_size, 1))    # for the last part data in one epoch.
for i_epoch in range(epochs):
    epoch_beg_time = time.time()
    print('Epoch %d/%d' % (i_epoch+1, epochs))
    losses_G = []
    losses_D = []

    np.random.shuffle(valid_img_ids)
    for batch_beg in range(0, valid_img_ids.size, batch_size):
        batch_ids   = valid_img_ids[batch_beg : batch_beg+batch_size]
        batch_imgs  = real_imgs[batch_ids]
        batch_noise = np.random.uniform(-1., 1., size=(batch_ids.size, noise_dim))
        batch_right_cond_vecs, batch_wrong_cond_vecs = convert_attrs_to_cond_vecs(batch_ids)

        ONES_ptr = ONES if batch_ids.size == batch_size else ONES_RES

        # Train D.
        D.trainable = True
        fake_imgs = G.predict([batch_noise, batch_right_cond_vecs])
        loss_D = iwd.train_on_batch(x=[batch_imgs, fake_imgs, batch_right_cond_vecs, batch_wrong_cond_vecs],
                                    y=[ONES_ptr, ONES_ptr, ONES_ptr])
        losses_D += [ loss_D[0] ]

        # Train G.
        D.trainable = False
        loss_G = gan.train_on_batch(x=[batch_noise, batch_right_cond_vecs], y=ONES_ptr)
        losses_G += [ loss_G ]

        batch_end  = batch_beg + batch_ids.size
        epoch_time = time.time() - epoch_beg_time
        percent    = float(batch_end) / valid_img_ids.size
        eta        = epoch_time / percent * (1. - percent)
        print('%d/%d - ETA: %ds' % (batch_end, valid_img_ids.size, eta), end='')
        print(' - loss_G: %.4f' % np.mean(losses_G), end='')
        print(' - loss_D: %.4f' % np.mean(losses_D), end='')
        print('', end='\r', flush=True)

    epoch_time = time.time() - epoch_beg_time
    print('%d/%d - %ds' % (valid_img_ids.size, valid_img_ids.size, epoch_time), end='')
    print(' - loss_G: %.4f' % np.mean(losses_G), end='')
    print(' - loss_D: %.4f' % np.mean(losses_D), flush=True)

    G.save_weights('models/Generator.h5')
    D.save_weights('models/Discriminator.h5')
