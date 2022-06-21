from mimetypes import MimeTypes
import matplotlib.pyplot as plt
from midiutil import MIDIFile
import math
from music21 import midi
import music21

def makeMidi(source_filename, Out_filename, tempo=120, MINOTETIME=0, test=False, add_lyrics=False):
    track = 0
    channel = 0
    time = 0
    volume = 100
    MyMIDI = MIDIFile(1, eventtime_is_ticks=True, removeDuplicates=False, file_format=1)
    MyMIDI.addTempo(track, time, tempo)
    MyMIDI.ticks_per_quarternote = 960
    MyMIDI.addTempo(track, 0, tempo)
    #960 ticks per quarter note
    source = make_source(source_filename)
    datDuration = []
    datNote = []
    last = 0
    lastStart = 0
    for i in range(len(source)):
        if(source[i][1] != last):
            datDuration.append(i - lastStart)# 0.01s per tick
            if i - lastStart >= MINOTETIME:
                datNote.append(last)
            else:
                datNote.append(0)
            lastStart = i
            last = source[i][1]
    datDuration.append(len(source) - lastStart)
    datNote.append(last)
    for j in range(0, 2):
        for i in range(len(datNote)):
            if i != 0 and i != len(datNote)-1 and datNote[i-1]==datNote[i+1] and datNote[i] ==0 and datDuration[i] >= MINOTETIME:
                changed = True
                datNote[i] = datNote[i-1]

    if test:
        for i in range(len(datDuration)):
            print("{} {}".format(datDuration[i], datNote[i]))
        px = []
        py = []
        pz = []
        now = 0
        for i in range(len(datDuration)):
            for j in range(now, datDuration[i]):
                px.append(j)
                py.append(datNote[i])
                pz.append(source[j][1])
            now = now + datDuration[i]
        plt.plot(px, py, 'r')
        plt.plot(px, pz, 'b')
        plt.show()

    for i in range(len(datDuration)):
        duration = math.floor(datDuration[i] / (6000 / (tempo * MyMIDI.ticks_per_quarternote)))
        if datNote[i] != 0:
            MyMIDI.addNote(track, channel, datNote[i], time, duration, volume)
            if test:
                print("at {} {} {}".format(time, datNote[i], duration))
        time = time + duration
            
    with open(Out_filename, "wb") as output_file:
        MyMIDI.writeFile(output_file)

def range_to_midinote(pinch):
    if pinch < 160: 
        return 0
    elif 160 <= pinch < 180: # f
        return 53
    elif 190 <= pinch < 210: # g
        return 55
    elif 218 <= pinch < 235: # a
        return 57
    elif 240 <= pinch < 275: # c1
        return 60
    elif 285 <= pinch < 320: # d1
        return 62
    elif 330 <= pinch < 375: # f1
        return 65
    elif 385 <= pinch < 402: # g1
        return 67
    elif 410 <= pinch < 500: # a1
        return 69
    else:
        return 0

def trim_pinch(pinch):
    if pinch < 160: 
        return 0
    elif 160 <= pinch < 175: # f
        return 170
    elif 190 <= pinch < 205: # g
        return 195
    elif 218 <= pinch < 235: # a
        return 225
    elif 240 <= pinch < 270: # c1
        return 250
    elif 285 <= pinch < 310: # d1
        return 295
    elif 335 <= pinch < 365: # f1
        return 350
    elif 385 <= pinch < 402: # g1
        return 390
    elif 410 <= pinch < 450: # a1
        return 420

def make_source(filename):

    timeline = []
    note = []
    with open(filename, "r") as f:
        for line in f:
            timeline.append(float(line.split(" ")[0]))
            note.append(range_to_midinote(float(line.split(" ")[1])))
    # with open("save.npy", "r") as f:
    #     x = numpy.load(f)
    #     timeline = x[:,0]
    #     note = x[:,1]
    return list(zip(timeline, note))

def print_source(source):
    for i in range(len(source)):
        print("{} {}".format(source[i][0], source[i][1]))

def save_source(source, filename):
    with open(filename, "w") as f:
        for i in range(len(source)):
            f.write("{} {}\n".format(source[i][0], source[i][1]))

def draw_source(filename, begin, len):
    x = []
    y = []
    z = []
    timeline = []
    note = []
    with open(filename, "r") as f:
        for line in f:
            timeline.append(float(line.split(" ")[0]))
            note.append(float(line.split(" ")[1]))
    for i in range(int(begin*100), int((begin + len)*100)):
        x.append(timeline[i])
        y.append(note[i])
        z.append(trim_pinch(note[i]))
    plt.plot(x, y, 'r')
    plt.plot(x, z, 'b')
    plt.show()

def test():
    makeMidi("frequency.txt", "test.mid", tempo=100, MINOTETIME=5)
    draw_source("frequency.txt",0 , 6)



if __name__ == "__main__":
    test()