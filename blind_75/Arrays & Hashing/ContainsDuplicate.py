from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = {}
        for num in nums:
            record[num] = record.get(num, 0) + 1
            if record.get(num) > 1:
                return True
        return False