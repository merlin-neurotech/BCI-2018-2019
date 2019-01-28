from scipy import signal
import pandas as pd
import numpy as np

spectrogramData = []
PSDData = []
fs = 256  #Sampling frequency. Calculate manually


for i in range(1,8):
    electrodeData = pd.read_csv("MyData/TimeSeries"+str(i)+"_Muse-EEG_0.csv")
    electrodeData = electrodeData.values
    spectSample = []
    psdSample = []
    print(i)
    for k in range(1,6):
        f1, t, sxx = signal.spectrogram(x=electrodeData[:,k], fs=fs, nperseg=50, noverlap=40)
        f2, PSD = signal.welch(x=electrodeData[:,], fs=fs)
        print(np.shape(sxx))
        spectSample.append(sxx)
        psdSample.append(PSD)
    spectrogramData.append(spectSample)
    PSDData.append(psdSample)

print(np.shape(spectrogramData))
print(np.shape(PSDData))


