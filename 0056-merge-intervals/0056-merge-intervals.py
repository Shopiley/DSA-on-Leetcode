class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        """
        1236
        intervals = [[1,4],[2,3],[8,10],[15,18]]
        1 2 3 4
        
        1 < 2 <= 3        
        
        """
        intervals.sort()
        i = 0
        while i < len(intervals)-1:
            max_start = max(intervals[i][0], intervals[i+1][0])
            min_end = min(intervals[i][1], intervals[i+1][1])
            
            if max_start <= min_end:                
                intervals[i+1] = [min(intervals[i][0], intervals[i+1][0]), max(intervals[i][1], intervals[i+1][1])]
                del intervals[i]
                
            else:
                i += 1

        return intervals
                
            
         