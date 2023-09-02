class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        left, right = 0, 0
        p_map, s_map ={}, {}
        
        for i in range(len(p)):
            p_map[p[i]] = 1 + p_map.get(p[i], 0)
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
        
        res = [0] if s_map == p_map else [] 
        
        for right in range(len(p), len(s)):
            # decrease count of left
            s_map[s[left]] -= 1      
            
            # and/or remove entirely from dictionary
            if s_map[s[left]] == 0:
                s_map.pop(s[left])
                
            # increment left
            left += 1
            
            # update dictionary with right
            s_map[s[right]] = 1 + s_map.get(s[right], 0)
             
            # compare new s_map with p_map
            if p_map == s_map:
                res.append(left)    # record starting index
        
        return res
            
            
            
            

                
                    
            
        
        
                
        