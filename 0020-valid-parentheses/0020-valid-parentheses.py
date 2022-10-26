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


        
        
        
# chudi's solution        
#         opened_stack = []
#         closed_stack = []
#         for bracket in s:
#             if bracket == "(" or bracket== "[" or bracket == "{":
#                 opened_stack.append(bracket)
#             elif bracket == ")" or bracket== "]" or bracket == "}":
#                 closed_stack.append(bracket)
                
#                 if len(opened_stack) == 0:
#                     return False
                
#                 opened_brac = opened_stack.pop()
#                 closed_brac = closed_stack.pop()
#                 elif ((opened_brac == "(") and ((closed_brac == "]") or (closed_brac == "}"))) :
#                     return False
#                 elif ((opened_brac == "[") and ((closed_brac == ")") or (closed_brac == "}"))) :
#                     return False
#                 elif ((opened_brac == "{") and ((closed_brac == "]") or (closed_brac == ")"))) :
#                     return False
#                 else:
#                     opened_stack.pop()
#                     closed_stack.pop()
#             if len(opened_stack) == 0:
#                 return True
                    

    
#               loop through s:
#                 if ( or [ or {:
#                     append to open
#                 elif ) or ] or }:
#                     append to close
#                     if len(open) == 0:
#                          return false
#                     elif open.pop() != close.pop():
#                          return false
#                     else:
#                          open.pop()
#                          close.pop()
                
#                 if len(open) == 0:
#                     return True
                                                      
                         
                         
                         
                         