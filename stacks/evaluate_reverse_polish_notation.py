'''Evaluate Reverse Polish Notation
Solved

You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

    The operands may be integers or the results of other operations.
    The operators include '+', '-', '*', and '/'.
    Assume that division between integers always truncates toward zero.
    
'''

# Attempt 1: Stack Evaluation
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution0:
    def evalRPN(self, tokens: List[str]) -> int:
        # RPN The Operator follows the Operand. So (3 + 4) becomes (3 4 +)
        # To evaluate this, add the items to the stack in order, so Push 3, Push 4, Push +.
        # To then perform the calculation, every Operator pops the next two items from the stack.
        # Then perform the operation and push the result to the stack.
        stack = []

        for token in tokens:
            # Remove the negative temporarily so the isdigit can recognise negatives
            if token.lstrip('-').isdigit():
                # If an Operand, push to stack.
                stack.append(int(token))
            else:
                
                # Pop two items from stack.
                y = stack.pop()
                x = stack.pop()
                # Perform the calculation.
                result = 0
                if token == '+':
                    result = x + y
                elif token == '-':
                    result = x - y
                elif token == '*':
                    result = x * y
                elif token == '/':
                    result = x / y
                # Push the result to the stack.
                stack.append(int(result))
        
        # Return the only value left on the stack.
        return stack.pop()