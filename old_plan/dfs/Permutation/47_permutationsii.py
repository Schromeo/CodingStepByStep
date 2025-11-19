'''
47. Permutations II
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)
        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                used[i] = False
        dfs([])
        return res
def test_permuteUnique():
    solution = Solution()
    
    # Test case 1: Empty array
    assert solution.permuteUnique([]) == [[]]
    
    # Test case 2: Single element
    assert solution.permuteUnique([1]) == [[1]]
    
    # Test case 3: Array with duplicates
    result = solution.permuteUnique([1, 1, 2])
    expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert sorted(result) == sorted(expected)
    
    # Test case 4: Array without duplicates
    result = solution.permuteUnique([1, 2, 3])
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert sorted(result) == sorted(expected)
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_permuteUnique()
