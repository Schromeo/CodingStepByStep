from collections import defaultdict, deque
"""
LeetCode 126: Word Ladder II
This module provides a solution to the Word Ladder II problem, where the goal is to find all shortest transformation sequences from a starting word to an ending word, given a list of allowed words. Each transformation changes only one letter at a time, and each intermediate word must exist in the word list.
Classes:
    Solution: Contains the method to find all shortest transformation sequences.
Methods:
    findLadders(beginWord, endWord, wordList):
        Finds all shortest transformation sequences from beginWord to endWord.
        Uses BFS to build a tree of shortest paths and returns all valid sequences.
Args:
    beginWord (str): The word to start the transformation from.
    endWord (str): The word to end the transformation at.
    wordList (List[str]): The list of allowed words for transformation.
Returns:
    List[List[str]]: A list of all shortest transformation sequences from beginWord to endWord.
"""

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # BFS to build the leel graph and prevent records
        levels = {beginWord: 0}
        predecessors = defaultdict(set)
        queue = deque([beginWord])
        found = False
        level = 0
        
        while queue and not found:
            level += 1
            next_level_words = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            if new_word not in levels:
                                levels[new_word] = level
                                queue.append(new_word)
                                next_level_words.add(new_word)
                            if levels[new_word] == level:
                                predecessors[new_word].add(word)
                            if new_word == endWord:
                                found = True
            wordSet -= next_level_words  # 防止重复访问

        # 如果没找到，返回空
        if endWord not in predecessors:
            return []

        # DFS 回溯路径
        res = []
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for prev in predecessors[word]:
                dfs(prev, path + [prev])

        dfs(endWord, [endWord])
        return res

# Example usage:
test = Solution()
print(test.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))