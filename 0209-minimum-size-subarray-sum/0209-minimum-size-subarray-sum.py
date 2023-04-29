class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0
        currentSum = nums[0]
        length = inf

        while right < len(nums):

            if currentSum >= target:
                length = min(length, right-left+1)

                if length == 1:
                    right += 1
                currentSum -= nums[left]
                left += 1               
                continue

            right += 1
            if right < len(nums):
                currentSum = currentSum + nums[right]

        return 0 if length==inf else length
        

            
