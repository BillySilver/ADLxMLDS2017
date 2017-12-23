"""
Skip-Thought Vectors (Sequence encoder)
https://github.com/tensorflow/models/tree/master/research/skip_thoughts#download-pretrained-models-optional

If 'models/hair_eyes_vec.*' exist, this script does not need to be executed.
"""


from skip_thoughts import configuration
from skip_thoughts import encoder_manager
import os.path
import numpy as np
# Prepare for encoder.load_model().
import nltk
nltk.download('punkt')


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

data = valid_attrs['hair'] + valid_attrs['eyes']
for hair in valid_attrs['hair']:
    for eyes in valid_attrs['eyes']:
        data += [ (hair + ' ' + eyes) ]

def main():
    encoder = get_encoder()

    # Generate Skip-Thought Vectors for each sentence in the dataset.
    encodings = encoder.encode(data)

    np.save('models/hair_eyes_vec.npy', encodings)
    with open('models/hair_eyes_vec.txt', 'w') as file:
        for hair_eyes in data:
            file.write(hair_eyes + '\n')


def get_encoder():
    # Download and extract the bidirectional model. (shell script)
    # cd models/
    # wget "http://download.tensorflow.org/models/skip_thoughts_bi_2017_02_16.tar.gz"
    # tar -xvf skip_thoughts_bi_2017_02_16.tar.gz
    # rm skip_thoughts_bi_2017_02_16.tar.gz
    # cd ..
    #
    # Set paths to the model.
    pretrained_path = 'models/skip_thoughts_bi_2017_02_16/'
    VOCAB_FILE = os.path.join(pretrained_path, 'vocab.txt')
    EMBEDDING_MATRIX_FILE = os.path.join(pretrained_path, 'embeddings.npy')
    CHECKPOINT_PATH = os.path.join(pretrained_path, 'model.ckpt-500008')

    # Set up the encoder. Here we are using a single unidirectional model.
    # To use a bidirectional model as well, call load_model() again with
    # configuration.model_config(bidirectional_encoder=True) and paths to the
    # bidirectional model's files. The encoder will use the concatenation of
    # all loaded models.
    encoder = encoder_manager.EncoderManager()
    encoder.load_model(configuration.model_config(bidirectional_encoder=True),
                       vocabulary_file=VOCAB_FILE,
                       embedding_matrix_file=EMBEDDING_MATRIX_FILE,
                       checkpoint_path=CHECKPOINT_PATH)

    return encoder


if __name__ == '__main__':
    main()
