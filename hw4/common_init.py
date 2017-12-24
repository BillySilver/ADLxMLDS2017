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


"""
This part is for convenience to specify one of several models if you'd like to train with different settings.

`$ python3 train.py --model_id 0`
That means 'Generator.0.h5' and 'Discriminator.0.h5' are used.

Use model_path('Generator') or model_path('Discriminator') in code to get file paths.
"""

def parse():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('testing_text', metavar='filename', type=str, nargs='?', default='data/sample_testing_text.txt', help='file of testing text.')
    parser.add_argument('--model_dir', type=str, default='models/', help='directory for saving/loading model file')
    parser.add_argument('--model_id', type=int, default=None, help='specified id for model file')
    args = parser.parse_args()
    return args

args = parse()

def model_filename(str_name):
    if args.model_id is not None:
        return '%s.%d.h5' % (str_name, args.model_id)
    return '%s.h5' % str_name

def model_path(str_name):
    from os.path import join
    return join(args.model_dir, model_filename(str_name))
