'''
46. Permutations
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]
'''
from typing import List
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start):
            if start == len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        dfs(0)
        return res

def test_permute():
    solution = Solution()
    assert solution.permute([]) == [[]]
    assert solution.permute([1]) == [[1]]
    assert solution.permute([0, 1]) == [[0, 1], [1, 0]]
    result = solution.permute([1, 2, 3])
    expected = [
        [1,2,3],[1,3,2],
        [2,1,3],[2,3,1],
        [3,1,2],[3,2,1]
    ]
    assert sorted(result) == sorted(expected)
    print("All test cases passed!")

if __name__ == "__main__":
    test_permute()

