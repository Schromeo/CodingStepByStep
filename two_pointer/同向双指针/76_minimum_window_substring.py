'''
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

Note that if there is such a substring, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Example 3:
Input: s = "a", t = "aa"
Output: ""

Constraints:
- m == len(s)
- n == len(t)
- 1 <= m, n <= 10^5
- s and t consist of English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?

'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        mp = [0] * 128
        count = len(t)
        start = 0
        end = 0
        min_len = float('inf')
        start_index = 0

        for char in t:
            mp[ord(char)] += 1

        while end < len(s):
            if mp[ord(s[end])] > 0:
                count -= 1
            mp[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if end - start < min_len:
                    start_index = start
                    min_len = end - start
                
                if mp[ord(s[start])] == 0:
                    count += 1
                mp[ord(s[start])] += 1
                start += 1
        return "" if min_len == float('inf') else s[start_index:start_index + min_len]

test = Solution()
print(test.minWindow(s = "ADOBECODEBANC", t = "ABC"))