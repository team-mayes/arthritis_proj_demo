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