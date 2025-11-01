'''
想象在一条数轴上放置了几盏灯，每盏灯都会照亮线上的一个线段。
具体来说，这些灯由一个二维数组 lamps 表示，其中第 $i$ 盏灯覆盖的范围是 [lamps[i][0], lamps[i][1]]（包含端点）。
此外，你还获得了一个 points 数组，代表数轴上的一系列控制点。
你的任务是找出每个控制点被多少盏灯照亮。
具体而言，对于数组中的每个控制点 points[j]，你需要找到有多少盏灯 lamps[i] 满足 points[j] 位于其覆盖的线段 [lamps[i][0], lamps[i][1]] 内部。
最后，返回一个整数数组，其中第 $i$ 个整数对应第 $i$ 个控制点的答案。
输入/输出：[input] array.array.integer lamps一个二维整数数组，代表灯的照明线段。
约束: $1 \le \text{lamps.length} \le 10^5$, 坐标 $1 \le \text{lamps[i][0]} \le \text{lamps[i][1]} \le 10^5$。[input] array.integer points一个整数数组，代表控制点。约束: $1 \le \text{points.length} \le 10^5$, 坐标 $1 \le \text{points[i]} \le 10^5$。[output] array.integer一个整数数组，包含每个控制点被照亮的灯的数量。
'''
def solution(lamps, points):
    """
    使用“差分数组” (Difference Array) / 扫描线技巧来高效计算。
    
    这个算法的复杂度是 O(N + M + C)，其中：
    N = 灯的数量
    M = 点的数量
    C = 最大的坐标值
    """
    
    # 1. 初始化
    # 题目约束最大的坐标是 100,000
    max_coordinate = 100000
    
    # 创建差分数组。
    # 我们需要 +2 的大小，因为一个覆盖 [100000] 的灯
    # 需要在索引 100001 处标记 -1。
    # counts[i] 将存储坐标 i 处 "净增" 的灯光数量
    counts = [0] * (max_coordinate + 2)
    
    # --- 阶段 1: 构建差分数组 O(N) ---
    for lamp in lamps:
        l, r = lamp[0], lamp[1]
        
        # 在 "起始点" l, 计数器 +1
        counts[l] += 1
        
        # 在 "结束点" r 的 *下一个点* (r+1), 计数器 -1
        counts[r + 1] -= 1
        
    # --- 阶段 2: 通过前缀和 (Prefix Sum) 重建计数 O(C) ---
    # 遍历一遍，将差分数组转换回 "绝对计数值" 数组
    # 执行后，counts[i] 将真正代表点 i 被多少盏灯覆盖
    for i in range(1, max_coordinate + 2):
        counts[i] += counts[i - 1]

    # --- 阶段 3: 查询结果 O(M) ---
    
    # 使用列表推导式 (List Comprehension) 高效地 O(1) 查找所有点
    # 
    # 对于 'points' 数组中的每一个 'p'
    # 我们直接从预先计算好的 'counts' 数组中
    # 提取 'counts[p]' 作为答案。
    results = [counts[p] for p in points]
    
    return results

# --- 运行示例 (来自题目) ---
lamps = [[1, 7], [5, 11], [7, 9]]
points = [7, 1, 5, 10, 9, 15] 
# (注: 题目中的 15 超出了 10^5 的约束，但我们的代码仍能处理)
# (如果严格按 10^5 约束，我们假设 15 是一个无效点)
# 让我们使用一个在约束内的点
points_in_bounds = [7, 1, 5, 10, 9, 100000]

print(f"Lamps: {lamps}")
print(f"Points: {points_in_bounds}")
print(f"Result: {solution(lamps, points_in_bounds)}")
# 预期: [3, 1, 2, 1, 2, 0] (假设 100000 没被覆盖)