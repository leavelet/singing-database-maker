#wirtten by: 孙远航 me@leavelet.io 2022-05-14
#description: 前面过程中发现了一些无效文件，对这些文件的关联文件进行删除
#version: 1.0
#under mit license

from logging import shutdown
import os
import shutil

for dir in os.listdir("./slice"):
    if os.path.isdir("./slice/" + dir):
        name = dir
        parent = dir[0:4]
        if os.path.exists("./pitch/" + name + ".pitch") \
            and os.path.exists("./align/dataset"+parent + "/phoneme_onsets/" + name + ".txt"):
            continue
        else:
            print("delete " + name)
            shutil.rmtree("./slice/" + name)
            if os.path.exists("./align/dataset"+parent + "/phoneme_onsets/" + name + ".txt"):
                os.remove("./align/dataset"+parent + "/phoneme_onsets/" + name + ".txt")
            if os.path.exists("./align/dataset"+parent + "/phoneme_offsets/" + name + ".txt"):
                os.remove("./align/dataset"+parent + "/phoneme_offsets/" + name + ".txt")
            if os.path.exists("./pitch/" + name + ".pitch"):
                os.remove("./pitch/" + name + ".pitch")
            