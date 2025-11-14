class Solution:
    def countDistinct(self, s: str) -> int:
        n = len(s)
        trie = {}
        count = 0
        for i in range(n):
            node = trie
            for j in range(i, n):
                char = s[j]
                if char not in node:
                    node[char] = {}
                    count += 1
                node = node[char]
        return count

