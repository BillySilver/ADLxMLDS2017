if [ ! -d "models" ]; then
    mkdir models
fi
if [ ! -e "models/model.h5" ]; then
    # wget -O models/model.h5 ''
    echo 'models/model.h5 not existed!'
fi

version=$(python -V 2>&1 | grep -Po '(?<=Python )\d')
if [ $version -eq 3 ]; then
    PYTHON=python
else
    PYTHON=python3
fi
$PYTHON hw2_seq2seq.py $1 $2 $3
