'''
遍历查找岛屿

逐个检查 grid[i][j]，若为 1，说明找到新的岛屿，执行 DFS 进行标记和形状记录。
DFS 标记岛屿形状

递归遍历四个方向 (R, L, D, U)，记录路径，确保相同形状的岛屿生成相同的路径表示。
用 B 记录回溯，防止形状不唯一。
存储唯一岛屿形状

使用 set 存储岛屿的路径表示，确保相同形状的岛屿只计算一次。
返回不同岛屿数量

set 的大小即为不同岛屿的数量。
该方法利用 DFS + 哈希集合，时间复杂度 O(mn)，

'''
from typing import List
class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        shapes = set()
        directions = [(0,1,'R'), (0,-1,'L'), (1, 0, 'U'), (-1, 0, 'D')]
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, move, path):
            visited[r][c] = True
            path.append(move)
            for dr, dc, mv in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 1:
                    dfs(nr, nc, mv, path)
            path.append('B')
        
        for r in range(rows):
            for c in range(cols):
                if not visited[r][c] and grid[r][c] == 1:
                    path = []
                    move = 'S'
                    dfs(r, c, move, path)
                    shapes.add(tuple(path))
        return len(shapes)

test = Solution()
print(test.numDistinctIslands2([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
print(test.numDistinctIslands2([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))