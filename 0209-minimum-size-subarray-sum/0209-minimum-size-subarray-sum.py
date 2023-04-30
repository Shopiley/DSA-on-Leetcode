class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        currentSum = 0
        length = inf

        while right < len(nums):
            currentSum = currentSum + nums[right]
            while currentSum >= target:
                length = min(length, right-left+1)
                currentSum -= nums[left]
                left += 1
            
            right += 1

        return 0 if length==inf else length
        

            
