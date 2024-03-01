class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        """
        - must not end in 0
        - must end in 1
            - max combo of remaining digits
        - can have leading 0
        
        
        0101 -> {0:2, 1:2}, len=4
        
        1001
        
        0101011 -> {0:3, 1:4}, len=5
        
        1110001
        """
        ones = s.count('1')
        zeroes = s.count('0') 
        if ones == 0 or zeroes == 0:
            return s
        
        s = list(s)
        ans = [0 for i in range(len(s))] #[1110001]
        # freq_map = {}
        
        # for c in s:
        #     if c not in freq_map: #{0:0, 1:0}
        #         freq_map[c] = 0
        #     freq_map[c] += 1
        
        ans[-1] = '1'
        # freq_map['1'] -= 1
        ones -= 1
        idx = 0
            
        while ones > 0:
            ans[idx] = '1'
            ones -= 1
            idx += 1
            
        while zeroes > 0:
            ans[idx] = '0'
            zeroes -= 1
            idx += 1
            
        return ''.join(ans)
            
            
            
        
        