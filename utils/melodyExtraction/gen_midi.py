import argparse
from ast import Try
from makeMidi import makeMidi
import os

def parser():
    p = argparse.ArgumentParser()
    p.add_argument('-o', '--output_dir',
                   help='Path to output folder (default: %(default)s',
                   type=str, default='./midi_new/')
    p.add_argument('-i', '--input_dir',
                   help='frequency files (default: %(default)s',
                   type=str, default='./results/')
    return p.parse_args()

if __name__ == '__main__':
    args = parser()
    for files in os.listdir(args.input_dir):
        name = files.replace("pitch_", "").replace('.txt', '').replace(".wav", "")
        print("./align/dataset"+name[0:4]+"/word_onsets/"+name)
        if files.endswith('.txt') and os.path.exists("./align/dataset"+name[0:4]+"/word_onsets/"+name+".txt"):
            makeMidi(args.input_dir + files, args.output_dir + files.replace("pitch_", "").replace('.txt', '.mid').replace(".wav", ""), tempo=100, MINOTETIME=5, add_lyrics=True)