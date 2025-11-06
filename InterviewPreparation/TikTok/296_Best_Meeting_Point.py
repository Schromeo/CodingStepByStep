from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # 直方图：每一行/列里 1 的数量
        row_counts = [sum(row) for row in grid]                 # Hx
        col_counts = [sum(col) for col in zip(*grid)]           # Hy
        total_ones = sum(row_counts)

        # 行方向最小代价 + 列方向最小代价
        return self._min_cost_on_axis(row_counts, total_ones) + \
               self._min_cost_on_axis(col_counts, total_ones)

    def _min_cost_on_axis(self, hist: List[int], total_weight: int) -> int:
        """
        对一维权重直方图 hist 计算 f(t)=∑|t-p|*hist[p] 的最小值。
        线性时间，无需排序坐标。
        """

        # f(0)：把集合点放在 0 时的总代价 = ∑ p * hist[p]
        cost_at_pos = sum(index * cnt for index, cnt in enumerate(hist))

        # balance = #right(0) - #left(0)
        # 初始时 left=0，right=total_weight
        balance = total_weight

        # 逐点向右移动集合点 t：t=0,1,2,...
        # 每走过位置 i，就把 hist[i] 从“右”搬到“左”，balance 减少 2*hist[i]
        for i, cnt in enumerate(hist):
            balance -= 2 * cnt              # 更新到 t = i+1 的 right-left
            if balance < 0:
                # 已跨过加权中位数（或进入最小平台），此时 cost_at_pos 即最小值
                break
            # f(i+1) = f(i) - balance(i+1)
            cost_at_pos -= balance

        return cost_at_pos

        
        