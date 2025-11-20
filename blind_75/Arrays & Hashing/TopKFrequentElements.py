from typing import List
from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucket = defaultdict(list)
        result = []

        for num, freq in counter.items():
            bucket[freq].append(num)
        
        for freq in range(len(nums), 0, -1):
            if freq in bucket:
                for num in bucket[freq]:
                    result.append(num)
                    if len(result) == k:
                        return result
        
        return result