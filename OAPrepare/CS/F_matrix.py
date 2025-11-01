'''
你将获得一个矩形字符矩阵 matrix，它代表一个二维场地，包含以下几种单元格：
    '-'：代表一个空单元格。
    '#'：代表一个障碍物。
    'F'：代表一个“连通图形”的单元格。
题目保证这个“连通图形” ('F') 存在，并且其所有单元格都是水平或垂直相连的。
重力会使这个图形朝场地底部下落，直到它的任意一个单元格碰到“地面”（矩阵的底部边缘）或碰到了一个障碍物 ('#')。
你的任务是返回图形停止下落后的场地状态。
复杂度说明： 你不需要提供最优解，一个时间复杂度不差于 $O(M^2 \cdot N^2)$ (M=行, N=列) 的解法均可通过。
'''
def solution(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # figure_cells: 一个集合，用于存储 (row, col) 元组
    figure_cells = set()
    
    # bfs_queue: 用于广度优先搜索 (BFS)
    bfs_queue = []

    # --- 阶段 1: 查找并擦除 "F" 图形 ---
    
    # 找到 "F" 图形的第一个单元格作为 BFS 的起点
    found_start = False
    for r in range(rows):
        if found_start:
            break
        for c in range(cols):
            if matrix[r][c] == 'F':
                bfs_queue = [(r, c)]
                found_start = True
                break
                
    # (如果找不到 'F'，bfs_queue 将为空，循环不会运行，代码安全)

    # 开始 BFS 遍历
    while bfs_queue:
        # 你的代码: x, y = q.pop()
        row, col = bfs_queue.pop()
        
        # 你的代码: if (x, y) in fc: continue
        if (row, col) in figure_cells:
            continue
            
        # 你的代码: fc.add((x, y))
        figure_cells.add((row, col))
        
        # 你的代码: matrix[x][y] = '-'
        # 立即从板上擦除，为阶段 3 做准备
        matrix[row][col] = '-'

        # 检查四个方向：上, 下, 左, 右
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row, next_col = row + dr, col + dc
            
            # 检查是否越界
            if 0 <= next_row < rows and 0 <= next_col < cols:
                # 检查是否是 'F' 的一部分
                if matrix[next_row][next_col] == 'F':
                    # 你的代码: q.append((nx, ny))
                    bfs_queue.append((next_row, next_col))

    # --- 阶段 2: 计算最小下落距离 ---
    
    # 你的代码: d = n (即 rows)
    # 我们需要跟踪 *所有* 单元格中 *最小* 的下落距离
    min_drop_distance = rows 

    for row, col in figure_cells:
        # 你的代码: s = 0
        # current_cell_drop: 当前这个单元格 *下方* 的空格数
        current_cell_drop = 0
        
        # 你的代码: while True: ... nx = x + s + 1
        # 从 (row + 1) 开始向下检查
        check_row = row + 1
        
        while True:
            # 检查是否 "触地" (越界) 或 "撞到障碍物"
            if check_row >= rows or matrix[check_row][col] == '#':
                break
            
            # 否则，我们又找到了一个空格
            current_cell_drop += 1
            check_row += 1
        
        # 你的代码: d = min(d, s)
        # 更新全局的 "最小" 下落距离
        min_drop_distance = min(min_drop_distance, current_cell_drop)

    # --- 阶段 3: 重绘图形 ---
    
    # 遍历我们存储的所有 "F" 单元格
    for row, col in figure_cells:
        # 将它们绘制到它们的新位置 (row + min_drop_distance)
        matrix[row + min_drop_distance][col] = 'F'
        
    return matrix

# --- 运行示例 (来自题目) ---
matrix = [
    ['F', 'F', 'F'],
    ['-', 'F', '-'],
    ['-', 'F', 'F'],
    ['#', '#', '-'],
    ['F', 'F', '-'],
    ['-', '-', '#'],
    ['-', '-', '-']
]

print("--- 原始矩阵 ---")
for r in matrix: print(r)

solution(matrix)

print("\n--- 下落后矩阵 ---")
for r in matrix: print(r)

# 预期输出 (来自题目):
# ['-', '-', '-']
# ['-', '-', '-']
# ['F', 'F', 'F']
# ['#', '#', 'F']
# ['-', 'F', 'F']
# ['F', 'F', '#']
# ['-', '-', '-']