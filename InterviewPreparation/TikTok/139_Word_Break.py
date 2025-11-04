from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        if not s:
            return True
        if not wordSet:
            return False
        minL = min(len(w) for w in wordSet)
        maxL = max(len(w) for w in wordSet)
        n = len(s)

        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for L in range(minL, maxL + 1):
                j = i - L
                if j < 0:
                    break
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]

test = Solution()
print(test.wordBreak(s = "leetcode", wordDict = ["leet","code"]))
print(test.wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
print(test.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))