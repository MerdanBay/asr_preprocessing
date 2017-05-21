#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import glob

sys.path.append('../')
sys.path.append('../../')
from prepare_path import Prepare
from utils.util import mkdir
from utils.config.make_config import setup


def main():

    prep = Prepare()

    wav_train_paths = prep.wav(data_type='train')
    wav_train_plus_paths = prep.wav(data_type='train_plus')
    wav_dev_paths = prep.wav(data_type='dev')
    wav_eval1_paths = prep.wav(data_type='eval1')
    wav_eval2_paths = prep.wav(data_type='eval2')
    wav_eval3_paths = prep.wav(data_type='eval3')
    wav_dialog_core_paths = prep.wav(data_type='dialog_core')
    wav_dialog_noncore_paths = prep.wav(data_type='dialog_noncore')

    save_train_path = mkdir(os.path.join(prep.fbank_path, 'train'))
    save_train_plus_path = mkdir(os.path.join(prep.fbank_path, 'train_plus'))
    save_dev_path = mkdir(os.path.join(prep.fbank_path, 'dev'))
    save_eval1_path = mkdir(os.path.join(prep.fbank_path, 'eval1'))
    save_eval2_path = mkdir(os.path.join(prep.fbank_path, 'eval2'))
    save_eval3_path = mkdir(os.path.join(prep.fbank_path, 'eval3'))
    save_dialog_core_path = mkdir(os.path.join(prep.fbank_path, 'dialog_core'))
    save_dialog_noncore_path = mkdir(
        os.path.join(prep.fbank_path, 'dialog_noncore'))

    # HTK settings
    setup(corpus='csj', feature='fbank', dim=40, sampling_rate=16000, window=0.025, slide=0.01,
          energy=True, delta=True, deltadelta=True, window_func='hamming')

    ##############################
    # train (basic)
    ##############################
    if len(wav_train_paths) == 0:
        raise ValueError('There are not any wav files.')
    with open('wav2fbank_train.scp', 'w') as f:
        for wav_path in sorted(wav_train_paths):
            speaker_name = wav_path.split('/')[-1].split('.')[0]
            save_path = os.path.join(save_train_path, speaker_name + '.htk')
            f.write(wav_path + '  ' + save_path + '\n')
    if len(wav_train_paths) != 986:
        raise ValueError('File number is not correct (True: 986, Now: %d).' %
                         len(wav_train_paths))

    ##############################
    # train (all = basic + plus)
    ##############################
    if len(wav_train_plus_paths) == 0:
        raise ValueError('There are not any wav files.')
    with open('wav2fbank_train_plus.scp', 'w') as f:
        for wav_path in sorted(wav_train_plus_paths):
            speaker_name = wav_path.split('/')[-1].split('.')[0]
            save_path = os.path.join(
                save_train_plus_path, speaker_name + '.htk')
            f.write(wav_path + '  ' + save_path + '\n')
    if len(wav_train_plus_paths) != 2226:
        raise ValueError('File number is not correct (True: 2226, Now: %d).' %
                         len(wav_train_plus_paths))

    ##############################
    # dev
    ##############################

    ##############################
    # eval1
    ##############################
    if len(wav_eval1_paths) == 0:
        raise ValueError('There are not any wav files.')
    with open('wav2fbank_eval1.scp', 'w') as f:
        for wav_path in sorted(wav_eval1_paths):
            speaker_name = wav_path.split('/')[-1].split('.')[0]
            save_path = os.path.join(save_eval1_path, speaker_name + '.htk')
            f.write(wav_path + '  ' + save_path + '\n')
    if len(wav_eval1_paths) != 10:
        raise ValueError('File number is not correct (True: 10, Now: %d).' %
                         len(wav_eval1_paths))

    ##############################
    # eval2
    ##############################
    if len(wav_eval2_paths) == 0:
        raise ValueError('There are not any wav files.')
    with open('wav2fbank_eval2.scp', 'w') as f:
        for wav_path in sorted(wav_eval2_paths):
            speaker_name = wav_path.split('/')[-1].split('.')[0]
            save_path = os.path.join(save_eval2_path, speaker_name + '.htk')
            f.write(wav_path + '  ' + save_path + '\n')
    if len(wav_eval2_paths) != 10:
        raise ValueError('File number is not correct (True: 10, Now: %d).' %
                         len(wav_eval2_paths))

    ##############################
    # eval3
    ##############################
    if len(wav_eval3_paths) == 0:
        raise ValueError('There are not any wav files.')
    with open('wav2fbank_eval3.scp', 'w') as f:
        for wav_path in sorted(wav_eval3_paths):
            speaker_name = wav_path.split('/')[-1].split('.')[0]
            save_path = os.path.join(save_eval3_path, speaker_name + '.htk')
            f.write(wav_path + '  ' + save_path + '\n')
    if len(wav_eval3_paths) != 10:
        raise ValueError('File number is not correct (True: 10, Now: %d).' %
                         len(wav_eval3_paths))
    ##############################
    # dialog (core)
    ##############################
    if len(wav_dialog_core_paths) == 0:
        raise ValueError('There are not any wav files.')
    with open('wav2fbank_dialog_core.scp', 'w') as f:
        for wav_path in sorted(wav_dialog_core_paths):
            speaker_name = wav_path.split('/')[-1].split('.')[0]
            save_path = os.path.join(
                save_dialog_core_path, speaker_name + '.htk')
            f.write(wav_path + '  ' + save_path + '\n')
    if len(wav_dialog_core_paths) != 30:
        raise ValueError('File number is not correct (True: 30, Now: %d).' %
                         len(wav_dialog_core_paths))

    ##############################
    # dialog (noncore)
    ##############################
    if len(wav_dialog_noncore_paths) == 0:
        raise ValueError('There are not any wav files.')
    with open('wav2fbank_dialog_noncore.scp', 'w') as f:
        for wav_path in sorted(wav_dialog_noncore_paths):
            speaker_name = wav_path.split('/')[-1].split('.')[0]
            save_path = os.path.join(
                save_dialog_noncore_path, speaker_name + '.htk')
            f.write(wav_path + '  ' + save_path + '\n')
    if len(wav_dialog_noncore_paths) != 80:
        raise ValueError('File number is not correct (True: 80, Now: %d).' %
                         len(wav_dialog_noncore_paths))


if __name__ == '__main__':
    main()
