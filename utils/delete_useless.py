#wirtten by: 孙远航 me@leavelet.io 2022-05-14
#description: 前面过程中发现了一些无效文件，对这些文件的关联文件进行删除
#version: 1.0
#under mit license

#warning: not tested yet, do not use!

import os
import shutil
import config

for dir in os.listdir(config.path_of_slice):
    if os.path.isdir(os.path.join(config.path_of_slice + dir)):
        if os.path.exists(os.path.join(config.path_of_pitch,  "pitch_" + dir + ".txt")) \
            and os.path.exists(os.path.join(config.path_of_align, dir, "phoneme_onsets", dir+'.txt')):
            continue
        else:
            print("delete " + dir)
            shutil.rmtree(os.path.join(config.path_of_slice, dir))
            if os.path.exists(os.path.join(config.path_of_pitch,  "pitch_" + dir + ".txt")):
                os.remove(os.path.join(config.path_of_pitch,  "pitch_" + dir + ".txt"))
            if os.path.exists(os.path.join(config.path_of_align, dir)):
                shutil.rmtree(os.path.join(config.path_of_align, dir))

            