'''
LeetCode 139: Word Break

Problem Description:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into 
a space-separated sequence of one or more dictionary words.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Example:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = {}
        def dfs(i):
            if i < 0:
                return True
            if i in dp:
                return dp[i]
            for word in wordDict:
                if word == s[i-len(word)+1:i+1] and dfs(i - len(word)):
                    dp[i] = True
                    return dp[i]
            dp[i] = False
            return dp[i]
        return dfs(len(s) - 1)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(solution.wordBreak(s, wordDict))  # Output: True
