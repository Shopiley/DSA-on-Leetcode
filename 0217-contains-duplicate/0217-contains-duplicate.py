class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            dict[num] = 1 + dict.get(num, 0)
        for val in dict.values():
            if val > 1:
                return True
        return False