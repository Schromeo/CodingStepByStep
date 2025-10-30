'''
You are monitoring the building density in a district of houses. The district is represented as a number line... Initially, there are no houses in the district.

You are given queries, an array of integers representing the locations of new houses in the order in which they will be built. After each house is built, your task is to find the longest segment of contiguous houses in the district.

Return an array of integers representing the longest segment of contiguous houses after each respective house from queries is built.

NOTE: It's guaranteed that all of the house locations in queries are unique...

---------------------------------------------------------------------------------------------------------------------
你正在监控一个住宅区的建筑密度。该区域被表示为一条数轴。最初，该区域没有任何房屋。
给定一个整数数组 queries，它按顺序表示新房屋将要建造的位置。每建造一栋房屋后，你的任务是找到该区域中最长的连续房屋段的长度。
返回一个整数数组，数组中的每个元素代表在 queries 中对应房屋建成后，当前的最长连续房屋段的长度。
注意： 保证 queries 中所有房屋的位置都是唯一的。

示例
    对于 queries = [2, 1, 3]，输出应为 solution(queries) = [1, 2, 3]。

    queries[0] = 2 后，房屋在 {2}。最长连续段为 1。

    queries[1] = 1 后，房屋在 {1, 2}。最长连续段为 2。

    queries[2] = 3 后，房屋在 {1, 2, 3}。最长连续段为 3。

    最终答案为 [1, 2, 3]。

对于 queries = [1, 3, 0, 4]，输出应为 solution(queries) = [1, 1, 2, 2]。

    queries[0] = 1 后，房屋在 {1}。最长连续段为 1。

    queries[1] = 3 后，房屋在 {1}, {3}。最长连续段为 1。

    queries[2] = 0 后，房屋在 {0, 1}, {3}。最长连续段为 2 (即 {0, 1})。

    queries[3] = 4 后，房屋在 {0, 1}, {3, 4}。最长连续段仍为 2 (可以是 {0, 1} 或 {3, 4})。

    最终答案为 [1, 1, 2, 2]。
'''
from collections import defaultdict
def solution(queries):
    start_to_end = defaultdict(int)
    end_to_start = defaultdict(int)
    curr_max = 0
    result = []
    for q in queries:
        left, right = q, q
        if (q - 1) in end_to_start:
            left = end_to_start[q-1]
            del end_to_start[q-1]
        if (q + 1) in start_to_end:
            right = start_to_end[q+1]
            del start_to_end[q+1]
        start_to_end[left] = right
        end_to_start[right] = left
        curr_max = max(curr_max, right - left + 1)
        result.append(curr_max)
    return result

print(solution([1, 3, 0, 4]))
print(solution([2,1,3]))
# {[2,2]} {[2,2]}