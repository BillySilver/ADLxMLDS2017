def add_arguments(parser):
    '''
    Add your arguments here if needed. The TAs will run test.py to load
    your default arguments.

    For example:
        parser.add_argument('--batch_size', type=int, default=32, help='batch size for training')
        parser.add_argument('--learning_rate', type=float, default=0.01, help='learning rate for training')
    '''
    parser.add_argument('--learning_rate', type=float, default=0.001, help='learning rate for training')
    parser.add_argument('--training_epochs', type=int, default=4000, help='number of epochs for training')
    parser.add_argument('--discount_factor', type=float, default=0.99, help='discount factor a.k.a. gamma for future rewards')
    parser.add_argument('--gradient_average', action='store_true', help='whether average gradients for each batch')
    parser.add_argument('--update_epochs', type=int, default=1, help='[PG] update every n epochs')
    parser.add_argument('--model_dir', type=str, default='models/', help='directory for saving/loading model file')
    parser.add_argument('--model_id', type=int, default=None, help='specified id for model file')
    return parser
