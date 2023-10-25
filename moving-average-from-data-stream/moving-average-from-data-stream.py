from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.size = size
        self.sum = 0
      

    def next(self, val: int) -> float:
        self.window.append(val)
        self.sum += val

        if len(self.window) > self.size:
            remove = self.window.popleft()
            self.sum -= remove
        
        return self.sum/len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

