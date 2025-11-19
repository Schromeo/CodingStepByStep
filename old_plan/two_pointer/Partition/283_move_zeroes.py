"""
LeetCode 283: Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Do this in-place without making a copy of the array.

Args:
    nums (List[int]): The input array of integers.

Returns:
    None: Modifies nums in-place.

Example:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1