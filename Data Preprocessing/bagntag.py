import pandas as pd
import os
import numpy as np
import csv

electrodeData = []

for patient in range(1, 4):
    data = pd.read_csv("Muse Data/p"+str(patient)+"_f_EEG.csv") #Read data from csv
    #data = data.values #convert pandas dataframe to numpy array
    electrodeData.append(data)
    date = pd.read_csv("Muse Data/p" + str(patient) + "_r_EEG.csv")  # Read data from csv
    #data = data.values  # convert pandas dataframe to numpy array
    electrodeData.append(data)

electrodeData = pd.DataFrame(electrodeData)
electrodeData.to_csv('electrodeData.csv')


def bag_and_tag(num_of_patients):
    focus_relaxed= []
    labels = []
    for i in range(num_of_patients +1):
        # we can take away the above loop if we use os.listdir (".")  as this just gets everything in the folder,
        # depends if patients exist
        for subfolders in os.listdir("Patient" + str(i+1)):
            trial_count = 0
            for trials in range(0, len(subfolders), 2):
                file_data = pd.read_csv(trials)
                tagged.append((trial_count, file_data.shape, len(file_data[0])))
