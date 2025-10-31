'''
给定一条无限长的整数数轴，你想要在上面建造一些砌块和障碍物。你需要实现支持两种操作的代码：

[1, x] - 在数轴上的坐标 x 处建造一个障碍物。题目保证当执行此操作时，坐标 x 处没有任何障碍物。

[2, x, size] - 检查是否可以在数轴上建造一个大小为 size、且其终点恰好在 x 之前的砌块。例如，如果 x = 6 且 size = 2，此操作会检查坐标 4 和 5。如果可以建造（即指定坐标上没有障碍物），则输出 "1"；否则输出 "0"。请注意，此操作不会真的建造砌块，它只进行检查。

给定一个包含上述两种操作的数组 operations，你的任务是返回一个二进制字符串，该字符串由所有 [2, x, size] 操作的输出按顺序组成。

Example
For operations = [[1, 2], [1, 5], [2, 5, 2], [2, 6, 3], [2, 2, 1], [2, 3, 2]], the output should be solution(operations) = "1010".

Explanation:

[1, 2]: 在 2 处建造一个障碍物。障碍物: {2}

[1, 5]: 在 5 处建造一个障碍物。障碍物: {2, 5}

[2, 5, 2]: 检查在 x=5 前、size=2 的块。即检查 [5-2 ... 5-1] -> [3, 4]。{3, 4} 中没有障碍物。输出: "1"

[2, 6, 3]: 检查在 x=6 前、size=3 的块。即检查 [6-3 ... 6-1] -> [3, 4, 5]。5 是一个障碍物。输出: "0"

[2, 2, 1]: 检查在 x=2 前、size=1 的块。即检查 [2-1 ... 2-1] -> [1]。{1} 中没有障碍物。输出: "1"

[2, 3, 2]: 检查在 x=3 前、size=2 的块。即检查 [3-2 ... 3-1] -> [1, 2]。2 是一个障碍物。输出: "0"

最终结果字符串是 "1010"。
'''
import bisect
def solution(ops):
    obstacles = []
    result = []

    for op in ops:
        if op[0] == 1:
            # 类型1： 建造障碍物
            x = op[1]
            bisect.insort(obstacles, x)
        elif op[0] == 2:
            x, size = op[1], op[2]
            left = x - size
            right = x - 1
            index_l = bisect.bisect_left(obstacles, left)
            index_r = bisect.bisect_right(obstacles, right)
            if index_l < index_r:
                result.append('0')
            else:
                result.append('1')
    return "".join(result)

print(solution([[1, 2], [1, 5], [2, 5, 2], [2, 6, 3], [2, 2, 1], [2, 3, 2]]))