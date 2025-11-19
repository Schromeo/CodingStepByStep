'''
LeetCode 283: Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note:
- You must do this in-place without making a copy of the array.
- Minimize the total number of operations.

Example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

'''
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        # No need to return anything, nums is modified in-place

'''
Dry Run:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Explanation:
- Initialize slow pointer at 0.
- Iterate fast pointer from 0 to 4:
    - fast = 0: nums[0] is 0, do nothing.
    - fast = 1: nums[1] is 1, swap nums[0] and nums[1], increment slow to 1.
    - fast = 2: nums[2] is 0, do nothing.
    - fast = 3: nums[3] is 3, swap nums[1] and nums[3], increment slow to 2.
    - fast = 4: nums[4] is 12, swap nums[2] and nums[4], increment slow to 3.
'''