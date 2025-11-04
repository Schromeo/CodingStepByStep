from collections import deque
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQ = deque()
        minQ = deque()
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            while maxQ and maxQ[-1] < x:
                maxQ.pop()
            maxQ.append(x)

            while minQ and minQ[-1] > x:
                minQ.pop()
            minQ.append(x)
        
            while maxQ[0] - minQ[0] > limit:
                if nums[left] == maxQ[0]:
                    maxQ.popleft()
                if nums[left] == minQ[0]:
                    minQ.popleft()
                left += 1
        
            ans = max(ans, right-left + 1)
        return ans
test = Solution()
print(test.longestSubarray([8,2,4,7], 4))