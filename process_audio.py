import argparse
import os
import numpy
import glob

import matplotlib.pyplot as plt
import matplotlib.patches

import scipy.io.wavfile as wavfile

from pydub import AudioSegment

from pyAudioAnalysis import ShortTermFeatures as sF
from pyAudioAnalysis import MidTermFeatures as aF
from pyAudioAnalysis import audioTrainTest as aT
from pyAudioAnalysis import audioSegmentation as aS
from pyAudioAnalysis import audioVisualization as aV
from pyAudioAnalysis import audioBasicIO


orig_wav_path = '../voices/baltimore_full_w.wav'
output_wav_path = '../voices/baltimore_full_converted.wav'
# convert wav to mono and correct sample rate
sound = AudioSegment.from_file(orig_wav_path, format="wav")
sound = sound.set_channels(1)
sound = sound.set_frame_rate(16000)
sound.export(output_wav_path, format='wav')
print('Converted file - saved to {}'.format(output_wav_path))

hmmModelName = '../pyAudioAnalysis/pyAudioAnalysis/data/hmmRadioSM'
gtFile = output_wav_path.replace(".wav", ".segments")
output = aS.hmm_segmentation(output_wav_path, hmmModelName, plot_results=True,
                    gt_file=gtFile)

with open('process_out.txt', 'w') as f:
    for x in output:
        f.write(str(x))
        f.write('\n')
        print(x)
# segments = audioAnalysis.segmentclassifyFileWrapper('../voices/baltimore_full_w.wav', '../pyAudioAnalysis/pyAudioAnalysis/data/hmmRadioSM', 'hmm')