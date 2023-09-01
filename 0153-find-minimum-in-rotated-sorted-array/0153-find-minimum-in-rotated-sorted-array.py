class Solution:
    def findMin(self, nums: List[int]) -> int:
        end = nums[len(nums)-1]
        mid = (len(nums)-1)//2
        
        if nums[mid] >= end:
            while nums[mid] > end:
                mid += 1
            return nums[mid]
        
        while nums[mid] < end:
            mid -= 1
        return nums[mid+1]
                
   
