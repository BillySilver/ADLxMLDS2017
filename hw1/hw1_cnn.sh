version=$(python -V 2>&1 | grep -Po '(?<=Python )\d')
if [ $version -eq 3 ]; then
    PYTHON=python
else
    PYTHON=python3
fi
$PYTHON hw1_cnn.py $1 $2
