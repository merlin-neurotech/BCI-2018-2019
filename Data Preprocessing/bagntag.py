import pandas as pd
import numpy as np
import csv

electrodeData = []

for patient in range(1,4):
    data = pd.read_csv("Muse Data/p"+str(patient)+"_f_EEG.csv") #Read data from csv
    #data = data.values #convert pandas dataframe to numpy array
    electrodeData.append(data)
    date = pd.read_csv("Muse Data/p" + str(patient) + "_r_EEG.csv")  # Read data from csv
    #data = data.values  # convert pandas dataframe to numpy array
    electrodeData.append(data)

electrodeData = pd.DataFrame(electrodeData)
electrodeData.to_csv('electrodeData.csv')

