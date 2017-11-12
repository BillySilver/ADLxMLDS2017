if [ ! -d "models" ]; then
    mkdir models
fi
if [ ! -e "models/model.h5" ]; then
    wget -O models/model.h5 'https://www.dropbox.com/s/1ofx29b7o6bji71/model03.h5?dl=1'
fi

version=$(python -V 2>&1 | grep -Po '(?<=Python )\d')
if [ $version -eq 3 ]; then
    PYTHON=python
else
    PYTHON=python3
fi
$PYTHON hw2_special.py $1 $2
