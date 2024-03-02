class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [num**2 for num in nums]
        
        return sorted(squared)
            
        