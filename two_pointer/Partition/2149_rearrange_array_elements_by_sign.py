"""
2149. Rearrange Array Elements by Sign

Given a 0-indexed integer array nums of even length n, 
consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:
- Every consecutive pair of integers have opposite signs.
- For all integers with the same sign, the order in which they were present in nums is preserved.
- The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the above conditions.

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer. So the rearranged array is [1,-1].

Constraints:
- n == nums.length
- 2 <= n <= 2 * 10^5
- n is even
- 1 <= |nums[i]| <= 10^5
- nums consists of equal number of positive and negative integers.
"""
from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        pos, neg = 0, 1
        for num in nums:
            if num > 0:
                result[pos] = num
                pos += 2
            else:
                result[neg] = num
                neg += 2
        return result