'''
给定两个整数数组 a 和 b，以及一个包含待处理查询的数组 queries。queries中的每个查询 queries[i] 有以下两种形式：

[0, i, x]: 这种情况下，你需要将 a[i] 的值赋值为 x。

[1, x]: 这种情况下，你需要找到所有满足 a[i] + b[j] == x 的索引对 (i, j) 的总数。

请按顺序执行给定的查询，并返回一个数组，该数组仅包含所有类型为 [1, x] 的查询结果。
'''
from collections import Counter

def solution(a, b, queries):
    # 1. 初始化: O(N + M) 时间
    # ca_counts 是动态的 (会变), cb_counts 是静态的 (不变)
    ca_counts = Counter(a)
    cb_counts = Counter(b)
    
    results = []

    # 2. 遍历所有查询
    for query in queries:
        op_type = query[0]
        
        if op_type == 0:
            # --- 类型 0: 赋值 a[i] = x ---
            i, x = query[1], query[2]
            
            # a. 获取 a[i] 的旧值
            #    (必须从原数组 a 获取)
            old_val = a[i]
            
            # b. 在 a 数组中执行赋值
            a[i] = x
            new_val = x
            
            # c. 更新 ca_counts: 旧值-1
            ca_counts[old_val] -= 1
            # 如果旧值计数为0, 从 map 中移除 (和 Java 逻辑保持一致)
            if ca_counts[old_val] == 0:
                del ca_counts[old_val]
                
            # d. 更新 ca_counts: 新值+1
            ca_counts[new_val] += 1
            
        else: # op_type == 1
            # --- 类型 1: 查询 a[i] + b[j] == x ---
            target_sum = query[1]
            pair_count = 0
            
            # --- 关键优化 ---
            # 我们遍历 ca_counts (来自数组 a), 
            # 因为 a.length <= 5e4, b.length <= 1e5。
            # 遍历 ca_counts (N_unique) 总是比遍历 cb_counts (M_unique) 更快或一样快。
            
            for num_a, count_a in ca_counts.items():
                # 寻找补数: b[j] = target_sum - num_a
                needed_from_b = target_sum - num_a
                
                # 从 cb_counts 中获取这个补数出现的次数
                # (如果 needed_from_b 不存在, cb_counts[...] 会返回 0)
                count_b = cb_counts[needed_from_b]
                
                if count_b > 0:
                    pair_count += count_a * count_b
                        
            # 将此次查询的结果存入
            results.append(pair_count)
            
    return results

# --- 测试 ---
a1 = [3, 4]
b1 = [1, 2, 3]
q1 = [[1, 5], [0, 0, 1], [1, 5]]
print(f"示例 1: {solution(a1, b1, q1)}") 
# 输出: 示例 1: [2, 1]

a2 = [2, 3]
b2 = [1, 2, 2]
q2 = [[1, 4], [0, 0, 3], [1, 5]]
print(f"示例 2: {solution(a2, b2, q2)}") 
# 输出: 示例 2: [3, 4]