'''
你在一个繁忙的办公室工作...你的任务是分析数据，根据事件的数量来确定一年中最繁忙的月份。
给定一个非空字符串数组 dateList，其中每个字符串都代表一个 "YYYY-MM-DD" 格式的日期。请计算每个月份的事件数量（忽略年份）。
返回事件数量最多的月份，格式为一个两位数的数字字符串（例如，七月返回 "07"）。如果出现平局（多个月份事件数相同），则返回一年中最晚的那个月份。

注意：同一日期可能发生多个事件，这些应被视为单独的事件。

示例
    对于 dateList = ["2023-01-01", "2022-01-15", "2023-02-20", "2023-01-01", "2023-02-28"]，输出应为 solution(dateList) = "01"。

    解释： 一月 ("01") 有 3 个事件。二月 ("02") 有 2 个事件。"01" 是最繁忙的。

    对于 dateList = ["2023-01-05", "2023-01-10", "2023-02-10", "2023-05-25", "2023-05-30"]，输出应为 solution(dateList) = "05"。

    解释： 一月 ("01") 和 五月 ("05") 都有 2 个事件。由于是平局，我们选择更晚的月份，即五月 ("05")。

'''
from collections import Counter
def solution(dateList):
    months = [s[5:7] for s in dateList]
    print(months)
    counts = Counter(months)
    print(counts)
    winner_item = max(counts.items(), key=lambda item: (item[1], item[0]))
    return winner_item[0]

print(solution(["2023-01-01", "2022-01-15", "2023-02-20", "2023-01-01", "2023-02-28"]))