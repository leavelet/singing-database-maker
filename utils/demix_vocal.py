#wirtten by: 孙远航 me@leavelet.io 2022-06-21
#description: song dimixer
#version: 1.0
#under mit license

import subprocess
import os
import shutil
from config import *

#warning: you should set up your environment before using this function, follow the readme in utils/melodyExtraction
#warning: this programming will consume a lot of memory, at least 32G memory is required

for file in os.listdir(path_of_origin):
    if file.endswith(".flac") and (not os.path.exists(os.path.join(path_of_origin,file.split(".")[-2] + ".wav"))):
        cmd = "cd " + path_of_origin + " && ffmpeg -i " + "\"" + file + "\"" + " -ar 32000 " + " \"" + file.split(".")[-2] + ".wav" + "\" "
        print(cmd)
        subprocess.call(cmd, shell=True)

if not os.path.exists(os.path.join(path_of_mdx, "data/test")):
    os.makedirs(os.path.join(path_of_mdx, "data/test"))

for file in os.listdir(path_of_origin):
    if file.endswith("wav"):
        file_of_song = os.path.join(path_of_mdx, "data/test",  file.split(".")[-2])
        if not os.path.exists(file_of_song):
            os.mkdir(file_of_song)  
        shutil.copy(os.path.join(path_of_origin, file), file_of_song + "/mixture.wav")

cmd = "cd " + path_of_mdx + " && python3 predict_blend.py"
print(cmd)
subprocess.call(cmd, shell=True)

if not os.path.exists(path_of_song):
    os.mkdir(path_of_song)

dicOrigin = os.path.join(path_of_mdx, "data/results/baseline/")

for dic in os.listdir(dicOrigin):
    if os.path.isdir(dicOrigin + dic):
        os.rename(os.path.join(dicOrigin + dic, "vocals.wav"), os.path.join(path_of_song,  dic+".wav"))