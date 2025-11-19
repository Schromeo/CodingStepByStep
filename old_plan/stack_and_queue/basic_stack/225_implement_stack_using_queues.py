"""
Implement the MyStack class to simulate a stack using only standard queue operations.

LeetCode 225 - Implement Stack using Queues

Design a stack that supports push, pop, top, and empty operations using only the basic operations of a queue:
- Push(x): Push element x onto stack.
- Pop(): Removes the element on top of the stack and returns that element.
- Top(): Get the top element.
- Empty(): Returns whether the stack is empty.

Constraints:
- You may use only standard queue operations (i.e., push to back, peek/pop from front, size, and is empty).
- All operations must be O(1) amortized time complexity.
- You may assume that all operations are valid (e.g., no pop or top operations will be called on an empty stack).
"""
from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        if not self.empty:
            return self.q[0]

    def empty(self) -> bool:
        return not self.q
    
test = MyStack()
test.push(1)
print(test.q)
test.push(2)
print(test.q)
test.pop()
print(test.q)
test.top()
print(test.q)
print(test.empty())
print(test.q)