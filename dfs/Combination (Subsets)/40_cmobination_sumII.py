# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(start, path, remain):
            if remain == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                dfs(i+1, path, remain - candidates[i])
                path.pop()
        dfs(0, [], target)
        return res

# tests
def test_combinationSum2():
    solution = Solution()
    
    # Test case 1: Empty array
    assert solution.combinationSum2([], 1) == []
    
    # Test case 2: Single element that matches target
    assert solution.combinationSum2([1], 1) == [[1]]
    
    # Test case 3: Multiple elements with duplicates
    assert solution.combinationSum2([10,1,2,7,6,1,5], 8) == [[1,1,6], [1,2,5], [1,7], [2,6]]
    
    # Test case 4: No valid combinations
    assert solution.combinationSum2([2,4,6], 7) == []
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_combinationSum2()
