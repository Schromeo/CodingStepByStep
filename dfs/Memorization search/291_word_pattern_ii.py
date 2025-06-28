'''
Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to non-empty strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

 
Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
Example 2:

Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
Example 3:

Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false
'''
class Solution:
    def wordPatternMatch(self, pattern:str, s: str) -> bool:
        def backtrack(p_i, s_i, mapping, used):
            if p_i == len(pattern) and s_i == len(s):
                return True
            if p_i == len(pattern) or s_i == len(s):
                return False
            char = pattern[p_i]
            for end in range(s_i + 1, len(s) + 1):
                word = s[s_i:end]
                if char in mapping:
                    if mapping[char] != word:
                        continue
                    if backtrack(p_i + 1, end, mapping, used):
                        return True
                else:
                    if word in used:
                        continue
                    mapping[char] = word
                    used.add(word)
                    if backtrack(p_i + 1, end, mapping, used):
                        return True
                    del mapping[char]
                    used.remove(word)
            return False
        return backtrack(0, 0, {}, set())

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    pattern = "abab"
    s = "redblueredblue"
    print(sol.wordPatternMatch(pattern, s))  # Output: True

    pattern = "aaaa"
    s = "asdasdasdasd"
    print(sol.wordPatternMatch(pattern, s))  # Output: True

    pattern = "aabb"
    s = "xyzabcxzyabc"
    print(sol.wordPatternMatch(pattern, s))  # Output: False