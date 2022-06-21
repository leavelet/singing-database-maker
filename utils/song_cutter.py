#wirtten by: 孙远航 me@leavelet.io 2022-05-14
#description: 按歌词分割歌曲
#version: 1.0
#under mit license

import song_processor
import config
import os

if not os.path.exists(config.path_of_slice):
    os.mkdir(config.path_of_slice)

if not os.path.exists(config.path_of_pinch):
    os.mkdir(config.path_of_pinch)

for file in os.listdir(config.path_of_song):
    if file.endswith(".wav"):
        song = song_processor.song_processor(config.path_of_song + file)
        song.seperate()