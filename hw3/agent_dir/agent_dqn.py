from agent_dir.agent import Agent
import numpy as np
from keras import backend as K

class Agent_DQN(Agent):
    def __init__(self, env, args):
        """
        Initialize every things you need here.
        For example: building your model
        """

        super(Agent_DQN,self).__init__(env)

        # action_id is in [action_first, action_first+action_size).
        # For example, set action_first = 2 and action_size = 2 for Pong.
        self.action_first = 0
        self.action_size  = self.env.action_space.n

        self.lr            = args.learning_rate
        self.epochs        = args.training_epochs
        self.gamma         = args.discount_factor
        self.grad_avg      = args.gradient_average
        self.update_steps  = args.update_steps
        self.update_target = args.target_update_ratio

        self.batch_size  = args.batch_size
        self.exp_size    = args.exp_size
        self.epsilon     = args.epsilon
        self.epsilon_min = args.epsilon_min
        self.epsilon_off = args.epsilon_off

        self.isDoubleDQN = True

        self.model_dir = args.model_dir
        if args.model_id is not None:
            self.model_id = args.model_id
        self.model = self._build_model()
        self.ledom = self._build_model()

        self._num_stt_size = np.prod(self.env.observation_space.shape)

        if args.test_dqn:
            #you can load your model here
            print('loading trained model')
            print(self._model_path)
            self.model.load_weights(self._model_path)
            self.ledom.load_weights(self._model_path)
            # less exploration than training.
            self.epsilon = self.epsilon_min
        else:
            try:
                self.model.load_weights(self._model_path)
                self.ledom.load_weights(self._model_path)
                print('\n* Has loaded existed model. *\n')
            except:
                self.model.summary()
                print('\n* Create a new model. *\n')


    def init_game_setting(self):
        """

        Testing function will call this function at the begining of new game
        Put anything you want to initialize if necessary

        """
        ##################
        # YOUR CODE HERE #
        ##################
        pass


    def train(self):
        """
        Implement your training algorithm here
        """
        scores = []
        total_steps = 0

        for i_epoch in range(self.epochs):
            print('Epoch %d/%d' % (i_epoch+1, self.epochs))

            epoch_TU = False

            step_rs = []
            step_ls = []
            self.init_game_setting()
            observation = self.env.reset()
            while True:
                action = self.make_action(observation, test=False)

                observation_, reward, done, info = self.env.step(action)
                self._store_transition(observation, action, reward, done, observation_)
                observation = observation_
                step_rs     += [ reward ]

                if self._exp_full and (self._exp_ptr % self.update_steps == 0):
                    loss, isTargetUpdated = self._replay_exp()
                    step_ls  += [ loss ]
                    epoch_TU = epoch_TU or isTargetUpdated

                if done is True:
                    break

            scores += [ np.sum(step_rs) ]
            print('  score: %s' % scores[-1], end='')
            print(', steps: %d' % len(step_rs), end='')
            total_steps += len(step_rs)
            print('/%d' % total_steps, end='')
            print(', epsilon: %7.5f' % self.epsilon, end='')
            if self._exp_full:
                print(', loss: %6.4f' % np.sum(step_ls), end='')
            print('')      # A newline.

            if epoch_TU:
                print('')

        self.model.save_weights(self._model_path)
        print('')
        return scores


    def make_action(self, observation, test=True):
        """
        Return predicted action of your agent

        Input:
            observation: np.array
                stack 4 last preprocessed frames, shape: (84, 84, 4)

        Return:
            action: int
                the predicted action from trained model
        """
        if np.random.uniform() < self.epsilon:
            # epsilon-greedy policy.
            action_id = np.random.choice(self.action_size)
        else:
            observation = np.expand_dims(observation, axis=0)
            Q_actions   = self.model.predict(observation)
            action_id   = np.argmax(Q_actions)

        if test is not True:
            self.epsilon = max((1 - self.epsilon_off)*self.epsilon, self.epsilon_min)

        return action_id + self.action_first
        # return self.env.get_random_action()


    """CUSTOM FUNCTIONS
    """

    def _build_model(self):
        from keras.models import Model
        from keras.layers import Input, Flatten
        from keras.layers.core import Dense
        from keras.layers.convolutional import Convolution2D
        from keras.layers.advanced_activations import LeakyReLU
        from keras.optimizers import Adam, SGD, RMSprop

        myOpt = Adam(lr=self.lr)
        # myOpt = SGD(lr=self.lr)
        # myOpt = RMSprop(lr=self.lr)

        OB = Input(shape=self.env.observation_space.shape)
        if False:
            # https://github.com/keon/policy-gradient/blob/master/pg.py
            # ~ 31 ms/step.
            x = Convolution2D(filters=32, kernel_size=(6, 6), strides=3,
                               activation='relu', padding='same', kernel_initializer='he_uniform')(OB)
            x = Flatten()(x)
            x = Dense(units=64, activation='relu', kernel_initializer='he_uniform')(x)
            x = Dense(units=32, activation='relu', kernel_initializer='he_uniform')(x)
        else:
            # https://github.com/tokb23/dqn/blob/master/dqn.py
            # ~ 53 ms/step.
            x = Convolution2D(filters=32, kernel_size=(8, 8), strides=4,
                               activation='relu', padding='same', kernel_initializer='he_uniform')(OB)
            x = Convolution2D(filters=64, kernel_size=(4, 4), strides=2,
                               activation='relu', padding='same', kernel_initializer='he_uniform')(x)
            x = Convolution2D(filters=64, kernel_size=(3, 3), strides=1,
                               activation='relu', padding='same', kernel_initializer='he_uniform')(x)
            x = Flatten()(x)
            x = Dense(units=512, kernel_initializer='he_uniform')(x)
            x = LeakyReLU(alpha=0.1)(x)
        Q = Dense(units=self.action_size, activation='linear')(x)

        model = Model(inputs=OB, outputs=Q)
        model.compile(loss=self._my_masked_mse, optimizer=myOpt)
        return model

    def _store_transition(self, state, action, reward, done, state_):
        if hasattr(self, '_exp_ptr') is False:
            self._exps_stts  = np.empty(shape=(self.exp_size, np.prod(state.shape)))
            self._exps_acts  = np.empty(shape=(self.exp_size, 1), dtype=np.uint8)
            self._exps_rs    = np.empty(shape=(self.exp_size, 1), dtype=np.int8)
            self._exps_undos = np.empty(shape=(self.exp_size, 1), dtype=np.uint8)
            self._exps_stts_ = np.empty(shape=(self.exp_size, np.prod(state.shape)))
            self._exp_ptr    = 0
            self._exp_full   = False

        undone = 0 if done is True else 1
        # ~ 1600 ms/step.
        # self._exps[self._exp_ptr] = np.concatenate((state.ravel(), [action, reward, undone], state_.ravel()))
        # ~ 1000 ms/step.
        self._exps_stts[self._exp_ptr]  = state.ravel()
        self._exps_acts[self._exp_ptr]  = action
        self._exps_rs[self._exp_ptr]    = reward
        self._exps_undos[self._exp_ptr] = undone
        self._exps_stts_[self._exp_ptr] = state_.ravel()

        self._exp_ptr += 1
        if self._exp_ptr >= self.exp_size:
            self._exp_ptr -= self.exp_size
            if self._exp_full is False:
                self._exp_full = True
                print('* Experience is full. *')

    def _replay_exp(self):
        if hasattr(self, '_replay_cnt') is False:
            self._replay_cnt = 0

        # Sample a mini-batch from experience w/ replacement.
        batch_idxs = np.random.choice(self.exp_size, size=self.batch_size)

        # Decompose the mini-batch.
        batch_stts  = self._exps_stts[batch_idxs].reshape( (-1, ) + self.env.observation_space.shape )
        batch_acts  = self._exps_acts[batch_idxs]       # (batch_size, 1)
        batch_rs    = self._exps_rs[batch_idxs, 0]      # (batch_size, )
        batch_undos = self._exps_undos[batch_idxs, 0]   # (batch_size, )
        batch_stts_ = self._exps_stts_[batch_idxs].reshape( (-1, ) + self.env.observation_space.shape )

        from keras.utils import np_utils
        Q_next = self.ledom.predict(batch_stts_)                    # Q(s', a') from target-network.
        if self.isDoubleDQN:
            # a' of Q(s', a') is from online-network.
            # Q is still from target-network.
            Q_actions_ = self.model.predict(batch_stts_)
            actions_   = Q_actions_.argmax(axis=-1)
            Q_next     = Q_next[range(self.batch_size), actions_]   # (batch_size, )
        else:
            Q_next = Q_next.max(axis=-1)                            # (batch_size, )
        Q_target   = batch_rs + batch_undos * self.gamma * Q_next   # (batch_size, )
        Q_target[Q_target == 0.] = 1e-100                           # make sure self._my_masked_mse works.
        Q_target   = np.expand_dims(Q_target, axis=-1)              # (batch_size, 1)
        batch_acts = np_utils.to_categorical(batch_acts, num_classes=self.action_size)
        batch_acts *= Q_target

        losses = self.model.train_on_batch(batch_stts, batch_acts)
        loss   = losses[0] if isinstance(losses, list) else losses

        self._replay_cnt += 1
        # Save weights of the model for online-network.
        # Reset weights of the model for target-network.
        if self._replay_cnt % self.update_target == 0:
            self.model.save_weights(self._model_path)
            # self.ledom.load_weights(self._model_path)
            self.ledom.set_weights(self.model.get_weights())
            isTargetUpdated = True
        else:
            isTargetUpdated = False

        return loss, isTargetUpdated

    @property
    def _env_id(self):
        return self.env.env.spec.id

    @property
    def _model_filename(self):
        if hasattr(self, 'model_id'):
            return 'dqn_%s.%d.h5' % (self._env_id, self.model_id)
        return 'dqn_%s.h5' % self._env_id

    @property
    def _model_path(self):
        from os.path import join
        return join(self.model_dir, self._model_filename)


    def _my_masked_mse(self, y_true, y_pred):
        # [Shape]
        # y_true: (None, num_actions)
        from keras.losses import mean_squared_error

        # Create a one-hot mask.
        mask = K.cast(K.not_equal(y_true, 0.), K.floatx())

        n_acts = K.cast(K.tf.shape(y_true)[-1], K.floatx())     # Cancel averaging mse.

        if self.grad_avg is False:
            steps = K.cast(K.tf.shape(y_true)[0], K.floatx())   # Cancel averaging gradients.
        else:
            steps = K.constant(1.)
        return steps * n_acts * mean_squared_error(y_true, mask*y_pred)
