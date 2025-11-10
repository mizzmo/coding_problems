
'''
Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Each function should run in O(1)O(1) time.
'''
# Attempt 1
# Time Complexity: O(n)
# Space Complexity: O(n)
class MinStack0:

    stack = []

    def __init__(self):
        # Define a empty stack
        self.stack = []

    def push(self, val: int) -> None:
        # Push an item to the back of the stack
        self.stack.append(val)

    def pop(self) -> None:
        # Remove an item from the end of the stack
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]

    def getMin(self) -> int:
        min = self.stack[0]
        for item in self.stack:
            if item < min:
                min = item
        return min
        
        
# Attempt 2: Two stacks for min tracking
# Time Complexity: O(1)
# Space Complexity: O(n)
class MinStack1:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Add new value to end of stack
        self.stack.append(val)
        # Handle first instance
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            # Append the smaller of the new value or the old min.
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        # Pop both stacks
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return last value is stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return last value in min stack
        return self.min_stack[-1]


# Model Answer: Two Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class MinStackM:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
