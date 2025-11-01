'''
给定一个整数 n，你的任务是创建一个大小为 n 的方形边框，并以一个字符串数组的形式表示。该边框应由 * 字符围成的空心方框组成。
'''
def solution(n):
    # 初始化一个 n x n 的二维数组，填充空格
    square = [[' ' for _ in range(n)] for _ in range(n)]
    
    # 填充边框的 * 字符
    for i in range(n):
        square[0][i] = '*'          # 顶部边框
        square[n-1][i] = '*'        # 底部边框
        square[i][0] = '*'          # 左侧边框
        square[i][n-1] = '*'        # 右侧边框
    
    # 将每一行转换为字符串
    result = [''.join(row) for row in square]
    
    return result

# 示例用法
n = 5
for line in solution(n):
    print(line)