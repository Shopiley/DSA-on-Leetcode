class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # nums = [1, 2, 2, 3, 4, 5]
        # [2, 1, 2], [2, 2, 3], [2, 3, 4]
        
        # sort nums
        # i = 0, j= 1, k=2 ;check if satifies condition
        # if nums > 3: pick 3 numbers such that a + b > c 
        # but if nums[i] == nums[j]== nums[k] continue
        # add one to all, then check again - while k < len(nums)
        # if true add the 3 numbers and append to newArray
        # max(newArray)
        
        
        
        nums = sorted(nums)
        n = len(nums)
        max_val = 0
        for i in range(n-2):
            j = i+1
            k = i+2
            if nums[i] + nums[j] > nums[k]:
                val = nums[i] + nums[j] + nums[k]
                if val > max_val:
                    max_val = val
        return max_val