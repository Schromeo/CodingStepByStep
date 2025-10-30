'''
你将获得一个由 0 和 1 组成的整数数组 memory... memory[i] = 0 表示第 i 个内存单元空闲，memory[i] = 1 表示被占用。
内存按 8 个单元的段对齐，因此所有分配的内存块都必须从可被 8 整除的索引开始（例如 0, 8, 16...）。

你的任务是执行两种类型的查询：

    alloc x (分配 x): 找到最靠左的、对齐的、且包含 x 个连续空闲内存单元的内存块，并将这些单元标记为占用（即，找到一个从可被 8 整除的 start 位置开始的、长度为 x 的连续 0 子数组，并将其替换为 1）。
    如果找不到符合条件的内存块，返回 -1。
    否则，返回 start 索引...并为该块分配一个 ID。ID 基于一个原子计数器（计数器从 1 开始，每次成功的 alloc 操作后递增）。

注意：x 可能大于 8，所以内存块可能跨越多个段。
    erase ID (擦除 ID): 如果存在 ID 对应的已分配内存块，释放其所有内存单元（将块中的所有位置 0）。
    返回被删除内存块的长度。
    如果不存在该 ID（或该 ID 对应的块已被删除），返回 -1。
    查询按以下格式给出：
        queries[i][0] = 0: alloc 类型查询, x = queries[i][1]。
        queries[i][0] = 1: erase 类型查询, ID = queries[i][1]。
        返回一个包含所有查询结果的数组。
'''
def solution(matrix):
    # 1. 获取维度
    # rows = 行数 (n), cols = 列数 (m)
    rows, cols = len(matrix), len(matrix[0])

    # 2. 初始化 DP 矩阵
    # 矩阵应该是 rows x cols (即 n x m)
    left_up = [[0] * cols for _ in range(rows)]
    right_up = [[0] * cols for _ in range(rows)]
    left_down = [[0] * cols for _ in range(rows)]
    right_down = [[0] * cols for _ in range(rows)]

    # --- 阶段 1: 从上到下, 计算 left_up 和 right_up ---
    for i in range(rows):  # i 是行索引
        for j in range(cols):  # j 是列索引
            if matrix[i][j] == 1:
                # 【已修复】给 [i][j] 单元格赋值, 而不是覆盖整个变量
                # 【已修复】right_up 应该看 [i-1][j+1]
                left_up[i][j] = (left_up[i-1][j-1] + 1) if i > 0 and j > 0 else 1
                right_up[i][j] = (right_up[i-1][j+1] + 1) if i > 0 and j < cols - 1 else 1
    
    # --- 阶段 2: 从下到上, 计算 left_down 和 right_down ---
    for i in range(rows - 1, -1, -1): # i 是行索引
        for j in range(cols - 1, -1, -1): # j 是列索引
            if matrix[i][j] == 1:
                # 【已修复】给 [i][j] 单元格赋值
                # 【已修复】修正 DP 方向
                left_down[i][j] = (left_down[i+1][j-1] + 1) if i < rows - 1 and j > 0 else 1
                right_down[i][j] = (right_down[i+1][j+1] + 1) if i < rows - 1 and j < cols - 1 else 1

    # --- 阶段 3: 寻找最大值和最小索引 ---
    max_size = 0
    res = [0, 0]
    for i in range(rows): # i 是行
        for j in range(cols): # j 是列
            # 'x' 的大小是四条射线中最小的那条
            size = min(left_up[i][j], right_up[i][j], left_down[i][j], right_down[i][j])
            
            if size > max_size:
                max_size = size
                res = [i, j]
            elif size == max_size:
                # 平局规则: 最小的 i (row), 然后是 最小的 j (col)
                if i < res[0] or (i == res[0] and j < res[1]):
                    res = [i, j]
    
    return res

# --- 测试 ---
test_matrix = [
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1]
]

# 图片中的另一个例子:
test_matrix_2 = [
    [1, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1]
]
# 预期: [2, 4]

print(solution(test_matrix)) # 输出: [1, 1]
print(solution(test_matrix_2)) # 输出: [2, 4]