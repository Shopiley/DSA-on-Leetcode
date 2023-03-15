class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if stack and stack[len(stack) - 1] == "(" and bracket == ")":
                stack.pop()

            elif stack and stack[len(stack) - 1] == "[" and bracket == "]":
                stack.pop()

            elif stack and stack[len(stack) - 1] == "{" and bracket == "}":
                stack.pop()

            else:
                stack.append(bracket)

        if len(stack) == 0:
            return True
        else:
            return False
 
        
