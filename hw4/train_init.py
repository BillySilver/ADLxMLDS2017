from common_init import *
import skimage.io
import skimage.transform


# # Hair = 16545
# # Eyes = 14693
# #(Hair & Eyes) = 13843
# #(Hair | Eyes) = 17395
img_attrs = {}

# load useful tags like 'hair' and 'eyes'.
with open('data/tags_clean.csv') as file:
    for line in file:
        # img_id,(tag:#posts\t)+
        line   = line.split(',')
        img_id = int(line[0])
        img_attrs[img_id] = {'hair': [], 'eyes': []}

        line = line[1].split('\t')
        for tag in line:
            # Ignore #posts.
            tag = tag.split(':')[0]
            for attr in ['hair', 'eyes']:
                if tag in valid_attrs[attr]:
                    img_attrs[img_id][attr] += [ tag ]

# load resized and scaled real-images.
try:
    real_imgs = np.load('data/faces_resized.npy')
except:
    real_imgs = []
    for img_id in range(len(img_attrs)):
        img = skimage.io.imread('data/faces/%d.jpg' % img_id)
        img = skimage.transform.resize(img, img_shape[ :-1], mode='constant')  # It also scales img to [0, 1].
        real_imgs += [ img ]
    real_imgs = np.array(real_imgs)
    np.save('data/faces_resized.npy', real_imgs)


cond_vecs[-1] = np.zeros_like(cond_vecs[-1])    # Denote as a null condition.

def convert_attrs_to_cond_vecs(img_ids):
    right_cond_ids = []
    wrong_cond_ids = []
    for img_id in img_ids:
        right_attr_ids = ()
        wrong_attr_ids = ()
        for attr in ['hair', 'eyes']:
            img_attr = img_attrs[img_id][attr]
            right_attr = None
            if len(img_attr) > 0:
                right_attr = np.random.choice(img_attr)
                #
                while True:
                    wrong_attr = np.random.choice(valid_attrs[attr])
                    if wrong_attr not in img_attr:
                        break
                right_attr_id = cond_vec_ids[right_attr]
                wrong_attr_id = cond_vec_ids[wrong_attr]
            else:
                right_attr_id = -1  # Null condition.
                wrong_attr_id = -1  # Null condition.
            #
            right_attr_ids += (right_attr_id, )
            wrong_attr_ids += (wrong_attr_id, )

        right_cond_id  = right_attr_ids
        right_cond_ids += [ right_cond_id ]

        wrong_cond_id  = wrong_attr_ids
        wrong_cond_ids += [ wrong_cond_id ]

    right_cond_ids = np.array(right_cond_ids)
    wrong_cond_ids = np.array(wrong_cond_ids)

    # (num_img_ids, N, num_cond_dim) => (num_img_ids, N * num_cond_dim),
    # where N is the number of attributes of a condition.
    return cond_vecs[right_cond_ids].reshape((img_ids.size, -1)), \
           cond_vecs[wrong_cond_ids].reshape((img_ids.size, -1))
