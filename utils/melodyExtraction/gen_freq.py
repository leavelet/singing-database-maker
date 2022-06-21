import os
from melodyExtraction_NS import melodyExtraction_NS
import config
import threading

#notice: you should set up your environment before using this function

def gen_freq():
    file_list = []
    threads = []
    total = 0
    '''
    - path_of_slice
        - dir1
            - dir1.wav
            - dir1.txt
        - dir2
            - dir2.wav
            - dir2.txt
    - path_of_pitch
        - pinch_dir1.txt
        - pinch_dir2.txt
    '''
    for dir in os.listdir(config.path_of_slice):
        dir_final = os.path.join(config.path_of_slice, dir)
        if os.path.isdir(dir_final) and (not os.path.exists(os.path.join(config.path_of_pitch, "pitch_" + dir+".txt"))):
            # pitch_00131690317397.txt
            print(os.path.join(config.path_of_pitch, "pitch_" + dir+".txt"))
            file = os.path.join(dir_final, dir + ".wav")
            file_list.append(file)
            total += 1
    print("total: ", total)
    picenumber = int(total/config.thread_num)
    for i in range(config.thread_num):
        if i == config.thread_num - 1:
            file_list_sub = file_list[i*picenumber:]
        else:
            file_list_sub = file_list[i*picenumber:(i+1)*picenumber]
        t = threading.Thread(target=melodyExtraction_NS, args=(file_list_sub, config.path_of_pitch, 0))
        threads.append(t)
        t.start()

if __name__ == '__main__':
    gen_freq()