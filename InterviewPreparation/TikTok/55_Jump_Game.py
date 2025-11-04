from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        for i in range(len(nums) -2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0

test = Solution()
print(test.canJump([2,3,1,1,4]))
print(test.canJump([3,2,1,0,4]))