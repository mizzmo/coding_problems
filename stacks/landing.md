# Stacks

## Problems

1. [Valid Parenthesis](/stacks/valid_parentheses.py)

## Prerequisites

- [Stacks](#python-stacks)

## Python Stacks

Stacks are a linear data structure that follows the LIFO principle, where the item that enters the list last is the first item to be removed from the list.

A stack can hold many elements and elements are added and removed from the top of the stack, think building a tower of lego bricks.

### Operations

1. Push - Add a new element to the top of the stack.
2. Pop - Remove and return the item at the top of the stack.
3. Peek - Return the top element of the stack without removing it.
4. isEmpty - Returns a boolean depending on if the stack is empty or not.
5. Size - Returns the number of elements in the stack.

### Implementation

Stacks can be implemented as either Arrays or Linked-Lists.
In Python, Lists have the available methods to be used as stacks

``` python
    # Creating a stack (List)
    stack = []
    # Pushing to a stack.
    stack.append('A')
    # Popping from a stack.
    element = stack.pop()
    # Peeking to a stack.
    peek = stack[-1]
    # isEmpty
    isEmpty = not bool(stack)
    # Size
    size = len(stack)
```
