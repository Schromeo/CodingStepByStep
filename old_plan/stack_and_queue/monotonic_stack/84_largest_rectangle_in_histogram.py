from typing import List

"""
LeetCode 84 — Largest Rectangle in Histogram (LC style)

Given an array of integers heights representing the histogram's bar heights where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Examples:
- Input: heights = [2,1,5,6,2,3]
    Output: 10
    Explanation: The largest rectangle has area 10 (heights[2]=5 and heights[3]=6 span width 2 -> 5*2 = 10).

- Input: heights = [2,4]
    Output: 4

Constraints:
- 1 <= len(heights) <= 10^5
- 0 <= heights[i] <= 10^4

Follow-up / Hint:
- Optimal O(n) time using a monotonic (increasing) stack. Use sentinel zeros at both ends to simplify boundary handling.
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Add sentinels to avoid empty-stack checks
        heights = heights + [0]
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area

if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))  # 10
    print(s.largestRectangleArea([2,4]))          # 4