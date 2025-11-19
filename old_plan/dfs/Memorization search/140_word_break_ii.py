'''
140. Word Break II

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 
Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

'''
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]
            
            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for sub_sentence in backtrack(end):
                        if sub_sentence:
                            res.append(word + " " + sub_sentence)
                        else:
                            res.append(word)
            memo[start] = res
            return res

        return backtrack(0)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    print(solution.wordBreak(s, wordDict))  # Output: ["cats and dog","cat sand dog"]