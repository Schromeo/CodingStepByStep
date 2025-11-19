'''
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''
from typing import List
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        a_ord = ord('a')
        s1_count = [0] * 26
        win_count = [0] * 26

        for c in s1:
            s1_count[ord(c) - a_ord] += 1
        for c in s2[:n1]:
            win_count[ord(c) - a_ord] += 1

        if s1_count == win_count:
            return True

        for i in range(n1, n2):
            win_count[ord(s2[i]) - a_ord] += 1
            win_count[ord(s2[i - n1]) - a_ord] -= 1
            if s1_count == win_count:
                return True

        return False


def test_checkInclusion():
    solution = Solution()
    # Test case 1: Empty strings
    assert solution.checkInclusion("", "") == True
    
    # Test case 2: s1 is longer than s2
    assert solution.checkInclusion("abc", "ab") == False
    
    # Test case 3: s1 is a permutation of a substring in s2

    # Test case 1: s1 is a permutation of a substring in s2
    assert solution.checkInclusion("ab", "eidbaooo") == True
    
    # Test case 2: s1 is not a permutation of any substring in s2
    assert solution.checkInclusion("ab", "eidboaoo") == False
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_checkInclusion()