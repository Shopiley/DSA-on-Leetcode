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
    
    
    
# O(n log(n))
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def helper(length):
            s, l = 0, 0
            for r in range(len(nums)):
                s += nums[r]
                if r - l + 1 == length:
                    if s >= target: return True
                    s -= nums[l]
                    l += 1
            return False 
                
        l, r, res = 1, len(nums), 0 
        while l <= r:
            mid = l + (r - l) // 2 
            if helper(mid):
                r = mid - 1
                res = mid
            else: 
                l = mid + 1 
        return res
        

            
