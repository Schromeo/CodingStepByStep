# LeetCode 22: Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# The solution should use backtracking to explore all valid combinations.

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(current, left, right):
            if len(current) == 2 * n:
                result.append(current)
                return
            if left < n:
                backtrack(current + '(', left + 1, right)
            if right < left:
                backtrack(current + ')', left, right + 1)
        
        backtrack('', 0, 0)
        return result

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
