# writen by 孙远航, under mit license

import shutil
import make_word_list
import os
import regex
import shutil
import make_word2phoneme_dict
import align
import librosa

for num in range(0, 89):
    if not os.path.exists('./lyrc/lyrics_{:04d}'.format(num)):
        os.mkdir('./lyrc/lyrics_{:04d}'.format(num))
    for dir in os.listdir("../data/songs"):
        re = "^{:04d}\S*$".format(num)
        print(re)
        if regex.match(re, dir):
            shutil.copy(os.path.join("../data/songs/" + dir, dir+".txt"), "lyrc/lyrics_{:04d}".format(num)+"/"+dir+".txt")
    print("making word list for dataset {}".format(num))
    make_word_list.make_word_list('lyrc/lyrics_{:04d}'.format(num), 'dataset{:04d}'.format(num))
    #python make_word2phoneme_dict.py --dataset-name NAME
    print("making word2phoneme dict for dataset {}".format(num))
    make_word2phoneme_dict.make_word2phoneme_dict('dataset{:04d}'.format(num))

for dir in os.listdir("../data/songs"):
    if not os.path.isdir("../data/songs/" + dir):
        continue
    f = open(os.path.join("../data/songs/"+dir, dir+".txt"), "r")
    lines = f.readlines()
    f.close()
    w = open(os.path.join("../data/songs/"+dir, dir+"_upper.txt"), "w")
    for line in lines:
        line = line.upper()
        w.write(line + '\n')
    w.close()
    os.remove(os.path.join("../data/songs/"+dir, dir+".txt"))
    os.rename(os.path.join("../data/songs/"+dir, dir+"_upper.txt"), os.path.join("../data/songs/"+dir, dir+".txt"))
if not os.path.exists("./tmp"):
    os.mkdir("./tmp")
for num in range(34, 89):
    song_path = "./tmp/song_{:04d}/".format(num)
    if not os.path.exists(song_path):
        os.mkdir(song_path)
    for dir in os.listdir("../data/songs"):
        re = "^{:04d}\S*$".format(num)
        if regex.match(re, dir):
            shutil.copy(os.path.join("../data/songs/" + dir, dir+".wav"), song_path+dir+".wav")
    print("aligning dataset {}".format(num))
    for txt in os.listdir("lyrc/lyrics_{:04d}".format(num)):
        print(txt)
        name = txt.split(".")[-2]
        if not os.path.exists(song_path+name+".wav") :
            shutil.move("lyrc/lyrics_{:04d}/".format(num) + txt, "./trash/"+txt)
            continue
        try:
            librosa.load(song_path+name+".wav")
        except RuntimeError:
            shutil.move(txt, "./trash/"+txt)
            continue
    try:
        align.align(audio_path=song_path, lyrics_path="lyrc/lyrics_{:04d}".format(num), dataset_name="dataset{:04d}".format(num), lyrics_format='w', onsets='pw', vad_threshold=0)
    except RuntimeError:
        print("omit the file")