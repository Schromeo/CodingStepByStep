'''
给定一个整数矩阵 matrix，矩阵中的每个元素的值都为 0、1 或 2。
你的任务是找到一个符合以下模式的最长对角线段，并返回这个线段的长度。
模式： 1, 2, 0, 2, 0, ... （即，第一个元素必须是 1，然后 2 和 0 无限重复交替）。
对角线段定义：可以从矩阵中的任意元素开始和结束。可以朝任意一个对角线方向移动（共4个方向：右下、右上、左上、左下）。
'''
def find_longest_diagonal_pattern(matrix):
    """
    在矩阵中查找符合 1, 2, 0, 2, 0... 模式的最长对角线段。
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # 定义四个对角线方向：(行变化, 列变化)
    # (1, 1) -> 右下
    # (1, -1) -> 左下
    # (-1, 1) -> 右上
    # (-1, -1) -> 左上
    diagonal_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    
    max_length = 0  # 存储全局最长线段的长度

    # 1. 按方向遍历
    for direction in diagonal_directions:
        delta_row, delta_col = direction
        
        # 2. 收集该方向的所有 "边缘起点"
        starting_points = []
        
        # 方向：右下 (1, 1)
        if delta_row == 1 and delta_col == 1:
            # 起点必须在 顶边 或 左边
            starting_points += [[0, c] for c in range(cols)]  # 顶边
            starting_points += [[r, 0] for r in range(1, rows)] # 左边 (不含[0,0])
        
        # 方向：左下 (1, -1)
        elif delta_row == 1 and delta_col == -1:
            # 起点必须在 顶边 或 右边
            starting_points += [[0, c] for c in range(cols)]  # 顶边
            starting_points += [[r, cols - 1] for r in range(1, rows)] # 右边 (不含[0,n-1])

        # 方向：右上 (-1, 1)
        elif delta_row == -1 and delta_col == 1:
            # 起点必须在 底边 或 左边
            starting_points += [[rows - 1, c] for c in range(cols)] # 底边
            starting_points += [[r, 0] for r in range(rows - 1)] # 左边 (不含[m-1,0])

        # 方向：左上 (-1, -1)
        elif delta_row == -1 and delta_col == -1:
            # 起点必须在 底边 或 右边
            starting_points += [[rows - 1, c] for c in range(cols)] # 底边
            starting_points += [[r, cols - 1] for r in range(rows - 1)] # 右边 (不含[m-1,n-1])

        # 3. 遍历这个方向的所有 "边缘起点"
        for start_point in starting_points:
            current_row, current_col = start_point
            
            # 4. 从该起点出发，将整条对角线提取为一维列表
            diagonal_values = []
            while 0 <= current_row < rows and 0 <= current_col < cols:
                diagonal_values.append(matrix[current_row][current_col])
                current_row += delta_row
                current_col += delta_col
            
            # 5. 在这个一维列表中查找 1, 2, 0, 2, 0... 模式
            diagonal_length = len(diagonal_values)
            for start_index in range(diagonal_length):
                
                # 模式必须以 1 开始
                if diagonal_values[start_index] == 1:
                    current_length = 1  # 当前找到的模式长度
                    pattern_index = 1   # 模式计数器 (1->2, 2->0, 3->2, ...)
                    
                    # 从 1 的下一个位置开始检查
                    check_index = start_index + 1
                    
                    while check_index < diagonal_length:
                        # 核心逻辑：
                        # pattern_index 是奇数(1,3,5...)时, 期望值为 2
                        # pattern_index 是偶数(2,4,6...)时, 期望值为 0
                        expected_value = 2 if pattern_index % 2 == 1 else 0
                        
                        if diagonal_values[check_index] == expected_value:
                            # 匹配成功！
                            current_length += 1
                            pattern_index += 1
                            check_index += 1
                        else:
                            # 模式中断
                            break
                    
                    # 检查完一个以 1 开头的子序列后，更新全局最大值
                    if current_length > max_length:
                        max_length = current_length

    return max_length

matrix = [
  [9, 1, 9, 9, 1, 9],
  [2, 9, 2, 2, 9, 9],
  [9, 1, 0, 0, 9, 9],
  [9, 1, 9, 9, 2, 9],
  [9, 9, 9, 9, 9, 0]
]

print(find_longest_diagonal_pattern(matrix))  # 输出应为 5