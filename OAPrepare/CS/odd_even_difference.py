'''
给定一个整数数组 numbers。你的任务是返回两个总和的差值：偶数索引（0-based）上所有值在 [-100, 100] 范围内的元素之和。
奇数索引上所有值在 [-100, 100] 范围内的元素之和。
注意： 题目不要求最优解，时间复杂度不差于 $O(\text{numbers.length}^2)$ 的解法均可通过。
'''

def solution(nums):
    sum_1 = sum(nums[i] for i in range(0,len(nums),2) if -100 <= nums[i] <= 100)
    sum_2 = sum(nums[i] for i in range(1,len(nums),2) if -100 <= nums[i] <= 100)
    return sum_1 - sum_2

print(solution([101, 3, 4, 359, 2, 5]))