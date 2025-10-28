'''
给你一个整数数组 nums，请你找出一个连续子数组，使得该子数组内的元素乘积最大，并返回这个乘积。
'''
from typing import List
class Solution:
    def max_product_subarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 2. 初始化
        #    我们把所有状态都初始化为第一个元素
        #    current_max: 包含 *当前* 元素的最大乘积
        #    current_min: 包含 *当前* 元素的最小乘积
        #    global_max:  我们目前为止见过的全局最大乘积
        current_max = nums[0]
        current_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            old_max = current_max
            current_max = max(num, num * old_max, num * current_min)
            current_min = min(num, num * old_max, num * current_min)

            global_max = max(global_max, current_max)
        
        return global_max

test = Solution()
print(test.max_product_subarray([2,3,0,-1,100]))