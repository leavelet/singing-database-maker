#wirtten by: 孙远航 me@leavelet.io 2022-05-14
#description: 从midi转换为有歌词的musicXML，有问题
#version: 0.1
#under mit license

from music21 import *
import os

#generate xmusicxml, write lyrcis to it

def gen_xml(file_name, output_dir):
    score = converter.parse(file_name).flatten()
    name = os.path.splitext(os.path.basename(file_name))[0]
    # lyrcfile = open("./processed_data/align/dataset"+name[0:4]+"/word_onsets/"+name+".txt", "r")
    # lyrc = lyrcfile.readlines()
    # lyrcfile.close()
    # word = []
    # time = []
    # for line in lyrc:
    #     word.append(line.split("\t")[0])
    #     time.append(float(line.split("\t")[1]))
    # word_time = list(zip(time, word))
    # print(word_time)
    # total_time = 0
    # for note in score.recurse().notesAndRests:
        
    #     # TODO : 明确offset，修正部分歌词的位置错误，正确处理一个单词多个音的情况。
    #     # 思路：必要的情况下使用音素和字母的对应关系，而不是全都使用歌词
    #     #属于重大缺陷，为了提高准确度必须修正

    #     timerange = (note.offset*1.25, note.offset * 1.25 + note.duration.quarterLength * 1.25)
    #     try :
    #         for i in range(len(word_time)):
    #             if timerange[0] <= word_time[i][0] and timerange[1] >= word_time[i][0]:
    #                 note.lyric = word_time[i][1]
    #                 print("write lyric:", word_time[i][1]) 
    #     except:
    #         pass
    score.write('musicxml', fp=output_dir+name)

if __name__ == "__main__":
    # data/musicxml_no_lric/00881300113172.musicxml
    gen_xml("./processed_data/midi_from_notes/00311468615250.mid", "./processed_data/musicxml/")

