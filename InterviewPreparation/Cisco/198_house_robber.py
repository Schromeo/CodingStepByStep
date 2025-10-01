from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        prev2, prev1 = nums[0], max(nums[0],nums[1])
        for num in nums[2:]:
            prev2, prev1 = prev1, max(prev2 + num, prev1)
        return prev1