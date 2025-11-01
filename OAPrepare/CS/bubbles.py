'''
给定一个包含不同颜色气泡的单元格面板 (bubbles)，你的任务是模拟一个戳气泡游戏。玩家每回合可以点击一个单元格：

被点击单元格中的气泡，以及其对角相邻单元格中颜色相同的气泡，会被“戳破”并移除，原地变成空单元格 (用 0 表示)。

在气泡被移除后，位于空单元格上方的剩余气泡会“掉落”下来，填满所有空单元格。

如果被点击的单元格是空的（不包含气泡），则什么也不发生。

对角相邻的定义是：与给定单元格只有一个角接触的单元格。（图片显示了 (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1) 这四个位置）。

输入/输出：

[input] array.array.integer bubbles

一个 2D 整数数组，代表气泡的颜色。

[input] array.array.integer operations

一个 2D 数组，代表玩家的点击操作，每个元素是 [row, col] 坐标。

[output] array.array.integer

返回处理完所有 operations 后的游戏面板最终状态。空单元格用 0 替换。
'''
def solution(bubbles, operations):
    # n = 行数, m = 列数 (与你代码中的 n, m 保持一致)
    rows_n = len(bubbles)
    cols_m = len(bubbles[0])

    # --- 阶段 1: 气泡消除 ---
    
    # 定义 5 个检查方向：(0,0)是单元格自身
    # (1,1), (1,-1), (-1,1), (-1,-1) 是四个对角线
    diagonal_and_self = [(0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for x, y in operations:
        clicked_color = bubbles[x][y]
        
        # 优化：如果点击的是空格子 (0)，则什么也不做，跳到下一次操作
        if clicked_color == 0:
            continue
            
        for dx, dy in diagonal_and_self:
            target_row = x + dx
            target_col = y + dy
            
            # 检查目标坐标是否在棋盘内
            is_in_bounds = (0 <= target_row < rows_n) and (0 <= target_col < cols_m)
            
            if is_in_bounds and bubbles[target_row][target_col] == clicked_color:
                # 戳破气泡 (设置为空)
                bubbles[target_row][target_col] = 0

    # --- 阶段 2: 重力下落 ---
    
    # 我们必须逐 *列* 处理
    for j in range(cols_m):
        
        # "last" (你代码中的) 是 "写入指针" (writer_pointer)
        # 它指向下一个 "非空" 气泡应该被移动到的 *最上方* (即索引最大) 的空槽。
        # 我们从最底部的行开始 (rows_n - 1)。
        writer_row = rows_n - 1

        # "i" (你代码中的) 是 "读取指针" (reader_pointer)
        # 我们从下往上 (n-1 到 0) 遍历该列中的所有单元格。
        for reader_row in range(rows_n - 1, -1, -1):
            
            # 你的代码: if last != i:
            #   bubbles[last][j] = bubbles[i][j]
            #   bubbles[i][j] = 0
            # 你的代码: last -= bubbles[last][j] != 0
            
            # --- 下面是你重力算法的逻辑分解 ---
            
            # 1. 检查 "读取" 的单元格是否包含一个气泡
            if bubbles[reader_row][j] != 0:
                # 2. 如果 "读取" 和 "写入" 指针不在同一位置
                if writer_row != reader_row:
                    # 将气泡从 [reader_row] "移动" 到 [writer_row]
                    bubbles[writer_row][j] = bubbles[reader_row][j]
                    bubbles[reader_row][j] = 0 # 清空旧位置
                
                # 3. 移动 "写入" 指针
                # (因为 writer_row 这一行现在被占用了, 
                #  下一个气泡必须放在它的 *上方*)
                writer_row -= 1
        
        # 循环结束后，writer_row 指向最上面的一个空槽
        # (或 -1，如果该列已满)。
        # 剩下的所有 "顶部" 单元格 (从 0 到 writer_row) 都应为空。
        # (在你的精炼算法中，这一步是隐式完成的，
        #  因为不匹配的 `0` 会被移动和覆盖)
        #
        # 我们可以添加一个显式的 "清空顶部" 循环，
        # 这会让逻辑更清晰，虽然你那个版本也正确。
        while writer_row >= 0:
            bubbles[writer_row][j] = 0
            writer_row -= 1
            
    return bubbles

print(solution([
  [1, 2, 9, 3],  # 第 0 行 (9 是一个 "干扰" 颜色)
  [9, 1, 9, 3],  # 第 1 行
  [1, 9, 1, 9],  # 第 2 行
  [9, 1, 9, 3],  # 第 3 行
  [1, 9, 1, 3]   # 第 4 行
], [
  [2, 2],  # 1. 点击 (2,2)，值为 1。
  [0, 3],  # 2. 点击 (0,3)，值为 3。
  [1, 1],  # 3. 点击 (1,1)，它现在是 0。
  [0, 0]   # 4. 点击 (0,0)，值为 1。
]))