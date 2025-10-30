'''
给定两个整数数组 a 和 b，以及一个包含待处理查询的数组 queries。queries中的每个查询 queries[i] 有以下两种形式：

[0, i, x]: 这种情况下，你需要将 x 加到 b[i] 的当前值上。

[1, x]: 这种情况下，你需要找到所有满足 a[i] + b[j] == x 的索引对 (i, j) 的总数。

请按顺序执行给定的查询，并返回一个数组，该数组仅包含所有类型为 [1, x] 的查询结果。
'''
from collections import Counter
def solution(a, b, queries):
    b_counts = Counter(b)
    results = []
    for query in queries:
        op_type = query[0]

        if op_type == 0:
            i, x = query[1], query[2]
            old_val = b[i]
            b[i] += x
            new_val = b[i]
            b_counts[old_val] -= 1
            b_counts[new_val] += 1
        
        else:
            target_sum = query[1]
            pair_count = 0

            for num_a in a:
                needed_from_b = target_sum - num_a
                pair_count += b_counts[needed_from_b]
            results.append(pair_count)
    
    return results

print(solution([1,2,3], [1,4], [[1, 5], [0, 0, 2], [1, 5]]))