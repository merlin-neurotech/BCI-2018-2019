from scipy import signal
import pandas as pd
import numpy as np

<<<<<<< HEAD
spectrogramData = []
PSDData = []
fs = 256  #Sampling frequency. Calculated manually


for i in range(1,8):
    electrodeData = pd.read_csv("MyData/TimeSeries"+str(i)+"_Muse-EEG_0.csv") #Read data from csv
    electrodeData = electrodeData.values #convert pandas dataframe to numpy array
    spectSample = []
    psdSample = []
    print(i)
    for k in range(1,6):
        f1, t, sxx = signal.spectrogram(x=electrodeData[:,k], fs=fs, nperseg=50, noverlap=40) #calculate spectrogram data
        f2, PSD = signal.welch(x=electrodeData[:,], fs=fs) #calculate PSD
        #Append data for electrode to overall sample with 5 electrodes
        spectSample.append(sxx)
        psdSample.append(PSD)
    #Append samples to transformed datasets
    spectrogramData.append(spectSample)
    PSDData.append(psdSample)

print(np.shape(spectrogramData))
print(np.shape(PSDData))



