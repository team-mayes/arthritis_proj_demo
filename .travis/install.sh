#!/usr/bin/env bash

if [[ $TRAVIS_OS_NAME == 'linux' ]]; then
    sudo apt-get update
fi
# We do this conditionally because it saves us some downloading if the
# version is the same.
if [[ "$PYTHON_VER" == "2.7" ]]; then
    wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O miniconda.sh;
else
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh;
fi

bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
hash -r
conda config --set always_yes yes --set changeps1 no
conda update -q conda
# Useful for debugging any issues with conda
conda info -a

conda create -q -n test-environment python=$PYTHON_VER pip pytest pytest-cov
source activate test-environment
python setup.py install

# Install pip only modules
pip install codecov