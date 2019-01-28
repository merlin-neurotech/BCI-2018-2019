from scipy import signal
import pandas as pd
import numpy as np

<<<<<<< HEAD
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
=======
data = []
fs = 256  #Sampling frequency. Calculated manually


for i in range(1,8):
    electrodeData = pd.read_csv("MyData/TimeSeries"+str(i)+"_Muse-EEG_0.csv") #read csv data file
    electrodeData = electrodeData.values #converts pandas data frame into numpy array
    sample = []
    print(i)
    for k in range(1,6):
        f, t, sxx = signal.spectrogram(x=electrodeData[:,k], fs=fs, nperseg=50, noverlap=40) #calculate spectrogram
        sample.append(sxx)
    data.append(sample)
>>>>>>> cbdcfb6f0c4c47397ce89879dd460a3714a397a8


