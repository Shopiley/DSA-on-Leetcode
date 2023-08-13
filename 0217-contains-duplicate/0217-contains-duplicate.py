class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            dict[num] = 1 + dict.get(num, 0) # tries to get the value associated with the key num in the dictionary dict and increment by 1. If num is not already a key in the dictionary, it returns the default value 0.
        for val in dict.values():
            if val > 1:
                return True
        return False