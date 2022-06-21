#!/bin/zsh
conda create -n freq python=3.8
conda create -n midi python=3.8
conda init zsh
source ~/.zshrc
conda activate freq
pip install -r requirements.txt
python gen_freq.py
conda activate midi
pip install requirements-midi.txt
mkdir midi
python gen_midi.py