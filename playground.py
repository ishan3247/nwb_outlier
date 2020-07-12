# this file is for testing the nwb api calls so we can translate them into the webpage with ease
import os
from dateutil.tz import tzlocal
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# nwb stuff
from pynwb import NWBFile
from pynwb import NWBHDF5IO
from std import nwb_metric


io = NWBHDF5IO('flask/nwb_files/test.nwb', 'r')
nwbfile_in = io.read()
print(nwbfile_in)

data = nwbfile_in.acquisition['flow']
data2 = nwbfile_in.acquisition['wheel']
# drop nan from data2
# data2 = data2[np.isfinite(data2)]
# data2 = data2[np.logical_not(np.isnan(data2))]

data3 = nwbfile_in.acquisition['TwoPhotonSeries1']
# drop nan from data3
# data3 = data3[np.isfinite(data3)]

print("flow STD is: " + str(nwb_metric.check_spread(nwb_metric, data.data[:])))
print("flow prob jumps is: " +
      str(nwb_metric.prob_jumps(nwb_metric, data.data[:])))
print("flow saturation is: " +
      str(nwb_metric.check_saturation(nwb_metric, data.data[:])))

print("wheel STD is: " +
      str(nwb_metric.check_spread(nwb_metric, data2.data[:])))
print("Wheel prob jumps is: " +
      str(nwb_metric.prob_jumps(nwb_metric, data2.data[:])))
print("Wheel saturation is: " +
      str(nwb_metric.check_saturation(nwb_metric, data2.data[:])))

print("two photon STD is: " +
      str(nwb_metric.check_spread(nwb_metric, data3.data[:])))
print("two photon prob jumps is: " +
      str(nwb_metric.prob_jumps(nwb_metric, data3.data[:])))
print("two photon saturation is: " +
      str(nwb_metric.check_saturation(nwb_metric, data3.data[:])))


'''
# currently nwbfile_in has the following fields
# Fields:
#   acquisition: {
#     test_timeseries <class 'pynwb.base.TimeSeries'>
#   }
#   file_create_date: [datetime.datetime(2018, 4, 15, 12, 0, tzinfo=tzoffset(None, -14400))]
#   identifier: TEST_TimeSeries
#   session_description: a file to test writing and reading a TimeSeries
#   session_start_time: 1971-01-01 12:00:00+00:00
#   timestamps_reference_time: 1971-01-01 12:00:00+00:00



# to dig deeper into the acquistion we do the following
# unsure why we need the brackets at end with test_timeseries
'''

# test_timeseries_in = nwbfile_in.acquisition['test_timeseries']

'''
# the acquistion has fields, note data and timestamp are hdf5 arrays
# this is a file format for large data files, although this one only has like 10
# Fields:
#   comments: no comments
#   conversion: 1.0
#   data: <HDF5 dataset "data": shape (10,), type "<i8">
#   description: no description
#   interval: 1
#   resolution: 0.1
#   timestamps: <HDF5 dataset "timestamps": shape (10,), type "<f8">
#   timestamps_unit: seconds
#   unit: SIunit

'''


# print("\n the time series data is \n \n", data)
# print('looking into the time_series data field we have')
# print("\n time stamps are \n", data.timestamps[:100])
# print("\n data are \n", data.data[:100])
# print("\n data are \n", data2.data[:100])
# print("\n data are \n", data3.data[:100])


# timestamp = [x for x in data.timestamps]
# data = [y for y in data.data]

# plt.plot(timestamp, data, 'ro')
# plt.show()


# print("STD is: " + str(nwb_metric.check_spread(nwb_metric, data3.data[:])))
# print(nwb_metric.prob_jumps(nwb_metric, data3.data[:]))
# print(nwb_metric.check_saturation(nwb_metric, data3.data[:]))

io.close()
