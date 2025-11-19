# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# input: nums = [1,2,2]
# output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return res
    
# tests
def test_subsetsWithDup():
    solution = Solution()
    
    # Test case 1: Empty array
    assert solution.subsetsWithDup([]) == [[]]
    
    # Test case 2: Single element
    assert solution.subsetsWithDup([1]) == [[], [1]]
    
    # Test case 3: Array with duplicates
    assert solution.subsetsWithDup([1,2,2]) == [[], [1], [1,2], [1,2,2], [2], [2,2]]
    
    # Test case 4: Array with multiple duplicates
    assert solution.subsetsWithDup([1,1,2,2]) == [[], [1], [1,1], [1,1,2], [1,1,2,2], [1,2], [1,2,2], [2], [2,2]]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_subsetsWithDup()
