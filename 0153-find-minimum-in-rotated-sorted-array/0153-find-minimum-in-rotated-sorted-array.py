class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high)//2
        
        if nums[mid] >= nums[low]:
            while mid < len(nums) and nums[mid] >= nums[low]:
                mid += 1
            if mid >= len(nums):
                return nums[low]
            return nums[mid]
        
        elif nums[mid] < nums[low]:
            while nums[mid] < nums[low]:
                mid -= 1
            return nums[mid+1]
   
