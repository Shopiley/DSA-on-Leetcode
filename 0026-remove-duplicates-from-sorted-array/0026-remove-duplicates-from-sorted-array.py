class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        """
        initialize a pointer to 1
        """
        
        pointer = 1

        for i in range(1, len(nums)):

            if nums[i-1] != nums[i]:
                nums[pointer] = nums[i]
                pointer += 1

        return len(nums[0:pointer])