import wizardhat.transform as transform
import pandas as pd

for i in range(0,5):
    holder = pd.read_csv("MyData/TimeSeries" + str(i) + "_Muse-EEG_0.csv")
    data[i] = holder

