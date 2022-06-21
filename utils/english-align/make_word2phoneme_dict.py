"""
Reads the .dict output file of the CMU pronunciation dictionary
and creates and saves a Python dictionary: dict[word] = phoneme.
"""

import pickle
import os

def make_word2phoneme_dict(dataset_name, tmpdir):
# read .txt-file with words and phonemes, make dict word2phonemes
    words2phonemes_file = open(os.path.join(tmpdir, '{}_word2phonemes.txt'.format(dataset_name)))
    lines = words2phonemes_file.readlines()

    word2phonemes = {}

    for line in lines:
        line = line.replace('\n', '').split('\t')

        word = line[0].lower().replace('’', "'")
        phonemes = line[1]
        word2phonemes[word] = phonemes

    # save dict
    pickle_out = open(os.path.join(tmpdir, "{}_word2phonemes.pickle".format(dataset_name)), "wb")
    pickle.dump(word2phonemes, pickle_out)
    pickle_out.close()