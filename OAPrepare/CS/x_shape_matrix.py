'''
给定一个只包含 0 和 1 的整数矩阵 matrix。
我们定义一个 "x-shape" (x形状) 是一个以 matrix[row][col] 为中心、并有 4 条等长对角射线的图形。
如果一个 "x-shape" 上的所有元素都为 1，则称其为完美的。
请返回矩阵中最大的完美 "x-shape" 的中心坐标 [row, col]。
        如果存在多个答案（即多个相同最大尺寸的 'x'），则返回行索引最小的答案；
        如果行索引仍然相同，则返回列索引最小的答案。
    注意：索引从 0 开始。保证矩阵中至少有一个 1。复杂度不差于 $O(N^2 \cdot M^2)$ 的解法均可通过
'''
def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    left_up = [[0] * rows for _ in range(cols)]
    right_up = [[0] * rows for _ in range(cols)]
    left_down = [[0] * rows for _ in range(cols)]
    right_down = [[0] * rows for _ in range(cols)]

    for i in range(cols):
        for j in range(rows):
            if matrix[i][j] == 1:
                left_up[i][j] = (left_up[i-1][j-1] + 1) if i > 0 and j > 0 else 1
                right_up[i][j] = (right_up[i-1][j-1] + 1) if i > 0 and j > 0 else 1
    
    for i in range(cols - 1, -1, -1):
        for j in range(rows - 1, -1, -1):
            if matrix[i][j] == 1:
                left_down[i][j] = (left_down[i+1][j-1] + 1) if i < cols -1 and j > 0 else 1
                right_down[i][j] = (right_down[i+1][j+1] + 1) if i < cols -1 and j < rows - 1 else 1
    
    max_size = 0
    res = [0, 0]
    for i in range(cols):
        for j in range(rows):
            size = min(left_up[i][j], right_up[i][j], left_down[i][j], right_down[i][j])
            if size > max_size:
                max_size = size
                res = [i,j]
            elif size == max_size:
                if i < res[0] or (i == res[0] and j < res[1]):
                    res = [i,j]
    
    return res
print(solution([[1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 1]]))