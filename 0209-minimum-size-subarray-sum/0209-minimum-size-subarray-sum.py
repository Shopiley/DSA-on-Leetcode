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
        

            
