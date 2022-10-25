class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
    # time complexity O(n^2), inefficient for extremely large inputs
        # two pointers
        # max_sum = 0
        # pointer = 0
        # sum_sum = -2 + 1+ -3 ... + nums[len(nums)-1]
        # for loop for i to iterate through all the numbers
        # while loop for pointer to move forward through all the numbers on each iteration of i
        # take sum_sum
        # take max of sum_sum and max_sum for each sum_sum
        # replace max_sum with sum_sum
        # return max_sum
        
#         max_sum = float(-inf)
        
#         for i in range(len(nums)):
#             sum_sum = 0
#             pointer = i
#             while pointer < len(nums):
#                 sum_sum += nums[pointer]
#                 max_sum = max(sum_sum, max_sum)
#                 pointer += 1
#         return max_sum

# ----------------------------------------------------------------------------
# from discussions
    # class Solution:
    # def maxSubArray(self, nums):
    #     cur_max, max_till_now = 0, -inf
    #     for c in nums:
    #         cur_max = max(c, cur_max + c)
    #         max_till_now = max(max_till_now, cur_max)
    #     return max_till_now

# ------------------------------------------------------------------------- 
        # kadane's algorithm
        # bottle neck: doesn't work when the array has negative numbers only
        max_so_far = float("-inf")
        max_ending_here = 0
        
        for i in range(len(nums)):
            max_ending_here += nums[i]
            max_so_far = max(max_so_far, max_ending_here)

            if max_ending_here < 0:
                max_ending_here = 0     # hoping that we'll still find a positive no along the way

            

        return max_so_far
# ---------------------------------------------------------------------------

# from neetcode: kadane's but the if block is moved up

#         max_so_far = nums[0]
#         max_ending_here = 0
        
#         for i in range(len(nums)):
#             if max_ending_here < 0:
#                 max_ending_here = 0
            
#             max_ending_here += nums[i]
            
#             max_so_far = max(max_so_far, max_ending_here)
            
#         return max_so_far

# in a case where all the numbers in the array are positive, max_ending_here will just keep adding all the numbers together such that max_so_far will be the total sum of the array - which makes sense

# whereas, if all the numbers are negative, max_ending_here would have the values of the neg number on each iteration and dince we'd be comparing to max_so_far each time, max_so_far at the end of the day will be the single largest negative integer

# you're welcome future me!


















        
        