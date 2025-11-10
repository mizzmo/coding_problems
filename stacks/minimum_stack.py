
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
        
