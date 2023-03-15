# class UndergroundSystem:

#     def __init__(self):
#         self.delimiter = ","
#         self.arrivals = {}
#         self.averages = defaultdict(lambda: (0.0, 0)) # => A,B: totalhrs, pCount
                

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         self.arrivals[id] = (id, stationName, t)
        

#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         print(self.arrivals)
#         arrivalEvent = self.arrivals[id]
        
#         time_diff = t - arrivalEvent[2]
#         print("time_diff: ", time_diff)
        
#         key = arrivalEvent[1] + self.delimiter + stationName
        
#         # if key not in self.averages:
#         #     self.averages[key] = (time_diff, 1)
#         # else:
#         totalhrs, pCount = self.averages[key]
#         print("before: ", totalhrs, pCount)
#         totalhrs += time_diff
#         pCount += 1  
#         print("after: ", totalhrs, pCount)
#         self.averages[key] = (totalhrs, pCount)
       
#         print(self.averages)

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         key = startStation + self.delimiter + endStation
        
#         totalhrs, pCount = self.averages[key]
        
#         return totalhrs/pCount
        
        
class Event:
    def __init__(self,id, stationName, time):
        self.id = id
        self.stationName = stationName
        self.time = time
        
class Average: 
    def __init__(self, total, count):
        self.total = total
        self.count = count
        
    def updateAverage(self, diff):
        self.count += 1
        self.total += diff
        
    def getAverage(self):
        return self.total / self.count
        

class UndergroundSystem:

    def __init__(self):
        self.arrivals = defaultdict(list)
        self.averages = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.arrivals[id] = Event(id, stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        arrivalEvent = self.arrivals.get(id)
        self.arrivals.pop(id)
        
        diff = t - arrivalEvent.time
        
        key = (arrivalEvent.stationName, stationName)
        
        average = self.averages[key] if key in self.averages else Average(0, 0)
        average.updateAverage(diff)
        
        self.averages[key] = average
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        
        return self.averages.get(key).getAverage()        


# # Your UndergroundSystem object will be instantiated and called as such:
# # obj = UndergroundSystem()
# # obj.checkIn(id,stationName,t)
# # obj.checkOut(id,stationName,t)
# # param_3 = obj.getAverageTime(startStation,endStation)