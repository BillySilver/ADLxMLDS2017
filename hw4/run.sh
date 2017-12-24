if [ ! -d "models" ]; then
    mkdir models
fi
if [ ! -e "models/Generator.h5" ]; then
    # wget -O models/Generator.h5 ''
    echo 'models/Generator.h5 not existed!'
fi

PYTHON=python3.5
$PYTHON generate.py $1
