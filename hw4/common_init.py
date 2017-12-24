import numpy as np


valid_attrs = {
    'hair': [
        'orange hair', 'white hair', 'aqua hair', 'gray hair',
        'green hair', 'red hair', 'purple hair', 'pink hair',
        'blue hair', 'black hair', 'brown hair', 'blonde hair' ],
    'eyes': [
        'gray eyes', 'black eyes', 'orange eyes',
        'pink eyes', 'yellow eyes', 'aqua eyes', 'purple eyes',
        'green eyes', 'brown eyes', 'red eyes', 'blue eyes' ]
}

# load conditions transformed by make_hair_eyes_vec.py.
# (155, 2400)
cond_vecs = np.load('models/hair_eyes_vec.npy')
cond_vec_ids = {}
with open('models/hair_eyes_vec.txt') as file:
    cond_id = 0
    for cond in file:
        cond = cond.strip()
        cond_vec_ids[cond] = cond_id

img_shape = (64, 64, 3)
cond_dim  = cond_vecs.shape[-1]
noise_dim = 128
