'''
给定一个初始为空的数组 numbers，你的任务是处理一个 queries 列表。有两种类型的查询：

"+x" - 将整数 x 追加到 numbers 中。numbers 可以包含多个相同的整数。

"-x" - 从 numbers 中移除所有 x 的实例。题目保证 x 此时存在于 numbers 中。

在处理完每条查询后，你需要计算 numbers 中满足以下条件的三元组 (x, y, z) 的数量：x - y == diff 且 y - z == diff。diff 是一个给定的正整数。注意 numbers 中的元素可以被重新排列以满足条件（即我们是在一个集合中寻找组合，而不是在列表的固定位置上）。

返回一个数组，包含每次查询后的三元组总数。
'''

def solution(queries, diff):
    from collections import defaultdict
    count = defaultdict(int)
    total = 0
    result = []
    for q in queries:
        op = q[0]
        x = int(q[1:])

        if op == "+":
            d = count[x-diff] * count[x+diff]
            d += count[x-2*diff] * count[x-diff]
            d += count[x+diff] * count[x+2*diff]
            total += d
            count[x] += 1
        
        elif op == '-':
            c = count[x]
            count[x] = 0
            d = c * count[x-diff] * count[x+diff]
            d += c * count[x - 2* diff] * count[x - diff]
            d += c * count[x + diff] * count[x + 2 * diff]

            total -= d
        
        result.append(total)
    return result
print(solution(queries = ["+1", "+5", "+4", "+6", "-4"], diff = 1))