"""
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- push(val) pushes the element val onto the stack.
- pop() removes the element on the top of the stack.
- top() gets the top element of the stack.
- getMin() retrieves the minimum element in the stack.

Constraints:
- Methods pop, top, and getMin will always be called on non-empty stacks.
"""
import unittest
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
# Test cases for MinStack

class TestMinStack(unittest.TestCase):
    def test_min_stack_operations(self):
        # Initialize MinStack
        min_stack = MinStack()

        # Test push operation
        min_stack.push(5)
        self.assertEqual(min_stack.top(), 5)
        self.assertEqual(min_stack.getMin(), 5)

        min_stack.push(3)
        self.assertEqual(min_stack.top(), 3)
        self.assertEqual(min_stack.getMin(), 3)

        min_stack.push(7)
        self.assertEqual(min_stack.top(), 7)
        self.assertEqual(min_stack.getMin(), 3)

        min_stack.push(3)
        self.assertEqual(min_stack.top(), 3)
        self.assertEqual(min_stack.getMin(), 3)

        # Test pop operation
        min_stack.pop()
        self.assertEqual(min_stack.top(), 7)
        self.assertEqual(min_stack.getMin(), 3)

        min_stack.pop()
        self.assertEqual(min_stack.top(), 3)
        self.assertEqual(min_stack.getMin(), 3)

        min_stack.pop()
        self.assertEqual(min_stack.top(), 5)
        self.assertEqual(min_stack.getMin(), 5)

        # Test pop until empty
        min_stack.pop()
        with self.assertRaises(IndexError):
            min_stack.top()
        with self.assertRaises(IndexError):
            min_stack.getMin()

if __name__ == "__main__":
    unittest.main()