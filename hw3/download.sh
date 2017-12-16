if [ ! -d "models" ]; then
    mkdir models
fi
if [ ! -e "models/pg_Pong-v0.h5" ]; then
    wget -O models/pg_Pong-v0.h5 'https://www.dropbox.com/s/vusy12h2p5drgy6/pg_Pong-v0.6.h5?dl=0'
    # echo 'models/pg_Pong-v0.h5 not existed!'
fi
if [ ! -e "models/dqn_BreakoutNoFrameskip-v4.h5" ]; then
    wget -O models/dqn_BreakoutNoFrameskip-v4.h5 'https://www.dropbox.com/s/giy2ty4fmtflm5m/dqn_BreakoutNoFrameskip-v4.12.h5?dl=0'
    # echo 'models/dqn_BreakoutNoFrameskip-v4.h5 not existed!'
fi
