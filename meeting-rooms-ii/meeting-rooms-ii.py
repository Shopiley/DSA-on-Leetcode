from heapq import heapify, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # basically the number of overlapping intervals
        # group non-overlapping intervals

    # intervals = [[0,30],[5,10],[15,20]]

    # heap = [10, 30]
        intervals.sort()

        heap = []
        heappush(heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heap[0] = intervals[i][1]
                heapify(heap)

            else:
                heappush(heap, intervals[i][1])

        return len(heap)

            

            


        