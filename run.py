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

# print(nwbfile_in)


acquisition_fields= set()
for obj in nwbfile_in.acquisition:
    acquisition_fields.add(obj)

for obj in nwbfile_in.objects.values():
    # print('%s: %s "%s"' % (obj.object_id, obj.neurodata_type, obj.name))
    if obj.neurodata_type == 'TimeSeries' and obj.name in acquisition_fields:
        print(obj.name)




