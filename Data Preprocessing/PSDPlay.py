import wizardhat.transform as transform
import pandas as pd
import numpy as np

data = []

def get_windowed(data, n_fft):
    data_centered = data - np.mean(data, axis=0)
    window = np.hamming
    window = window(n_fft).reshape((n_fft, 1))
    data_windowed = data_centered * window
    return data_windowed


def getPSD(data, n_fft):
    data_windowed = get_windowed(data, n_fft)
    data_fft = np.fft.rfft(data_windowed, n=self.n_fft, axis=0)
    data_fft /= n_fft
    psd = 2 * np.abs(data_fft)
    return psd

for i in range(1,8):
    holder = pd.read_csv("MyData/TimeSeries" + str(i) + "_Muse-EEG_0.csv")
    fft = []
    for t in range(0, len(holder)):
      fft.append(getPSD(holder[None,i], len(holder)))
data.append(fft)
print(data)



