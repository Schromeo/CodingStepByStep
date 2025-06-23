'''
Given an m x n board of characters board and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

''' 
from typing import List
from collections import defaultdict, Counter

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words:List[str]) -> List[str]:
        # filter the letter that doesn't exist on board
        board_letters = Counter(c for row in board for c in row)
        valid_words = []
        for word in words:
            if all(board_letters.get(c, 0) >= word.count(c) for c in set(word)):
                valid_words.append(word)
        
        # build Trie tree
        root = TrieNode()
        for word in valid_words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        
        rows, cols = len(board), len(board[0])
        result = []

        # dfs
        def dfs(r, c, parent):
            ch = board[r][c]
            curr = parent.children.get(ch)
            if not curr:
                return
            if curr.word:
                result.append(curr.word)
                curr.word = None
            board[r][c] = '#'
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, curr)

            board[r][c] = ch

            if not curr.children:
                parent.children.pop(ch)
        
        # main traverse
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        
        return result

test = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(test.findWords(board=board, words=words))