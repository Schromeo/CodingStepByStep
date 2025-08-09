'''

LeetCode 5: Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.
A palindrome is a string that reads the same backward as forward.
Example 1:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
Example 2:
    Input: s = "cbbd"
    Output: "bb"
Constraints:
    - 1 <= s.length <= 1000
    - s consist of only digits and English letters.

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        
        def expand(start, end):
            while 0 <= start < n and 0 <= end < n and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start+1: end]
        
        result = ""
        for i in range(n):
            odd = expand(i, i)
            even = expand(i, i+1)
            result = max(odd, even, result, key=len)
        
        return result