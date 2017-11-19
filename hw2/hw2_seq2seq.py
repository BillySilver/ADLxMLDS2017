from hw2_init import *
from keras.models import load_model


try:
    outputFileName = sys.argv[2]
except:
    outputFileName = 'sample_output_testset.txt'


nVocabFeat = len(num2vocab)
instances, video_ids = getInstances()
fake_labels = getOneHotLabels_Fake(len(instances), maxText=41, num_classes=nVocabFeat)


model = load_model('models/model.h5', custom_objects={
    'BOSPadding': BOSPadding,
    'RecurrentWrapper': RecurrentWrapper,
    'Slicer': Slicer,
    'ArgmaxOneHot': ArgmaxOneHot,
    'ScheduleSampling': ScheduleSampling,
    'Attention': Attention,
    'my_categorical_crossentropy': my_categorical_crossentropy,
    'orgCE': orgCE,
    'myAcc': myAcc })
Y = model.predict([instances, fake_labels])
Y = nums2captions(Y)
with open(outputFileName, 'w') as File:
    for i in range(len(Y)):
        vid     = video_ids[i]
        caption = ' '.join(Y[i])
        File.write(vid + ',' + caption + '\n')


# For peer review. Only avaliable with set $3.
try:
    outputFileName = sys.argv[3]

    instances, video_ids = getInstances(peer_review=True)
    fake_labels = getOneHotLabels_Fake(len(instances), maxText=41, num_classes=nVocabFeat)

    Y = model.predict([instances, fake_labels])
    Y = nums2captions(Y)
    with open(outputFileName, 'w') as File:
        for i in range(len(Y)):
            vid     = video_ids[i]
            caption = ' '.join(Y[i])
            File.write(vid + ',' + caption + '\n')
except:
    pass
