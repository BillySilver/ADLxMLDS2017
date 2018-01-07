if [ ! -d "models" ]; then
    mkdir models
fi
if [ ! -e "models/Generator.h5" ]; then
    wget -O models/Generator.h5 'https://www.dropbox.com/s/3n0um2a1wh0ihty/Generator.7.h5?dl=0'
    wget -O models/Discriminator.h5 'https://www.dropbox.com/s/wpvu2wlncq43ds2/Discriminator.7.h5?dl=0'
    # echo 'models/Generator.h5 not existed!'
fi

PYTHON=python3.5
$PYTHON generate.py "$@"
