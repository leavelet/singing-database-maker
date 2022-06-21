from ctypes import util
import os

proj_root = ".."

thread_num = 10

path_of_origin = os.path.join(proj_root, "origin")
path_of_song = os.path.join(proj_root, "processed_data/vocal")
path_of_slice = os.path.join(proj_root, "processed_data/slice")
path_of_pitch = os.path.join(proj_root, "processed_data/pitch")
path_of_midi = os.path.join(proj_root, "processed_data/midi")
path_of_align = os.path.join(proj_root, "processed_data/align")

tmpdir = os.path.join(proj_root, "processed_data/tmp")

phoneme_from_word = os.path.join(proj_root, "make_dic")

cmudict_path = os.path.join(proj_root, "utils/english-align", "cmudict.txt")

path_of_mdx = os.path.join(proj_root, "utils/vocal-extraction")