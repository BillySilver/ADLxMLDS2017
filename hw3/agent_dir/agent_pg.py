from agent_dir.agent import Agent
import scipy
import numpy as np
from keras import backend as K

def prepro(o, image_size=[80, 80], env_id=None):
    """
    Call this function to preprocess RGB image to grayscale image if necessary
    This preprocessing code is from
        https://github.com/hiwonjoon/tf-a3c-gpu/blob/master/async_agent.py

    Input:
    RGB image: np.array
        RGB screen of game, shape: (210, 160, 3)
    Default return: np.array
        Grayscale image, shape: (80, 80, 1)

    """
    # return preprocess(o)
    #
    if env_id in ['Pong-v0']:
        o = o[34:194]   # (160, 160, 3), only for Pong.
    y = 0.2126 * o[:, :, 0] + 0.7152 * o[:, :, 1] + 0.0722 * o[:, :, 2]
    y = y.astype(np.uint8)
    resized = scipy.misc.imresize(y, image_size)
    return np.expand_dims(resized.astype(np.float32) / 255., axis=2)

def preprocess(I):
    # Only for Pong.
    I = I[35:195]
    I = I[::2, ::2, 0]
    I[I == 144] = 0
    I[I == 109] = 0
    I[I != 0] = 1
    return np.expand_dims(I.astype(np.float), axis=2)


