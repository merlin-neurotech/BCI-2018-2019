import pandas as pd
import os
import numpy as np
import csv

def bag_and_tag(num_of_patients): #shrey wrote this
    matrices = []
    labels = []
    for i in range(num_of_patients +1):
        # we can take away the above loop if we use os.listdir (".")  as this just gets everything in the folder,
        # depends if patients exist
            f_data = pd.read_csv("Muse Data/p" + str(num_of_patients) + "_f_EEG.csv")
            r_data = pd.read_csv("Muse Data/p" + str(num_of_patients)+"_r_EEG.csv")
            f_data.drop(f_data.columns[[0, 4]], axis=1, inplace=True)
            r_data.drop(r_data.columns[[0, 4]], axis=1, inplace=True)
            labels.append(1)
        # 1 is focused, 0 is relaxed
            labels.append(0)
            matrices.append(f_data)
            matrices.append(  r_data)

# def main():
#     bag_and_tag(3)
#
#
# if __name__ == '__main__':
#     main()
