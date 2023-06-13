class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        """
        turn the array in a array of the frequency of each letter
        initalize a maxHeap and a Queue
        remove the max from the heap 
        subtract one from the value and add one to the time
        add the value and it's next available time to the queue
        pop the value from the queue and add to the maxHeap once it's time has reached
        return time
        """
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        
        while maxHeap or q:
            time += 1              
            if maxHeap:
                item = heapq.heappop(maxHeap)
                item += 1
                
                if item:
                    q.append((item, time+n))
                    
            if q and time == q[0][1]:
                move = q.popleft()
                heapq.heappush(maxHeap, move[0])
        return time
            
            
            