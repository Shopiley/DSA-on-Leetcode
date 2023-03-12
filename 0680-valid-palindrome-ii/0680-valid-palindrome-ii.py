class Solution:
    def validPalindrome(self, s: int) -> bool:

        """
        initialize two pointers left, right at the start and end
        iterate from both front and back
        if str[left] != str[right]: 
            - (move left+1 and check sub palindrome) or (move right-1 and check sub palindrome) : if True, return TRUE;  if False, return FALSE

        return TRUE
        """

        left = 0
        right = len(s) - 1

        while (left <= right):
            if s[left] != s[right]:
                return self.subPalindrome(left+1, right, s) or self.subPalindrome(left, right-1, s)
            left += 1
            right -= 1
        return True
                

    def subPalindrome(self, left, right, s):

        while (left <= right):
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
    

   
