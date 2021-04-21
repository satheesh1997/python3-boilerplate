#!/bin/sh

echo "Setting up the python3 boilerplate"
echo "Using python version 3.8.2"

if [ "$(python --version)" != "Python 3.8.2" ]
then
    echo "\n Python 3.8.2 is needed to setup this boilerplate code"
    echo "\n Install pyenv from https://github.com/pyenv/pyenv"
    echo "\n After installation run (pyenv install 3.8.2)"
    exit
fi

echo "1. Install requirements"
pip install -r requirements.txt

echo "2. Installing pre-commit hooks"
pre-commit install

echo "Setup complete :)"
echo "==============================================="
cat MANUAL.md
