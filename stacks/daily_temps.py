'''
Daily Temperatures
Solved

You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

'''
# Attempt 1: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution0:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [[temperatures[0],0]]
        result = [0] * len(temperatures)

        # Add elements to the stack until a value higher than the highest value appears.
        # Remember the index of each value using a data structure.
        for i in range(1, len(temperatures)):
            # Peek at the value at the top of the stack
            value = stack[len(stack)-1][0]
            # Compare that value to the next index.
            if temperatures[i] <= value:
                # Add to stack if the value is not greater
                stack.append([temperatures[i], i])
            else:
                # For every value that the current value is greater than
                while True:
                    if temperatures[i] > value and len(stack) > 0:
                        # If greater, pop the stack.
                        index = stack.pop()
                        index = index[1]
                        # Compare the index of the popped value to that of the current element.
                        difference = i - index
                        # Put that value in the correct place in the array.
                        result[index] = difference
                        # Update value to be the next in the stack if not empty
                        if len(stack) > 0:
                            value = stack[len(stack)-1][0]
                    else:
                        break
                # Add the new value to the stack.
                stack.append([temperatures[i], i])
        
        return result
                
# Model Solution: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
