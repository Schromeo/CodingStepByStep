'''
一群勇敢的冒险家正在探索一件神秘的文物，它的圆形边缘刻有一系列独特的符号。

这些符号的顺序早已失传，但人们找到了一系列已知彼此相邻的符号对。

不幸的是，这些符号对随着时间的推移而变得混乱，这意味着每一对 (x, y) 都有可能被记录为 (x, y) 或 (y, x)。

你将获得一个 symbolPairs 数组，代表这些混乱的符号对。你的任务是重新发现文物圆形边缘上符号的原始序列。

请记住，序列的任何循环旋转或反转都可以被视为一个正确的解决方案，因为这个圆环没有固定的起点或终点。请返回任何一种有效的排列方式。

示例： 对于 symbolPairs = [[3, 5], [1, 4], [2, 4], [1, 5], [2, 3]]，输出可以是 solution(symbolPairs) = [3, 5, 1, 4, 2]。
'''
from collections import defaultdict

def solution(symbolPairs):
    """
    使用图遍历（邻接表）来重建循环序列。
    """
    
    # 1. 构建邻接表 (图)
    #    defaultdict(list) 会自动为空键创建一个空列表
    adj = defaultdict(list)
    for u, v in symbolPairs:
        adj[u].append(v)
        adj[v].append(u)

    # 2. 初始化遍历
    n = len(adj)             # 唯一节点的总数
    res = [0] * n            # 创建结果列表，长度为 n
    seen = set()             # 跟踪已访问的节点
    
    # 选取一个任意的起始节点
    start_node = symbolPairs[0][0]
    
    res[0] = start_node
    seen.add(start_node)
    
    # 跟踪我们 "来自" 哪个节点，以防止立即走回头路
    # (虽然 'seen' 集合已经能处理这个问题，但保留它逻辑更清晰)
    prev_node = -1 # 使用一个无效的节点 ID

    # 3. 遍历这个环 (n-1 步)
    for i in range(1, n):
        # 获取上一个添加的节点的邻居
        current_node = res[i-1]
        neighbors = adj[current_node]
        
        for next_node in neighbors:
            # 寻找一个我们 "不是刚从那里来" 并且 "尚未访问过" 的邻居
            if next_node != prev_node and next_node not in seen:
                res[i] = next_node
                seen.add(next_node)
                prev_node = current_node # 更新 "上一个" 节点
                break # 找到了这一步的路径，跳出内循环

    return res

# --- 运行示例 ---
symbolPairs = [[3, 5], [1, 4], [2, 4], [1, 5], [2, 3]]
print(f"输入: {symbolPairs}")
print(f"输出: {solution(symbolPairs)}") 

# 预期输出 (可能是 [3, 5, 1, 4, 2] 或 [3, 2, 4, 1, 5] 等)