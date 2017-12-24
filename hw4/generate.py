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
        text_id  = int(line[0])

        cond = line[1].strip()
        cond = re.sub('\s+', ' ', cond)     # Reduce successive spaces.
        if re.findall('eyes.+hair', cond) != []:
            # Make sure 'hair' first if 'eyes' is in front of 'hair'.
            cond = cond.split()
            cond = cond[2: ] + cond[ :2]
            cond = ' '.join(cond)
        cond_id  = cond_vec_ids[cond]
        cond_vec = cond_vecs[cond_id]
        cond_vec = np.tile(cond_vec, (num_gene_imgs_per_text, 1))

        noises    = np.random.uniform(-1., 1., size=(num_gene_imgs_per_text, noise_dim))
        gene_imgs = G.predict([noises, cond_vec])
        for i in range(num_gene_imgs_per_text):
            scipy.misc.imsave('samples/sample_%d_%d.jpg' % (text_id, i+1), gene_imgs[i])
