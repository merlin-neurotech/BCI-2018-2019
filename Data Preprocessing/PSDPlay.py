from scipy import signal
from scipy import pi
import pandas as pd
import numpy as np

def bandpass(x, axis, low: float, high: float, transition: float, fs: float):
    #determine required order of filter and Wn,
    #Wn is a scalar or length-2 sequence giving the critical frequencies. For a Butterworth filter, this is the point at which the gain drops to to the -3dB point of the passband
    n, wn = signal.buttord(wp=[low*2/fs, high*2/fs], ws=[(low-transition)*2/fs, (high+transition)*2/fs], gpass=3, gstop=40, analog=False, fs=fs)
    b, a = signal.butter(N=n, Wn=wn, btype='bandpass', analog=False, output='ba', fs=fs)
    filteredSignal = signal.lfilter(b, a, axis)
    return filteredSignal


spectrogramData = []
PSDData = []
electrodeData = np.zeros()
fs = 256  #Sampling frequency. Calculated manually


for i in range(1,4):
    data = pd.read_csv("Muse Data/p"+str(i)+"_f_EEG.csv") #Read data from csv
    data = data.values #convert pandas dataframe to numpy array
    np.append(electrodeData, data, axis=2)
    date = pd.read_csv("Muse Data/p" + str(i) + "_r_EEG.csv")  # Read data from csv
    data = data.values  # convert pandas dataframe to numpy array
    np.append(electrodeData, data, axis=2)
    spectSample = []
    psdSample = []
    print(i)
    for k in range(1,6):
        f1, t, sxx = signal.spectrogram(x=electrodeData[:,k], fs=fs, nperseg=50, noverlap=20) #calculate spectrogram data
        f2, PSD = signal.welch(x=electrodeData[:,], fs=fs) #calculate PSD
        #Append data for electrode to overall sample with 5 electrodes
        spectSample.append(sxx)
        psdSample.append(PSD)
    #Append samples to transformed datasets
    spectrogramData.append(spectSample)
    PSDData.append(psdSample)

#NOTE: Output is spectrogramData and PSDData


