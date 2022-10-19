class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers mechanism: left, right
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left = right  # we always want left to be the minimum (use [2,1,2,1,0,1,2])
                right += 1
            else:
                if profit > max_profit:
                    max_profit = profit
                right += 1
                
        return max_profit
            
             
            
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         buy day < sell day 
        
#         buy price < sell price
#         max(sell price - buy price)

        max_diff = 0
    
        for i in range(len(prices)):        #time limit exceeded for extremmely large input array - possible cause: nested for loop                                                   
            for j in range(len(prices)):
                if j > i:
                    diff = prices[j] - prices[i]
                    
                    if diff > max_diff:
                        max_diff = diff
                        
#         return max_diff
    
#         stock_dict = 
        
#         for day, price in enum(prices):


        
            
            
    
                    
    
    
    
    
    
    
    
    
    
        