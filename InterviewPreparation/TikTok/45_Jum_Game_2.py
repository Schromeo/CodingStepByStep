from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curEnd = 0
        curFarthest = 0
        for i in range(len(nums) - 1):
            curFarthest = max(curFarthest, i + nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = curFarthest
        return jumps