import ble2lsl
from ble2lsl.devices import muse2016
from wizardhat import acquire, transform

import numpy as np
import matplotlib.pyplot as plt


streamer = ble2lsl.Streamer(muse2016)


streamer.subscriptions

receiver = acquire.Receiver()

receiver.buffers


receiver.ch_names

receiver.buffers['EEG'].data



receiver.buffers['EEG'].data.shape

receiver.buffers['EEG'].unstructured

receiver.buffers['EEG'].get_timestamps()

our_first_recording = receiver.record(10)



our_first_recording.buffers['EEG'].data

raw = receiver.buffers['EEG'].data[-channel_to_view][-samples_to_view:]
time_raw = receiver.buffers['EEG'].data['time'][-samples_to_view:]



