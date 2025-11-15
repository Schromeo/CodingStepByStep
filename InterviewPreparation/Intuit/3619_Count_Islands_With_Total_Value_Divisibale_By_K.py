class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        island_count = 0

        def dfs(r: int, c: int) -> int:
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            total_value = grid[r][c]
            for dr, dc in directions:
                total_value += dfs(r + dr, c + dc)
            return total_value
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and (r, c) not in visited:
                    island_value = dfs(r, c)
                    if island_value % k == 0:
                        island_count += 1

        return island_count