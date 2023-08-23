class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # group into hash map
        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
        
        # sort hash map by key, produces a list of (key, value) pair in sets
        sortedMap = sorted(hashMap.items(), key=lambda x:x[1]) #[(1, 3), (2, 2), (3, 1)]
        
        # just trying smth out
        print(dict(sortedMap))
        
        #loop through to pick top k
        ans = []
        for i in range(k):
            ans.append(sortedMap[::-1][i][0])
        
        return ans
            
            
            
        