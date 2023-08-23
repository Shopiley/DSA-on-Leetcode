class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
        
        sortedMap = sorted(hashMap.items(), key=lambda x:x[1], reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(sortedMap[i][0])
        
        return ans
            
            
            
        