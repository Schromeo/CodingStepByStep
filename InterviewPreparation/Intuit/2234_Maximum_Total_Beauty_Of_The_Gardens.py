from bisect import bisect_right
from itertools import accumulate


class Solution:
    def maximumBeauty(self, flowers: list[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        # 保底分， 不需要消耗新花
        shift = sum( flower >= target for flower in flowers) * full
        # 将不完善的花园从小到大排序，填平的话从左往右，凑full的话从右往左
        sorted_unfill_garden = sorted([flower for flower in flowers if flower < target])
        n = len(sorted_unfill_garden)
        # 边界检查，如果没有不完善的花园，直接返回保底分
        if not sorted_unfill_garden:
            return shift
        
        # 检查如果手里的新花足够填满所有的花园；
        if newFlowers >= target * n - sum(sorted_unfill_garden):
            return max(full * n, partial * (target-1) + full * (n-1)) + shift
        
        # cost[i] 的含义是：把前 i+1 个花园 (B[0]...B[i]) 全部填平，
        # 填到和当前最高的那个 (B[i]) 一样高，总共需要多少花？
        cost = [0] + list(accumulate((i+1)*(y-x) for i, x, y in zip(range(n), sorted_unfill_garden, sorted_unfill_garden[1:])))

        j, ans = n-1, 0
        while newFlowers >= 0:
            idx = min(j, bisect_right(cost, newFlowers)-1)
            bar = sorted_unfill_garden[idx] + (newFlowers - cost[idx]) // (idx + 1)
            ans = max(ans, bar * partial + full * (n-j-1))
            new -= (target - sorted_unfill_garden[j])
            j -= 1
        return ans + shift
    