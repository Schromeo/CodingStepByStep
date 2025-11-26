from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                curr_sum = nums[left] + nums[i] + nums[right]
                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    res.append([nums[left], nums[i], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right -1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

test = Solution()
print(test.threeSum(nums = [-1,0,1,2,-1,-4]))