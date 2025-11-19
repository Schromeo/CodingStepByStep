# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(start, path, remain):
            if remain == 0:
                res.append(path[:])
            if remain < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, remain - candidates[i])
                path.pop()
        dfs(0, [], target)
        return res

# tests
def test_combinationSum():
    solution = Solution()
    
    # Test case 1: Empty array
    assert solution.combinationSum([], 1) == []
    
    # Test case 2: Single element that matches target
    assert solution.combinationSum([1], 1) == [[1]]
    
    # Test case 3: Multiple elements with valid combinations
    assert solution.combinationSum([2,3,6,7], 7) == [[2,2,3], [7]]
    
    # Test case 4: No valid combinations
    assert solution.combinationSum([2,4,6], 7) == []
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_combinationSum()
