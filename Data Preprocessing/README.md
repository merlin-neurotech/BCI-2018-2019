# Data Preprocessing Subteam #

This folder is for preparing the scripts that will process the raw eeg data into features for the classifier

Take raw data and convert it into the following tuple: [Samples, Electrode, Timesteps, Features]

The main data transformation is obtaining the power spectral density of the EEG data. Including accelerometer and gyroscope data features may be necessary depending on noise due to movement.
