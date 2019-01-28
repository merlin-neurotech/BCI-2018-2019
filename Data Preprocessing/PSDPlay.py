from scipy import signal
import pandas as pd
import numpy as np

data = []
fs = 256  #Sampling frequency. Calculate manually


for i in range(1,8):
    electrodeData = pd.read_csv("MyData/TimeSeries"+str(i)+"_Muse-EEG_0.csv")
    electrodeData = electrodeData.values
    sample = []
    print(i)
    for k in range(1,6):
        f, t, sxx = signal.spectrogram(x=electrodeData[:,k], fs=fs, nperseg=50, noverlap=40)
        print(np.shape(sxx))
        sample.append(sxx)

    data.append(sample)


