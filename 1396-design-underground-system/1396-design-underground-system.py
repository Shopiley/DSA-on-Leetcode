class UndergroundSystem:

    def __init__(self):
        self.delimiter = ","
        self.arrivals = {}
        self.averages = {} # => A,B: totalhrs, pCount
                

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.arrivals[id] = (id, stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        arrivalEvent = self.arrivals[id]
        del self.arrivals[id]
        
        time_diff = t - arrivalEvent[2]
        
        key = arrivalEvent[1] + self.delimiter + stationName
        
        if key not in self.averages:
            self.averages[key] = (time_diff, 1)
        else:
            totalhrs, pCount = self.averages[key]
            totalhrs += time_diff
            pCount += 1  
            self.averages[key] = (totalhrs, pCount)
       

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + self.delimiter + endStation
        
        totalhrs, pCount = self.averages[key]
        
        return totalhrs/pCount
        
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)