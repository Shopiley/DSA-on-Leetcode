class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        """
        intiialize two pointers left= 0, right = 1
        currLen = 1
        maxLen = 0
        checker = " "

        compare left and right:
            if left < right:
                if checker != "<":
                    checker = <
                    currLen += 1
                else:
                    currlen = 2
        """

        left = 0
        right = 1
        currLen = 1
        maxLen = 0
        checker = ""


        while (right < len(arr)):
            if arr[left] < arr[right] and checker != "<":
                    checker = "<"
                    currLen += 1

            elif arr[left] > arr[right] and checker != ">":
                    checker = ">"
                    currLen += 1

            else:
                if arr[left] == arr[right]:  
                    maxLen = max(maxLen, currLen)                
                    currLen = 1
                else:
                    maxLen = max(maxLen, currLen)
                    currLen = 2
                
            left += 1
            right += 1

        return max(maxLen, currLen)








