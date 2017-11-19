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


def getInstances(video_ids=None, peer_review=False):
    if video_ids is None:
        video_ids = []
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

def getOneHotLabels_Fake(num_samples, maxText, num_classes):
    idxBOS = vocab2num['^']
    fake_labels = numpy.ones(shape=(num_samples, maxText, num_classes))
    fake_labels[ : , : , 0 : idxBOS+1] = 0
    return fake_labels
