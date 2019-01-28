from scipy import signal
import pandas as pd
import numpy as np

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


