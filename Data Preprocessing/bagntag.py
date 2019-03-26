import pandas as pd
import os
import numpy as np
import csv
from scipy import signal
import matplotlib.pyplot as plt


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = signal.lfilter(b, a, data)
    return y


def bag_and_tag(num_of_patients): #shrey wrote this
    matrices = []
    labels = []
    for i in range(num_of_patients +1):
        # we can take away the above loop if we use os.listdir (".")  as this just gets everything in the folder,
        # depends if patients exist
            f_data = pd.read_csv("Muse Data/p" + str(num_of_patients) + "_f_EEG.csv")
            r_data = pd.read_csv("Muse Data/p" + str(num_of_patients)+"_r_EEG.csv")
            f_data.drop(f_data.columns[[0, 4]], axis=1, inplace=True)
            r_data.drop(r_data.columns[[0, 4]], axis=1, inplace=True)
            f_data = f_data.transpose()
            r_data = r_data.transpose()
            labels.append(1)
        # 1 is focused, 0 is relaxed
            labels.append(0)
            matrices.append(f_data)
            matrices.append(  r_data)
    return matrices

electrodeData = bag_and_tag(3)
f1, t, sxx = signal.spectrogram(x=electrodeData[0], fs=256, nperseg=50, noverlap=20) #calculate spectrogram data
filt = butter_bandpass_filter(sxx[0,:,0], 2, 30, 256, 10)
#26 frequencies windows
plt.plot(f1, sxx[0,:,0])
plt.show()


# def main():
#     bag_and_tag(3)
#
#
# if __name__ == '__main__':
#     main()
