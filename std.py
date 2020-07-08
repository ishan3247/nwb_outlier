import statistics
import math as m


class Tests:

    def check_spread(self, data):
        return statistics.stdev(data)

    def count_jumps(self, data):
        max_data = max(data)
        print(max_data)
        jumps = 0
        for i in range(len(data)):
            if i < len(data)-1:
                val = abs(data[i]-data[i+1])
                if val > float(0.01*max_data):
                    # print(data[i])
                    # print(data[i+1])
                    jumps += 1
        return jumps

    def prob_jumps(self, data):
        jumps = self.count_jumps(self, data)
        print(float(jumps/len(data)))
        if float(jumps/len(data)) > 0.001:
            return "There are too many jumps: " + str(jumps)
        else:
            if float(jumps/len(data)) != 0:
                return "There are some jumps: " + str(jumps)
            else:
                return "There are no jumps"

    def check_saturation(self, data):
        max_data = max(data)
        count = 0
        for i in range(len(data)):
            if abs(data[i]-max_data) <= 1:
                count += 1
        if float(count/len(data)) > 0.01:
            return "The data is highly saturated: " + str(count)
        else:
            return "The data is not highly saturated"
