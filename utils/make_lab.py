#wirtten by: 孙远航 me@leavelet.io 2022-05-14
#description: 转换为音素的开始结束时间
#version: 1.0
#under mit license
import os
import librosa

def make_lab(name, file_name, endtime, output_dir):
    origin = open(file_name, 'r')
    lab_file = open(output_dir + name + '.lab', 'w')
    has_begin = False

    lines = origin.readlines()

    last_time = 0
    last_note = ""

    for line in lines:
        now_note = line.split()[0]
        now_time = float(line.split()[1])
        if not has_begin and (not now_note.startswith('>')):
            has_begin = True
            lab_file.write(str(int(0)) + " " + str(int(now_time*10e8)) + ' ' + "sil" + '\n')
            last_time = now_time
            last_note = now_note 
            continue
        if line.startswith('>') and has_begin:
            lab_file.write(str(int(last_time*10e8)) + " " + str(int(now_time*10e8)) + ' ' + last_note + '\n')
            last_time = now_time
            last_note = now_note
            continue
        if last_note == ">":
            lab_file.write(str(int(last_time*10e8)) + " " + str(int(now_time*10e8)) + ' ' + "pau" + '\n')
            last_time = now_time
            last_note = now_note
            continue
        if has_begin:
            lab_file.write(str(int(last_time*10e8)) + " " + str(int(now_time*10e8)) + ' ' + last_note + '\n')
            last_time = now_time
            last_note = now_note
    lab_file.write(str(int(last_time*10e8)) + " " + str(int(endtime*10e8)) + ' ' + "pau" + '\n')
    lab_file.close()

for dir in os.listdir("./slice/"):
    if not os.path.isdir("./slice/" + dir):
        continue
    # align/dataset0043/phoneme_onsets/00431604917711.txt
    origin_name = "./align/dataset{}/phoneme_onsets/{}.txt".format(dir[0:4], dir)
    if not os.path.exists(origin_name):
        raise RuntimeError("no! {}".format(origin_name))
    wave_file = "./slice/{}/{}.wav".format(dir, dir)
    y, sr = librosa.load(wave_file, sr=44100)
    endtime = librosa.get_duration(y, sr)
    make_lab(dir, origin_name, endtime, "./lab/")


            