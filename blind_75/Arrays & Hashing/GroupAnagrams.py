from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            dic[sorted_word].append(word)
        return list(dic.values())