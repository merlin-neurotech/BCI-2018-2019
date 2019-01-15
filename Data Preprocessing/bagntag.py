import pandas as pd

for patient in range(0,10):
    data1 = pd.readcsv("Data/Patient", patient, "2019-01-15_TimeSeries_Muse-EEG_0.csv")
    print("Data/Patient" + str(patient) + "/2019-01-15_TimeSeries_Muse-EEG_0.csv")
    AllData[i] = data1
    AllData[]