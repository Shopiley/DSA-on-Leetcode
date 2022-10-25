class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create a hash map
        #iterate through the array
        #check the value r for which target - values in our hash map (false cause hashmap is empty the first time): return index of r in hash map
        #store values:index in the hash map 
        
        # for i in range(len(nums)):
        #     r = target - nums[i]
        #     if r in nums:
        #         if nums.index(r) != i:
        #             return (i, nums.index(r))
        
        
        for i in range(len(nums)):
            r = target - nums[i]
            if r in nums and nums.index(r) != i:
                return [i, nums.index(r)]
        
        
        
        # for i in range(0, len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         # if j <= i:
        #         #     continue
        #         if (nums[j] == target - nums[i]):
        #             return (i, j)
        