# writen by 孙远航, under mit license
import config
import shutil
import make_word_list
import os
import shutil
import make_word2phoneme_dict
import align
import subprocess

if os.path.exists(config.path_of_align) == False:
    os.makedirs(config.path_of_align)

if os.path.exists(config.tmpdir) == False:
    os.makedirs(config.tmpdir)

for dir in os.listdir(config.path_of_slice):
    if not dir.startswith("."):
        make_word_list.make_word_list(os.path.join(config.path_of_slice, dir), config.tmpdir,dir)

cmd = config.phoneme_from_word + " " + config.cmudict_path + " " + config.tmpdir
print(cmd)
subprocess.call(cmd, shell=True)

shutil.copy(os.path.join(config.proj_root, "utils", "english-align", "phoneme2idx.pickle"), config.tmpdir)
shutil.copy(os.path.join(config.proj_root, "utils", "english-align", "model_parameters.pth"), config.tmpdir)

sum = 0;
for dir in os.listdir(config.path_of_slice):
    if dir.startswith(".") or os.path.exists(os.path.join(config.tmpdir, dir + "_word2phonemes.txt")) == False:
        continue
    sum += 1
    song_path = os.path.join(config.path_of_slice, dir)
    make_word2phoneme_dict.make_word2phoneme_dict(dir, tmpdir=config.tmpdir)
    align.align(audio_path=song_path, lyrics_path=song_path, dataset_name=dir, lyrics_format='w', onsets='pw', vad_threshold=0, output_dir=config.path_of_align, tmpdir=config.tmpdir )
print(sum)