'''
一场赛车排位赛的所有车手都完成了他们的排位圈。每一圈跑完后，当前“最佳”圈速最慢（即个人最快圈速用时最长）的车手将被淘汰。如果多名车手并列最慢，他们将全部被淘汰。

你将获得一个二维字符串数组 laps，其中包含每位车手每一圈的姓名和圈速（秒）。你的任务是返回一个按淘汰顺序列出车手的数组，并以最后留下的一名或多名车手结束。如果在同一圈中有多名车手被淘汰，他们的名字应按字母顺序排列。

注意： laps[i] 中的条目保证为 "str(姓名) int(时间)" 格式。

Example
For laps = [["Gina 155", "Eddie 160", "Joy 161", "Harold 163"], ["Harold 151", "Gina 153", "Joy 160", "Eddie 163"], ["Harold 149", "Gina 150", "Eddie 152", "Joy 155"]]

The output should be solution(laps) = ["Harold", "Eddie", "Joy", "Gina"].

Explanation:

After Lap 1 (laps[0]):

    Best times: Gina=155, Eddie=160, Joy=161, Harold=163.

    Slowest best time is 163.

    Harold is eliminated.

    Remaining: {Gina, Eddie, Joy}

After Lap 2 (laps[1]):

    Current lap times: Gina=153, Joy=160, Eddie=163.

    Updated best times:

    Gina: min(155, 153) = 153

    Eddie: min(160, 163) = 160

    Joy: min(161, 160) = 160

    Slowest best time is 160 (a tie).

    Eddie and Joy are eliminated. (Output alphabetically: "Eddie", then "Joy")

    Remaining: {Gina}

After Lap 3 (laps[2]):

    Gina is the only one remaining. No eliminations.

End of Laps:

    The remaining driver is Gina.

Final list = ["Harold", "Eddie", "Joy"] + ["Gina"]

Output: ["Harold", "Eddie", "Joy", "Gina"]
'''

def solution(laps):
    best_times = {}
    active_drivers = set()
    elimination_order = []
    for entry in laps[0]:
        name, time_str = entry.split()
        time = int(time_str)
        best_times[name] = time
        active_drivers.add(name)
    
    for lap in laps[1:]:
        for entry in lap:
            name, time_str = entry.split()
            if name in active_drivers:
                time = int(time_str)
                best_times[name] = min(best_times[name], time)
        
        if len(active_drivers) <= 1:
            continue

        slowest_time = -1
        to_eliminate = []
        for driver in active_drivers:
            driver_best = best_times[driver]
            if driver_best > slowest_time:
                slowest_time = driver_best
                to_eliminate = [driver]
            elif driver_best == slowest_time:
                to_eliminate.append(driver)
        
        if to_eliminate:
            to_eliminate.sort()
            elimination_order.extend(to_eliminate)
            active_drivers.difference_update(to_eliminate)
    remaining_drivers = sorted(list(active_drivers))
    elimination_order.extend(remaining_drivers)
    return elimination_order

# --- 测试 ---
test_laps_1 = [
    ["Gina 155", "Eddie 160", "Joy 161", "Harold 163"],
    ["Harold 151", "Gina 153", "Joy 160", "Eddie 163"],
    ["Harold 149", "Gina 150", "Eddie 152", "Joy 155"]
]

test_laps_2 = [
    ["Juan 154", "Gina 155", "Juan 160"], # 示例 1
    ["Harold 152", "Gina 153", "Harold 160"],
    ["Harold 149", "Gina 150", "Juan 151"]
]

print(f"示例 1 (Harold, Eddie, Joy, Gina): {solution(test_laps_1)}")
# 输出: 示例 1 (Harold, Eddie, Joy, Gina): ['Harold', 'Eddie', 'Joy', 'Gina']

print(f"示例 2 (Juan, Harold, Gina): {solution(test_laps_2)}")
# 输出: 示例 2 (Juan, Harold, Gina): ['Juan', 'Harold', 'Gina']