# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or digits is None:
            return []
        res = []
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def dfs(i, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            possible_letters = phone_map[digits[i]]
            for letter in possible_letters:
                path.append(letter)
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return res
# tests
def test_letterCombinations():
    solution = Solution()
    
    # Test case 1: Empty string
    assert solution.letterCombinations("") == []
    
    # Test case 2: Single digit
    assert solution.letterCombinations("2") == ["a", "b", "c"]
    
    # Test case 3: Two digits
    assert solution.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    
    # Test case 4: Three digits
    assert solution.letterCombinations("234") == ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
                                                "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
                                                "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_letterCombinations()
