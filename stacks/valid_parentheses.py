'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
'''

# Attempt 1: Stack Backtracking
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution0:
    def isValid(self, s: str) -> bool:
        # Create stacks to hold each character
        stack = []
        open_brackets = ['(', '{', '[']
        
        for character in s:
            # If the character is an open bracket, add it to the stack.
            if character in open_brackets:
                stack.append(character)
            # If the character is a closed bracket, compare it to the top item on the stack
            # and if it is the correct closing character, pop the stack.
            elif len(stack) > 0:
                peek = stack[-1]
                if peek == '(' and character == ')':
                    stack.pop()
                elif peek == '{' and character == '}':
                    stack.pop() 
                elif peek == '[' and character == ']':
                    stack.pop() 
                else:
                    return False
            else:
                return False
        # If the stack is empty, the correct number sequence of brackets has occured.
        if len(stack) == 0:
            return True
        else:
            return False


        