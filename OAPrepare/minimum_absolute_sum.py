'''
There is an array A consisting of N integers. Choose at most one element to multiply by -1 in order to obtain an array whose sum of elements is as close to 0 as possible. That is, find the sum with the minimum absolute value.

that, given an array A, returns the minimum absolute value of the sum of A that can be obtained.

Example 1:

Input: A = [1, 3, 2, 5]
Output: 1
Explanation:
      For A = [1, 3, 2, 5], after multiplying the last element by -1, A will be equal to [1, 3, 2, -5]. Its sum is 1. It is not possible to obtain any sum closer to 0. The function should return 1.
      

Example 2:

Input: A = [-4, 0, -3, 3]
Output: 2
Explanation:

      For A = [-4, 0, -3, 3], we can multiply -4 by -1 and therefore obtain A = [4, 0, -3, 3]. Its sum is 2. The function should return 2.
      

Example 3:

Input: A = [4, -3, 5, -7]
Output: 1
Explanation:
      Assume that A = [4, -3, 5, -7]. Its sum is -1. There is no possible move that could improve this result. The function should return 1.
      

Example 4:

Input: A = [-15, 18, 1, -1, 10, -22]
Output: 9
Explanation:
      It is optimal to change -1 to 1. The function should return 9.
      
Constraints:
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [-1,000..1,000].
'''
from typing import List
class Solution:
    def minimum_absolute_sum(self, nums: List[int]) -> int:
        S = sum(nums)
        ans = abs(S)
        for num in nums:
            ans = min(ans, abs(S - 2 * num))
        return ans

test = Solution()
print(test.minimum_absolute_sum([-15, 18, 1, -1, 10, -22])) # 7
print(test.minimum_absolute_sum([1,3,2,5]))
print(test.minimum_absolute_sum([-4,0,-3,3]))
print(test.minimum_absolute_sum([4, -3, 5, -7]))