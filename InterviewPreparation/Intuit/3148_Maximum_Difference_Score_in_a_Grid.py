from typing import List
import math
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        best = -math.inf
        for r in range(rows - 1, -1, -1):
            for c in range(cols -1, -1, -1):
                original = grid[r][c]
                if r != rows - 1:
                    diff = grid[r+1][c] - original
                    if diff > best:
                        best = diff
                    if grid[r+1][c] > grid[r][c]:
                        grid[r][c] = grid[r+1][c]
                
                if c != cols -1:
                    diff = grid[r][c+1] - original
                    if diff > best:
                        best = diff
                    if grid[r][c+1] > grid[r][c]:
                        grid[r][c] = grid[r][c+1]
        return best

test = Solution()
print(test.maxScore([[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]))