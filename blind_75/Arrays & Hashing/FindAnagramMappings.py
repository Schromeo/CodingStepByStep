from typing import List
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        for i in range(len(nums2)):
            if nums2[i] not in mapping:
                mapping[nums2[i]] = i
        return [mapping[nums1[i]] for i in range(len(nums1))]
            