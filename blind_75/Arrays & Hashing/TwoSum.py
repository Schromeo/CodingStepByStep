from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in record:
                return [record[complement], idx]
            record[num] = idx