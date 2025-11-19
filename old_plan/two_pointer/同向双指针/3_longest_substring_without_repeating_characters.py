'''
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

'''
class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        res = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            char = s[right]
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            res = max(res, right - left + 1)
        return res

test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))