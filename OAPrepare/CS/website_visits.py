'''
给定一个非负整数数组 visits，它代表一个网站连续几天的访问人数。visits[0] 是第一天的访客数，visits[1] 是第二天的，以此类推。

你的任务是返回累计总访问量首次达到（大于或等于）给定 target 的那一天的索引 i。如果所有天数的总访问量都未达到 target，则返回 -1。
'''
def solution(visits, target):
    s = 0  # 's' 用来存储“累计总和”
    for i, v in enumerate(visits):
        s += v  # 将当天的访问量 v 加入总和 s
        if s >= target:
            return i  # 一旦总和达标, 立即返回当天的索引 i
    return -1  # 如果循环跑完了总和都没达标, 返回 -1
