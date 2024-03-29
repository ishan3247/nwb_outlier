## todo: get rid of NANs

from pynwb import NWBFile
from pynwb import NWBHDF5IO
from std import nwb_metric
import os

import warnings
warnings.filterwarnings("ignore")

# check if the supplied filepath is a valid path for an nwb document
def valid_path(path):

    if len(path)<4:
        print('not a valid filepath')
        return False

    if path[-4:] == '.nwb':
        return True
    
    print('not a valid filepath')
    return False
    


while 1:
    x = input(">>> ")
    if x == 'exit':
        break

    entry = x.split(' ')

    if entry[0] == 'file':
        if len(entry) == 1:
            print('no path specified')
            continue
        filepath = entry[1]
        if not valid_path(filepath): continue
        io = NWBHDF5IO(filepath, 'r')
        nwbfile_in = io.read()

        # this code scans the acquisition for timeseries datasets
        acquisition_fields = set()
        for obj in nwbfile_in.acquisition:
            acquisition_fields.add(obj)
        for obj in nwbfile_in.objects.values():
            # print('%s: %s "%s"' % (obj.object_id, obj.neurodata_type, obj.name))
            if obj.neurodata_type == 'TimeSeries' and obj.name in acquisition_fields:
                print(obj.name)

        # print(nwbfile_in)

    # for field in acquisition_fields:\

    if x in acquisition_fields:
        data = nwbfile_in.acquisition[x]
        print(data.data[:])
        print(str(x) + " STD is: " +
              str(nwb_metric.check_spread(nwb_metric, data.data[:])))
        print(str(x) + " prob jumps is: " +
              str(nwb_metric.prob_jumps(nwb_metric, data.data[:])))
        print(str(x) + " saturation is: " +
              str(nwb_metric.check_saturation(nwb_metric, data.data[:])))
