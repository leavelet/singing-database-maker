#wirtten by: 孙远航 me@leavelet.io 2022-05-14
#description: 分隔歌曲
#version: 1.0
#under mit license

from process_lyrics import *
from config import *
import subprocess
import librosa
import math

def addsplash(file):
    return "\"" + file + "\""

def getTime(sub):
    return round((sub.minutes * 60 * 1000 + sub.seconds * 1000 + sub.milliseconds) / 1000, 2)

class song_processor():
    '''
    input file is a song ending with wav.
    A lyrics in lrc format in the same folder is needed too.
    '''
    def __init__(self, file):
        lrc = file.replace(".wav", ".lrc")
        if (not os.path.exists(file)) or (not os.path.exists(lrc)):
            print(file.split('.')[-2]+".lrc")
            print("not found {}, please ensure both wav and lrc exists! ".format(file))
            exit(1)
        print("into {}".format(file))
        self.name = file.split("/")[-1].replace(".wav", "")
        self.lrc_processor = lyrics_processer(lrc)
        self.wav_path = self.name + ".wav"

    def seperate(self):
        print("seperating {}".format(self.name))
        for i in range(0, len(self.lrc_processor.subs)):
            print("{}/{}".format(i, len(self.lrc_processor.subs)))
            sub = self.lrc_processor.subs[i]
            #to filter empty or translate
            if(len(sub.text) == 0 or (sub.text.startswith('[tr:')) or (sub.text.find("：") != -1) or (sub.text.find("by") != -1)):
                continue
            beg_time = getTime(sub)
            if i == len(self.lrc_processor.subs) -1 :
                end_time = round(librosa.get_duration(filename=path_of_song + self.wav_path), 2)
            else :
                end_time = getTime(self.lrc_processor.subs[i+1])
            end_time = max(beg_time, end_time-0.05)
            #too short, something wrong
            if(end_time <= beg_time+0.5):
                print("too short, skip")
                continue
            #too long, just take 20 seconds
            if(end_time - beg_time >= 20):
                end_time = beg_time + 20
                print("too long, take 20 seconds")
            #format slicename
            slicename = self.name + str(int(beg_time*100)) + str(int(end_time*100))
            songpath = os.path.join(path_of_slice, slicename)
            os.makedirs(songpath)
            ffmpeg_begin = "{:02d}:{:02d}:{:02d}.{:03d}".format(0, sub.minutes, sub.seconds, sub.milliseconds)
            end_minute = int((end_time - beg_time))//60
            end_second = int(math.floor((end_time - beg_time)%60))
            end_mili =int(((end_time - beg_time) - end_minute*60 - end_second)*1000)
            ffmpeg_end = "{:02d}:{:02d}:{:02d}.{:03d}".format(0, end_minute, end_second, end_mili)
            cmd = "cd " + path_of_song + " && " + "ffmpeg -i " + addsplash(self.wav_path) + " -ss " + ffmpeg_begin + " -t " + ffmpeg_end + " -ac 1 -ar 32000 " + addsplash(slicename+ ".wav") + " && mv " + addsplash(slicename+ ".wav") + " " + addsplash(os.path.join("../slice/" + slicename, slicename + ".wav"))
            print(cmd)
            subprocess.call(cmd, shell=True)
            with open(os.path.join(songpath, slicename + ".txt"), "w") as t:
                print(sub.text, file=t)