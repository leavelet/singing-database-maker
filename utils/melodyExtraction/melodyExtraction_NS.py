# -*- coding: utf-8 -*-
from tkinter.messagebox import NO
import numpy as np
import argparse
import os
from model import *
import librosa
from madmom.audio.signal import *
from pathlib import Path
import tensorflow as tf

def spec_extraction(file_name, win_size, x_train_mean, x_train_std):
    # print(currentFilePath)

    x_test = []

    # y, sr = librosa.load(file_name, sr=8000)
    # *********** madmom.Signal() is faster than librosa.load() ***********
    y = Signal(file_name, sample_rate=8000, dtype=np.float32, num_channels=1)
    S = librosa.core.stft(y, n_fft=1024, hop_length=80*1, win_length=1024)
    x_spec = np.abs(S)
    x_spec = librosa.core.power_to_db(x_spec, ref=np.max)
    x_spec = x_spec.astype(np.float32)
    num_frames = x_spec.shape[1]

    # for padding
    padNum = num_frames % win_size
    if padNum != 0:
        len_pad = win_size - padNum
        padding_feature = np.zeros(shape=(513, len_pad))
        x_spec = np.concatenate((x_spec, padding_feature), axis=1)
        num_frames = num_frames + len_pad

    for j in range(0, num_frames, win_size):
        x_test_tmp = x_spec[:, range(j, j + win_size)].T
        x_test.append(x_test_tmp)
    x_test = np.array(x_test)

    # for normalization

    x_test = (x_test-x_train_mean)/(x_train_std+0.0001)
    x_test = x_test[:, :, :, np.newaxis]

    return x_test, x_spec

def melodyExtraction_NS(file_list, output_path, gpu_index=None):
    currentFilePath = str(Path(__file__).resolve().parent)

    os.environ['CUDA_DEVICE_ORDER'] = 'PCI_BUS_ID'
    if gpu_index is None:
        os.environ['CUDA_VISIBLE_DEVICES'] = ''
    else:
        os.environ['CUDA_VISIBLE_DEVICES'] = str(gpu_index)

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

    note_res = 8
    pitch_range = np.arange(40, 95 + 1.0/note_res, 1.0/note_res)
    pitch_range = np.concatenate([np.zeros(1), pitch_range])
    x_train_mean = np.load(currentFilePath+'/x_data_mean_total_31.npy')
    x_train_std = np.load(currentFilePath+'/x_data_std_total_31.npy')

    model = melody_ResNet()
    model.load_weights(currentFilePath+'/weights/ResNet_NS.hdf5')

    for file_name in file_list:
        '''  Features extraction'''
        X_test, X_spec = spec_extraction(
            file_name=file_name, win_size=31, x_train_mean=x_train_mean, x_train_std=x_train_std)

        '''  melody predict'''
        tensor = tf.convert_to_tensor(X_test, dtype=tf.float32)
        y_predict = model(inputs=tensor)
        y_shape = y_predict.shape
        print(y_shape)
        num_total_frame = y_shape[0]*y_shape[1]
        est_pitch = np.zeros(num_total_frame)
        index_predict = np.zeros(num_total_frame)

        y_predict = np.reshape(y_predict, (num_total_frame, y_shape[2]))

        for i in range(num_total_frame):
            index_predict[i] = np.argmax(y_predict[i, :])
            pitch_MIDI = pitch_range[np.int32(index_predict[i])]
            if pitch_MIDI >= 53 and pitch_MIDI <= 69:
                est_pitch[i] = pitch_MIDI
        ''' save results '''
        PATH_est_pitch = output_path+ 'pitch_'+file_name.split('/')[-1].split('.')[-2]+'.txt'
        if not os.path.exists(os.path.dirname(PATH_est_pitch)):
            os.makedirs(os.path.dirname(PATH_est_pitch))
        f = open(PATH_est_pitch, 'w')
        for j in range(len(est_pitch)):
            est = "%.2f %.4f\n" % (0.01 * j, est_pitch[j])
            f.write(est)
        f.close()
        KK.clear_session()

def parser():
    p = argparse.ArgumentParser()
    p.add_argument('-p', '--filepath',
                   help='Path to input audio (default: %(default)s',
                   type=str, default='./vocals_2.wav')
    p.add_argument('-o', '--output_dir',
                   help='Path to output folder (default: %(default)s',
                   type=str, default='./')
    p.add_argument('-gpu', '--gpu_index',
                   help='Assign a gpu index for processing. It will run with cpu if None.  (default: %(default)s',
                   type=int, default=None)
    return p.parse_args()


if __name__ == '__main__':
    args = parser()
    melodyExtraction_NS(file_list=[args.filepath],
                        output_path=args.output_dir, gpu_index=args.gpu_index)