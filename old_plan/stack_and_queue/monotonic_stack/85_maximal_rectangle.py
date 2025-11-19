"""
Maximal Rectangle (LeetCode 85) — problem description in LeetCode style.

Given a 2D binary matrix filled with '0's and '1's, find the largest rectangle containing only '1's and return its area.

Parameters
----------
matrix : List[List[str]] or List[List[int]]
    A 2D list representing the binary matrix. Each element is either '0'/'1' or 0/1.

Returns
-------
int
    The area (number of cells) of the largest rectangle that contains only '1's.

Examples
--------
Example 1:
Input:
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
Explanation: The maximal rectangle of area 6 is formed in the 3rd row spanning multiple columns.

Example 2:
Input:
matrix = [["0"]]
Output: 0

Example 3:
Input:
matrix = [["1"]]
Output: 1

Notes
-----
- Typical constraints: 1 <= rows, cols <= 200 (varies by platform).
- Input may be provided as characters ('0'/'1') or integers (0/1); handle both.

Approach (common optimal solution)
----------------------------------
- Treat each row as the base of a histogram: for every column maintain a running height equal to the number of consecutive '1's up to the current row.
- For each row, compute the largest rectangle area in the histogram defined by the heights. Use a monotonic increasing stack to compute largest rectangle in histogram in O(cols) time.
- Update the global maximum area across all rows.

Time complexity: O(rows * cols)
Space complexity: O(cols) for the heights array and stack

Implementation hints
--------------------
- Convert input entries to integers if necessary (e.g., int(cell) or cell == '1').
- Initialize heights = [0] * ncols. For each row, update heights[j] = heights[j] + 1 if matrix[row][j] == '1' else 0.
- Use the standard stack-based largest-rectangle-in-histogram routine that pushes indices of increasing heights and computes areas when popping.
"""

from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        nrows, ncols = len(matrix), len(matrix[0])
        heights = [0] * ncols
        max_area = 0

        for row in range(nrows):
            for col in range(ncols):
                heights[col] = heights[col] + 1 if matrix[row][col] == '1' or matrix[row][col] == 1 else 0

            # Calculate largest rectangle in histogram for current heights
            stack = []
            extended_heights = heights + [0]  # Add sentinel
            for i, h in enumerate(extended_heights):
                while stack and extended_heights[stack[-1]] > h:
                    height = extended_heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

        return max_area
if __name__ == "__main__":
    s = Solution()
    matrix1 = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    print(s.maximalRectangle(matrix1))  # Output: 6

    matrix2 = [["0"]]
    print(s.maximalRectangle(matrix2))  # Output: 0

    matrix3 = [["1"]]
    print(s.maximalRectangle(matrix3))  # Output: 1
