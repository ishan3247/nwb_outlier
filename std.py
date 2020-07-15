import statistics
import math
import matplotlib as plt


"""
next steps: autochecking for the correct datatypes
need ways to define specific phenomenon (like 90% stimulated outlier)
    would need to know about it in the first place in order to recognize 
"""

class nwb_metric:

    # checks if more than 10% of data is "close" to min or max values defined as within 1% of the range
    def check_saturation(self, data):
        max_data = max(data)
        min_data = min(data)
        close_distance = 0.01 * (max_data-min_data)
        count = 0
        for element in data:
            # if abs(element-max_data) <=1:
            #     count += 1

            if (max_data-element < close_distance) or (element - min_data < close_distance):
                count += 1

        if count/len(data) > 0.01:
            return "The data is highly saturated: " + str(count)
        else:
            return "The data is not highly saturated"

    def check_spread(self, data):
        return statistics.stdev(data)

    def count_jumps(self, data):
        max_data = max(data)
        jumps = 0
        for i in range(len(data)):
            if i < len(data)-1:
                diff = abs(data[i]-data[i+1])
                # either need to increase 0.01 or classify max_data as an outlier in order to reduce number of jumps identified
                if diff > float(0.01*max_data):
                    jumps += 1
        return jumps

    def prob_jumps(self, data):
        num_jumps = self.count_jumps(self, data)
        if num_jumps/len(data) > 0.001:
            return "There are too many jumps: " + str(num_jumps) + " jumps"
        elif math.ceil(num_jumps/len(data)):
            return "There are some jumps: " + str(num_jumps) + " jumps"
        else:
            return "There are no jumps"
            

    
