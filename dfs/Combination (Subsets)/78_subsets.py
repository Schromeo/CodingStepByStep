# 78. Subsets
# https://leetcode.com/problems/subsets/
# Given an integer array nums of unique elements, return all possible subsets (the power set).

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return res


# tests
def test_subsets():
    solution = Solution()
    
    # Test case 1: Empty array
    assert solution.subsets([]) == [[]]
    
    # Test case 2: Single element
    assert solution.subsets([1]) == [[], [1]]
    
    # Test case 3: Two elements
    assert solution.subsets([1,2]) == [[], [1], [1,2], [2]]
    
    # Test case 4: Three elements
    assert solution.subsets([1,2,3]) == [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_subsets()
