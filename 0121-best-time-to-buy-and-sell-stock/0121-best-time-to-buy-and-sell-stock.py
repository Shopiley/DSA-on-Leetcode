class Solution:
    def maxProfit(self, prices: List[int]) -> int:
     
        #Brute force approach: will cause TLE for extremely large input array - possible cause: nested for loop
        max_diff = 0
    
        for i in range(len(prices)):                                                           
            for j in range(len(prices)):
                if j > i:
                    diff = prices[j] - prices[i]
                    
                    if diff > max_diff:
                        max_diff = diff
                        
        return max_diff
    
    
        # two pointers mechanism: left, right
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right  # we always want left to be the minimum, so if there's any lesser value we encounter, we want that to be our left (use [2,1,2,1,0,1,2])
            else:
                max_profit = max(max_profit, profit)
            right += 1
                
        return max_profit
            
"""               
    check here for explanation:      
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1735550/Python- Javascript-Easy-solution-with-very-clear-Explanation     
""" 


