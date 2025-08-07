"""
LeetCode 209: Minimum Size Subarray Sum

Given an array of positive integers nums and a positive integer target, 
find the minimal length of a contiguous subarray [nums_l, nums_{l+1}, ..., nums_r] 
of which the sum is greater than or equal to target. If there is no such subarray, return 0.

Example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        if sum(nums) < target:
            return 0
        elif sum(nums) == target:
            return n
        if target in nums:
            return 1
        left = 0
        res = n
        curr_sum = 0
        for right in range(n):
            curr_sum += nums[right]
            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            
        return res

test = Solution()
print(test.minSubArrayLen(7, [2,3,1,2,4,3]))
