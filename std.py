import statistics
import math as m


class Tests:

    def check_spread(self, data):
        return statistics.stdev(data)

    def count_jumps(self, data):
        max_data = max(data)
        jumps = 0
        for i in range(len(data)):
            if i < len(data)-1:
                val = abs(data[i]-data[i+1])
                print(val)
                if val > 0.01*max_data:
                    jumps += 1
        return jumps

    def prob_jumps(self, data):
        jumps = self.count_jumps(self, data)
        if float(jumps/len(data)) > 0.001:
            return "There are too many jumps: " + str(jumps)
        else:
            if float(jumps/len(data)) != 0:
                return "There are some jumps: " + str(jumps)
            else:
                return "There are no jumps"
