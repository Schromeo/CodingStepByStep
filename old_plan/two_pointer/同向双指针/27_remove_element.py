'''
leetcode 27. Remove Element
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_]
Explanation: Your function should return length = 2, with the first two elements of nums being 2. It doesn't matter what you leave beyond the returned length.
'''
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow