import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        
        mp = [0] * 128
        count = len(t)
        for char in t:
            mp[ord(char)] += 1
        
        start, end, start_index = 0, 0, 0
        min_len = math.inf

        while end < len(s):
            if mp[ord(s[end])] > 0:
                count -= 1
            mp[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if end - start < min_len:
                    min_len = end - start
                    start_index = start
                if mp[ord(s[start])] == 0:
                    count += 1
                mp[ord(s[start])] += 1
                start += 1
        
        return "" if min_len == math.inf else s[start_index:start_index+min_len]