class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        alice = 0
        bob = 0
        left = 0 
        
        for right in range(3, len(colors)+1):
            window = colors[left:right]
            
            if window == "AAA":
                alice += 1
            elif window == "BBB":
                bob += 1
            left += 1
        
        print(alice, bob)
        return alice - bob >= 1
        
        
        

            
    
                
                
                