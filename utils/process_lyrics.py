#wirtten by: 孙远航 me@leavelet.io 2022-05-14
#description: lyrics processing
#version: 1.0
#under mit license

import pylrc_my as pylrc
import os

class lyrics_processer():

    def __init__(self, lyrics_file):
        try:
            lrc_file = open(lyrics_file)
            self.lrc_string = ''.join(lrc_file.readlines())
            lrc_file.close()
        except:
            raise RuntimeError("no lrc file found for " + lyrics_file)
        self.lrc_string = self.lrc_string.replace("&apos;", "'")
        self.subs = pylrc.parse(self.lrc_string)
        self.name = lyrics_file.split('.')[-1]

    def generator(self):
        for sub in self.subs:
            if len(sub.text) > 0 and (not sub.text.startswith('[tr:')) and (sub.text.find("：") == -1) and(sub.text.find("by") == -1):
                yield sub
            else:
                continue
    
    def output_to_lrc(self):
        lrc_string = self.subs.toLRC()
        try:
            lrc_file = open(self.name + "_processed.lrc","w")
            lrc_file.write(lrc_string)
            lrc_file.close()
        except:
            raise RuntimeError("failed to save " + self.name + "_processed.lrc")
    
    def print_lyrics(self):
        for sub in self.generator():
            print(sub.text)
            print(sub.minutes)
            print(sub.seconds)
            print(sub.milliseconds)
            print(sub.hours)

if __name__ == "__main__":
    for file in os.listdir("."):
        if file.endswith(".lrc"):
            x = lyrics_processer(file)
            for sub in x.subs:
                if(not (len(sub.text) >0  and (not sub.text.startswith('[tr:')))):
                    x.subs.pop(sub)
            x.output_to_lrc()
            