"""
LeetCode 20: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

A string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Args:
    s (str): The input string containing only the characters '(', ')', '{', '}', '[' and ']'.

Returns:
    bool: True if the input string is valid, False otherwise.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'{':'}', '[':']','(':')'}
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if stack and pairs[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return not stack