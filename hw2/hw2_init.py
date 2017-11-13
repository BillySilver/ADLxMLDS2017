from keras_custom_init import *
import numpy
import sys
import re
import json


try:
    dataPath = sys.argv[1]
except:
    dataPath = 'MLDS_hw2_data/'


with open('models/num2vocab.json') as file:
    num2vocab = json.load(file)
    vocab2num = {}
    for idx in range(len(num2vocab)):
        text = num2vocab[idx]
        vocab2num[text] = idx


def nums2captions(nums):
    # One-hot.
    if type(nums) == numpy.ndarray:
        nums = numpy.argmax(nums, axis=-1)
    return __nums2captionsRecur(nums)

def __nums2captionsRecur(nums):
    if type(nums) == numpy.ndarray and 1 < len(nums.shape):
        return [ __nums2captionsRecur(array) for array in nums ]
    elif type(nums) == list and type(nums[0]) == list:
        return [ __nums2captionsRecur(array) for array in nums ]

    for i in range(len(nums)):
        if nums[i] == vocab2num['.']:
            nums = nums[ :i]
            break

    return [ num2vocab[idx] for idx in nums ]


def getInstances(video_ids=[], peer_review=False):
    if video_ids == []:
        IDPath = '/testing_id.txt' if peer_review is False else '/peer_review_id.txt'
        with open(dataPath + IDPath) as file:
            for line in file:
                video_ids += [ line.strip('\n') ]

    instances = []
    featPath  = '/testing_data/feat/' if peer_review is False else '/peer_review/feat/'
    for vid in video_ids:
        instances += [ numpy.load(dataPath + featPath + vid + '.npy') ]

    # (nVideo, nFrame, nFeature) = (1450, 80, 4096)
    instances = numpy.array(instances, dtype='float16')
    return instances, video_ids



"""Other functions for convenience
"""

def getCaptions(video_ids=None):
    with open(dataPath + '/testing_label.json') as file:
        labelFile = json.load(file)

    minText   = 1000
    maxText   = 0
    captions  = []
    for video in labelFile:
        vid = video['id']
        if video_ids is not None and vid not in video_ids:
            continue
        captions += [ [] ]
        for caption in video['caption']:
            texts   = re.findall(r'\w.*?(?=[^\w]*\s|[^\w]*$)', caption)
            nText   = len(texts)
            minText = min(minText, nText)
            maxText = max(maxText, nText)

            try:
                # To ignore caption which contains a word not in vocabulary.
                texts = [ vocab2num[text.lower()] for text in texts ] + [0]
                captions[-1] += [ texts ]
            except:
                pass

    return captions, maxText+1

# from model_init import getOneHotLabels_RandChoicePerVideo
def getOneHotLabels_RandChoicePerVideo(captions, num_classes):
    from keras.utils import np_utils
    maxText = 41
    """choice one caption (list of ints) from caption candidates ramdomly for each video.

    Arguments:
        captions {list} -- contains captions (list) of videos.
        num_classes {int} -- vocabulary size.

    Returns:
        numpy.darray -- one-hot vectors. shape = (#sample, #max_timestep, #feature)
    """
    labels = []
    for videoCaps in captions:
        idx     = numpy.random.randint(len(videoCaps))
        caption = videoCaps[idx]
        # labels  += [ np_utils.to_categorical(caption, num_classes=num_classes) ]
        labels  += [ numpy.concatenate(
            ( np_utils.to_categorical(caption, num_classes=num_classes),
              numpy.zeros( (maxText-len(caption), num_classes) ) ),     # Dummy inputs.
            axis=0
        ) ]
    return numpy.array(labels)
