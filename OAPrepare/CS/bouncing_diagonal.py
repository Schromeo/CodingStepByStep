'''
你将获得一个大小为 $n \times n$ 的方阵 matrix。
我们定义一个**“反弹对角线”：它从最左侧列的某个单元格开始，向右上对角移动，直到到达最右侧列。
如果它在移动中到达了矩阵的顶部，它会垂直向下反弹（dr = 1）；
如果它到达了底部，它会垂直向上**反弹（dr = -1）。
对于最左侧列的每个单元格，我们定义它的**“权重”**为从该单元格出发的“反弹对角线”上所有元素的总和。
你的任务是：根据权重对最左侧列的元素值进行升序排序。如果权重出现平局，则根据它们的原始值（也是升序）进行排序。
返回排序后最左侧列的值的数组。
'''
def solution(matrix):
    n = len(matrix)
    res = []  # 存储 (weight, value) 对
    for r in range(n):
        # s = 单元格的原始值 (value)
        s = matrix[r][0]
        # sum_w = 该对角线的权重 (weight)
        sum_w = s
          
        # --- 模拟对角线 ---
        row, col = r, 0  # 当前位置
        # dr = direction_row (行方向), dc = direction_col (列方向)
        dr, dc = -1, 1   # 初始方向: 右上
         
        # 循环, 直到到达最后一列
        while col + dc < n: 
            # nr = next_row, nc = next_col
            nr, nc = row + dr, col + dc
             
            # --- 反弹逻辑 ---
            if nr < 0:      # 撞到上边界
                dr = 1      # 改变行方向为 "下"
                nr = 1      # 新的行位置是 1 (从 0 反弹到 1)
            elif nr >= n:   # 撞到下边界5
                dr = -1     # 改变行方向为 "上"
                nr = n - 2  # 新的行位置 (从 n-1 反弹到 n-2)
             
            # 更新当前位置
            row, col = nr, nc
            # 累加权重
            sum_w += matrix[row][col]
             
        # 存储 (权重, 原始值) 元组
        res.append((sum_w, s))
         
        #   --- 排序和返回 ---
        # 关键: 使用 lambda x: (x[0], x[1]) 进行排序
        # 1. 首先按 x[0] (权重) 升序排序
        # 2. 如果 x[0] 相同, 再按 x[1] (原始值) 升序排序
        res.sort(key=lambda x: (x[0], x[1]))
     
        # 提取排序后的 "原始值"
        return [x[1] for x in res]