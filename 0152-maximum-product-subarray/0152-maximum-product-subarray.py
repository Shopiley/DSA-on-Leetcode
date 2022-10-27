class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        currMax, currMin = 1, 1
        res = max(nums)
        
        for n in nums:
            temp = currMax*n
            currMax = max(currMax*n, currMin*n, n)
            currMin = min(temp, currMin*n, n)
            res = max(res, currMax)
            
        return res
            
            
        
        
        
        
        
        
        
#         [2, 3, -2, 4]
        
#         c, mult -> mult
#         2, 2 -> 2 up
#         3, 6 -> 6 up
#         -2, -12 -> -2
#         4, -2 -> 4 
        
#         [-2, 0, -1]
        
#         c, mult -> mult
#         -2, -2 -> -2 up
#         0, 0 -> 0 up
#         -1, 0 -> 0 up

        # [-2, 3, -4]
        # -2, -2 -> -2 up
        # 3, -6 -> 3 up
        # -4, -12 -> -4
        
        mult = 0
        temp = 1
        max_mult = -inf
        for c in nums:
            temp = temp*c
            mult = max(mult, temp)
            # print(mult)
            max_mult = max(mult, max_mult)
            print(max_mult)
        return max_mult
    
    
    
    
    
    
    
    
    
    
            