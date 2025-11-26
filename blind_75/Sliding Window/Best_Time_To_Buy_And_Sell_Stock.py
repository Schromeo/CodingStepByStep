import math
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = math.inf
        max_profit = -math.inf
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

test = Solution()
print(test.maxProfit([7,1,5,3,6,4]))