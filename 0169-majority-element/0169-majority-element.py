class Solution:
    def majorityElement(self, nums: List[int]) -> int:            
        
        majority = len(nums)//2  
        print(majority)
        hashMap = {}
        
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        
        print(hashMap)
        
        for key in hashMap:
            if hashMap[key] > majority:
                print(key, "answer")
                return key
                
            
        
            