"""
Generates a .txt-file with all unique words in a dataset. This .txt/file
can be used to translate words into phoneme sequences with the
CMU pronunciation dictionary (http://www.speech.cs.cmu.edu/tools/lextool.html)
"""

import argparse
import os
import glob

def make_word_list(lyrics, tmpdir, dataset_name='dataset1'):
    unique_words = set()

    lyrics_files = glob.glob(os.path.join(lyrics, '*.txt'))
    assert len(lyrics_files) > 0, 'No .txt-files found in {}'.format(lyrics)

    # go through .txt-files and save unique words in the unique_words set
    for file in lyrics_files:

        with open(file) as word_file:
            lines = word_file.readlines()
            for line in lines:
                line = line.lower().replace('\n', '').replace('’', "'")
                clean_line = ''.join(c for c in line if c.isalnum() or c in ["'", ' '])

                if clean_line == ' ' or clean_line == '': continue
                words = clean_line.split(' ')
                for word in words:
                    unique_words.add(word)

    if " " in unique_words:
        unique_words.remove(" ")

    # create .txt-file
    word_file_path = os.path.join(tmpdir, '{}_word_list.txt'.format(dataset_name))
    if(os.path.exists(word_file_path)):
        return
    # write words in .txt-file
    words_file = open(word_file_path, 'a')
    for word in sorted(unique_words):
        words_file.write(word.upper() + '\n')
    words_file.close()

    # create empty .txt-file which will contain the output of the CMU pronuciation dictionary.
    empty_file_path = os.path.join(tmpdir, '{}_word2phonemes.txt'.format(dataset_name))
    empty_file = open(empty_file_path, 'a')
    empty_file.write('')
    empty_file.close()
