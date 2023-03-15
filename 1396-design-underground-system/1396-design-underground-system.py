# class UndergroundSystem:

#     def __init__(self):
#         self.delimiter = ","
#         self.arrivals = {}
#         self.averages = {} # => A,B: totalhrs, pCount
                

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         self.arrivals[id] = (id, stationName, t)
        

#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         print(self.arrivals)
#         arrivalEvent = self.arrivals[id]
#         del self.arrivals[id]
        
#         time_diff = t - arrivalEvent[2]
#         print("time_diff: ", time_diff)
        
#         key = arrivalEvent[1] + self.delimiter + stationName
        
#         if key not in self.averages:
#             self.averages[key] = (time_diff, 1)
#         else:
#             totalhrs, pCount = self.averages[key]
#             print("before: ", totalhrs, pCount)
#             totalhrs += time_diff
#             pCount += 1  
#             print("after: ", totalhrs, pCount)
#             self.averages[key] = (totalhrs, pCount)
       
#         print(self.averages)

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         key = startStation + self.delimiter + endStation
        
#         totalhrs, pCount = self.averages[key]
        
#         return totalhrs/pCount
        
class UndergroundSystem:
    def __init__(self):
        self.check_in = {}
        self.times = defaultdict(lambda: (0.0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        src, t1 = self.check_in[id]
        dst = stationName
        curr_avg, curr_freq = self.times[(src, dst)]
        curr_avg = (curr_avg * curr_freq + (t - t1)) / (curr_freq + 1)
        self.times[(src, dst)] = (curr_avg, curr_freq + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.times[(startStation, endStation)][0]        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)