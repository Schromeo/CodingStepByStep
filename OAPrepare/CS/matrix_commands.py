'''
在一个高度自动化的仓库中，一个机器人...被表示为一个 2D 整数列表 matrix... 机器人遵循一系列字符串 commands。每个命令指导机器人对矩阵执行特定操作：

"swapRows r1 r2": 将 r1 行的元素与 r2 行的元素交换。

"swapColumns c1 c2": 将 c1 列的元素与 c2 列的元素交换。

"reverseRow r": 将 r 行的元素反转。

"reverseColumn c": 将 c 列的元素反转。

"rotate90Clockwise": 将整个矩阵顺时针旋转 90 度。

你的任务是在 matrix 上实现这一系列命令，并返回矩阵的最终状态。
'''
def solution(matrix, commands):
    for cmd in commands:
        p = cmd.split() # p = parts (e.g., ["swapRows", "0", "2"])
        if p[0] == "swapRows":
            r1, r2 = int(p[1]), int(p[2])
            # Python 的元组交换, 直接交换两个 "行列表"
            matrix[r1], matrix[r2] = matrix[r2], matrix[r1]
        
        elif p[0] == "swapColumns":
            c1, c2 = int(p[1]), int(p[2])
            # 遍历每一行
            for row in matrix:
                # 交换这一行中 c1 和 c2 位置的元素
                row[c1], row[c2] = row[c2], row[c1]
        
        elif p[0] == "reverseRow":
            r = int(p[1])
            # 直接调用列表的 .reverse() 方法
            matrix[r].reverse()
            
        elif p[0] == "reverseColumn":
            c = int(p[1])
            n = len(matrix) # n = 总行数
            # 经典的 "双指针" 原地反转
            for i in range(n // 2):
                # i (从上往下) 和 n-i-1 (从下往上)
                matrix[i][c], matrix[n-i-1][c] = matrix[n-i-1][c], matrix[i][c]
                
        elif p[0] == "rotate90Clockwise":
            # 这是最巧妙的一行
            matrix[:] = [list(r) for r in zip(*matrix[::-1])]
            
    return matrix