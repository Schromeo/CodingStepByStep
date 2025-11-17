'''
Olivia 有 n 个整数，她想把它们都变成同一个整数 T。
变换代价是 (x - y)^2。
求最小的总代价。
'''

import math
def min_cost_to_equalize(nums):
    if not nums:
        return 0
    n = len(nums)
    total_sum = sum(nums)
    mean = total_sum / n
    target1 = math.floor(mean)
    target2 = math.ceil(mean)

    cost1 = sum((x-target1) ** 2 for x in nums)
    cost2 = sum((x-target2) ** 2 for x in nums)

    return min(cost1, cost2)

print(min_cost_to_equalize([1,2,3]))
print(min_cost_to_equalize([1,5]))