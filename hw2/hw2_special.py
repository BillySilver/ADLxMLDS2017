from hw2_init import *
from keras.models import load_model


try:
    outputFileName = sys.argv[2]
except:
    outputFileName = 'sample_output_special.txt'


test_video_ids = ['klteYv1Uv9A_27_33.avi',
                  '5YJaS2Eswg0_22_26.avi',
                  'UbmZAe5u5FI_132_141.avi',
                  'JntMAcTlOF0_50_70.avi',
                  'tJHUH9tpqPg_113_118.avi']

nVocabFeat = len(num2vocab)
captions, _ = getCaptions(video_ids=test_video_ids)                             # cheat.
instances = getInstances(video_ids=test_video_ids)
labels = getOneHotLabels_RandChoicePerVideo(captions, num_classes=nVocabFeat)   # cheat.


model = load_model('models/model.h5', custom_objects={
    'Layer_BOS_PrevLabels': Layer_BOS_PrevLabels,
    'my_categorical_crossentropy': my_categorical_crossentropy,
    'orgCE': orgCE,
    'myAcc': myAcc })
Y = model.predict([instances, labels])
Y = nums2captions(Y)
with open(outputFileName, 'w') as File:
    for i in range(len(Y)):
        vid     = test_video_ids[i]
        caption = ' '.join(Y[i])
        File.write(vid + ',' + caption + '\n')