class Agent_PG(Agent):
    def __init__(self, env, args):
        """
        Initialize every things you need here.
        For example: building your model
        """

        super(Agent_PG,self).__init__(env)

        # action_id is in [action_first, action_first+action_size).
        # For example, set action_first = 2 and action_size = 2 for Pong.
        self.action_first = 0
        self.action_size  = self.env.action_space.n

        self.lr            = args.learning_rate
        self.epochs        = args.training_epochs
        self.gamma         = args.discount_factor
        self.grad_avg      = args.gradient_average
        self.update_epochs = args.update_epochs

        self.model_dir = args.model_dir
        if args.model_id is not None:
            self.model_id = args.model_id
        self.model = self._build_model()

        if args.test_pg:
            #you can load your model here
            print('loading trained model')
            print(self._model_path)
            self.model.load_weights(self._model_path)
        else:
            try:
                self.model.load_weights(self._model_path)
                print('\n* Has loaded existed model. *\n')
            except:
                self.model.summary()
                print('\n* Create a new model. *\n')


    def init_game_setting(self):
        """

        Testing function will call this function at the begining of new game
        Put anything you want to initialize if necessary

        """
        self.prev_ob   = None
        self.cur_state = None


    def train(self):
        """
        Implement your training algorithm here
        """
        isMultiRound = (self._env_id in ['Pong-v0'])
        scores = []

        for i_epoch in range(self.epochs):
            print('Epoch %d/%d' % (i_epoch+1, self.epochs))

            # Beginning of update-epochs.
            if i_epoch % self.update_epochs == 0:
                episode_stts = []
                episode_acts = []
                episode_rs   = []

            step_rs = []
            self.init_game_setting()
            observation = self.env.reset()
            while True:
                action = self.make_action(observation, test=False)

                observation, reward, done, info = self.env.step(action)
                episode_stts += [ self.cur_state ]     # Set by self.make_action()
                episode_acts += [ action - self.action_first ]
                step_rs      += [ reward ]

                if done is True:
                    break
            episode_rs += step_rs

            scores += [ np.sum(step_rs) ]
            print('  score: %s' % scores[-1], end='')
            if self.update_epochs > 1:
                print(', steps: %d' % len(step_rs), end='')
            print('\t', end='')

            # Ending of update-epochs.
            if ((i_epoch + 1) % self.update_epochs == 0) or (i_epoch + 1 == self.epochs):
                from keras.utils import np_utils
                episode_stts = np.concatenate(episode_stts, axis=0)
                episode_acts = np_utils.to_categorical(episode_acts, num_classes=self.action_size)
                episode_Qs   = self._discount_and_stdNormalize(episode_rs,
                                                               isMultiRound=isMultiRound,
                                                               with_mean=True,
                                                               with_std=True)
                episode_acts *= episode_Qs

                # Clip batch_size if excessive steps of episode will be over memory limit.
                batch_size = min(len(episode_stts), 21000)
                self.model.fit(episode_stts, episode_acts, batch_size=batch_size, epochs=1, verbose=1)
            else:
                print('')   # A newline.

            # Save weights of the model every 25 updates.
            if (i_epoch + 1) % (25*self.update_epochs) == 0 or (i_epoch + 1 == self.epochs):
                self.model.save_weights(self._model_path)
                print('')

        return scores


    def make_action(self, observation, test=True):
        """
        Return predicted action of your agent

        Input:
            observation: np.array
                current RGB screen of game, shape: (210, 160, 3)

        Return:
            action: int
                the predicted action from trained model
        """
        observation  = prepro(observation, env_id=self._env_id)
        state        = (observation - self.prev_ob) \
                        if self.prev_ob is not None \
                        else np.zeros_like(observation)
        state        = np.expand_dims(state, axis=0)
        self.prev_ob = observation
        if test is not True:
            self.cur_state = state      # Used by self.train() later.

        prob_actions = self.model.predict(state)
        action_id    = np.random.choice(self.action_size, p=prob_actions.ravel())
        return action_id + self.action_first
        # return self.env.get_random_action()


    """CUSTOM FUNCTIONS
    """

    def _build_model(self, image_size=[80, 80]):
        from keras.models import Model
        from keras.layers import Input, Flatten
        from keras.layers.core import Dense
        from keras.layers.convolutional import Convolution2D
        from keras.optimizers import Adam, SGD, RMSprop

        myOpt = Adam(lr=self.lr)
        # myOpt = SGD(lr=self.lr)
        # myOpt = RMSprop(lr=self.lr)

        # OB = Input(shape=self.env.observation_space.shape[ :-1] + (1, ))
        OB = Input(shape=tuple(image_size) + (1, ))
        if True:
            # https://github.com/keon/policy-gradient/blob/master/pg.py
            x = Convolution2D(filters=32, kernel_size=(6, 6), strides=3,
                               activation='relu', padding='same', kernel_initializer='he_uniform')(OB)
            x = Flatten()(x)
            x = Dense(units=64, activation='relu', kernel_initializer='he_uniform')(x)
            x = Dense(units=32, activation='relu', kernel_initializer='he_uniform')(x)
        else:
            # https://github.com/coreylynch/async-rl/blob/master/model.py
            x = Convolution2D(filters=16, kernel_size=(8, 8), strides=4,
                               activation='relu', padding='same', kernel_initializer='he_uniform')(OB)
            x = Convolution2D(filters=32, kernel_size=(4, 4), strides=2,
                               activation='relu', padding='same', kernel_initializer='he_uniform')(x)
            x = Flatten()(x)
            x = Dense(units=128, activation='relu', kernel_initializer='he_uniform')(x)
            # Additional.
            # x = Dense(units=32, activation='relu', kernel_initializer='he_uniform')(x)
        PI = Dense(units=self.action_size, activation='softmax')(x)

        model = Model(inputs=OB, outputs=PI)
        model.compile(loss=self._my_ce, optimizer=myOpt, metrics=[self._my_ce, self._my_loss1, self._my_loss2])
        return model

    @staticmethod
    def _grayscale_normalize(observation):
        if len(observation.shape) == 3:
            observation = np.expand_dims(observation, axis=0)
        return np.expand_dims(observation.dot([0.299, 0.587, 0.114]) / 255., axis=-1)

    def _discount_and_stdNormalize(self, episode_rs, isMultiRound=False,
                                   with_mean=True, with_std=True):
        episode_Qs = np.array(episode_rs, dtype=float)
        for t in reversed(range(episode_Qs.size - 1)):
            if isMultiRound is True and episode_Qs[t] != 0.:
                continue
            episode_Qs[t] += self.gamma * episode_Qs[t+1]

        if with_mean is True:
            episode_Qs -= episode_Qs.mean()
        if with_std is True:
            episode_Qs /= episode_Qs.std()
        return np.expand_dims(episode_Qs, axis=-1)

    @property
    def _env_id(self):
        return self.env.env.spec.id

    @property
    def _model_filename(self):
        if hasattr(self, 'model_id'):
            return 'pg_%s.%d.h5' % (self._env_id, self.model_id)
        return 'pg_%s.h5' % self._env_id

    @property
    def _model_path(self):
        from os.path import join
        return join(self.model_dir, self._model_filename)


    def _my_ce(self, y_true, y_pred):
        # [Shape]
        # y_true: (num_steps, num_actions)
        # Q:      (num_steps)

        Q = K.sum(y_true, axis=-1)

        # Let y_true just contain 0 or 1.
        y_true = K.cast(K.not_equal(y_true, 0.), K.floatx())

        if self.grad_avg is False:
            steps = K.cast(K.tf.size(Q), K.floatx())    # Cancel averaging gradients.
        else:
            steps = K.constant(1.)
        return steps * Q * K.categorical_crossentropy(y_true, y_pred) * K.constant(1. / self.update_epochs)

    # Useless.
    def _my_loss1(self, y_true, y_pred):
        """
        y_pred <- y_pred.     Q >= 0;
                  1 - y_pred, Q < 0.
        """
        y_pred = K.tf.where(K.tf.less(y_true, 0),
                            x=1. - y_pred,
                            y=y_pred)
        y_true = K.abs(y_true)

        if self.grad_avg is False:
            steps  = K.cast(K.tf.size( K.sum(y_true, axis=-1) ),
                            K.floatx())
        else:
            steps = K.constant(1.)
        return steps * K.categorical_crossentropy(y_true, y_pred) * K.constant(1. / self.update_epochs)

    # Useless.
    def _my_loss2(self, y_true, y_pred):
        """
        y_true <- [0 0 ... 0 1 0 ... 0 0], Q >= 0;
                  [1 1 ... 1 0 1 ... 1 1] / (n-1), Q < 0.
        """
        Q = K.sum(y_true, axis=-1)

        # Let y_true just contain 0 or 1.
        y_true = K.cast(K.not_equal(y_true, 0.), K.floatx())
        # If Q < 0, use complement of one-hot instead.
        y_comp = 1. - y_true
        y_comp /= K.sum(y_comp, axis=-1, keepdims=True)
        y_true = K.tf.where(K.tf.less(Q, 0),
                            x=y_comp,
                            y=y_true)

        if self.grad_avg is False:
            steps = K.cast(K.tf.size(Q), K.floatx())    # Cancel averaging gradients.
        else:
            steps = K.constant(1.)
        return steps * K.abs(Q) * K.categorical_crossentropy(y_true, y_pred) * K.constant(1. / self.update_epochs)
