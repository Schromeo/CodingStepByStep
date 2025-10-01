from typing import List
from collections import defaultdict, Counter

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        board_letters = Counter(c for row in board for c in row)