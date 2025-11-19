'''
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.


Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''

from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append(i)
        return res
    
    # res: [0, 0, 0]
    # stack: []
    # 1: 0, 30  -> stack:[0]
    # 2: 1, 60  temp = 60 > 30 -> prev_index = 0, stack = []; res[0] = 1 - 0 = 1; stack = [1]
    # 3: 2, 90  temp = 90 > 60 -> prev_index = 1, stack = []; res[1] = 2 - 1 = 1; stack = [2]
    # stack = [2]; res = [1, 1, 0]