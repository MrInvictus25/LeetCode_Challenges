# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []  # Initialization a stack of S input. It is required to observe of opening brackets
        parentheses = {")": "(", "}": "{", "]": "["}  # Dictionary for keeping track of mappings.

        for element in s:
            if element in parentheses:  # It iterates keys and determines if the bracket is a closing or not
                if len(stack) > 0:  # I pop the upper element from the stack, if it is no empty
                    upperElement = stack.pop()  # It will be returned a removed element and assigned in a variable
                    #print(stack)

                else:
                    upperElement = 'Empty'

                if parentheses[element] != upperElement: # The checking if the opening bracket in the dictionary
                                                         # and the upper element corresponds each other
                    #print(parentheses[element])
                    #print(upperElement)
                    return False

            else:      # If it is an opening bracket I push it onto the stack.
                stack.append(element)
                #print(stack)
        if len(stack) == 0:
            return True  # If the stack is empty, consequently it is a valid expression

example = Solution()
print(example.isValid("([]){}"))

