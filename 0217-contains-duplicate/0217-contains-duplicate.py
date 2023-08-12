class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 0
            dict[num] += 1
        for val in dict.values():
            if val > 1:
                return True
        return False