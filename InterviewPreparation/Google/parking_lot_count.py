'''
题目:停车场门禁记录每辆车进出时间，给定时间t，返回从0到t每一时刻停车场有多少车
例子:三辆车进出时间[[1,3],[2,5],[4,5]],t=4 →返回[0,1212]
follow up:如果进出时间不是整数怎么改 code
'''

class Solution:
    def parking_lot_count(self, intervals, t):
        diff = [0] * (t+2)
        for start, end in intervals:
            diff[start] += 1
            if end <= t:
                diff[end] -= 1
        
        res = [0] * (t+1)
        cur = 0
        for i in range(t+1):
            cur += diff[i]
            res[i] = cur
        
        return res

t = Solution()
print(t.parking_lot_count([[1,3],[2,5],[4,5]], 4))