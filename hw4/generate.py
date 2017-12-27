from common_init import *
from model_setup import *
import sys
import re
import scipy.misc


num_gene_imgs_per_text = 5
np.random.seed(1337)     # To guarantee the results can be reproduced.


G = Generator(img_shape, cond_dim=cond_dim, noise_dim=noise_dim)
G.load_weights(model_path('Generator'))

with open(args.testing_text) as file:
    for line in file:
        line     = line.split(',')
        text_id  = line[0]

        cond = line[1].strip()
        cond = re.sub('\s+', ' ', cond)     # Reduce successive spaces.

        attr_ids = ()
        for attr in ['hair', 'eyes']:
            img_attr = re.findall('[^ ]+ %s' % attr, cond)
            if len(img_attr) > 0:
                img_attr = img_attr[0]
                attr_id  = cond_vec_ids[img_attr]
            else:
                attr_id = -1
            #
            attr_ids += (attr_id, )

        cond_vec = cond_vecs[list(attr_ids)]
        cond_vec = np.tile(cond_vec, (num_gene_imgs_per_text, 1))
        cond_vec = cond_vec.reshape((num_gene_imgs_per_text, -1))

        noises    = CommonNoiseGenerator(size=(num_gene_imgs_per_text, noise_dim))
        gene_imgs = G.predict([noises, cond_vec])
        for i in range(num_gene_imgs_per_text):
            scipy.misc.imsave('samples/sample_%s_%d.jpg' % (text_id, i+1), gene_imgs[i])
