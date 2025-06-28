'''
Given an array of unique strings words, return all the word squares you can build from words. The same word from words can be used multiple times. You can return the answer in any order.

A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
 

Example 1:

Input: words = ["area","lead","wall","lady","ball"]
Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
'''
from typing import List, Dict, Set
from collections import defaultdict
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        prefix_map = defaultdict(list)
        for word in words:
            for i in range(n+1):
                prefix_map[word[:i]].append(word)
        result = []
    
        def backtrack(path):
            if len(path) == n:
                result.append(path[:])
                return
            prefix = ''.join([word[len(path)] for word in path])
            for candidate in prefix_map.get(prefix, []):
                backtrack(path + [candidate])
        for word in words:
            backtrack([word])
        return result
# Example usage:
if __name__ == "__main__":
    sol = Solution()
    words = ["area","lead","wall","lady","ball"]
    print(sol.wordSquares(words))  # Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
    