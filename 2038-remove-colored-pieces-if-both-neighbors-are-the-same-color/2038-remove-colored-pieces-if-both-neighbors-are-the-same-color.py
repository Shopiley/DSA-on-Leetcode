class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        alice = 0
        bob = 0
        
        for i in range(0, len(colors)-2):
            if colors[i] == colors[i+1] == colors[i+2]:
                if colors[i] == "A":
                    alice += 1
                else:
                    bob += 1
        
        return alice - bob >= 1
    
"""
time complexity: O(n) where n = length of colors
space complexity: O(1)
"""
        
        
        

            
    
                
                
                