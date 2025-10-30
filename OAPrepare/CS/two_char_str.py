'''
给定一个包含字符串的数组 a。你的任务是构建一个相同长度的新数组，其中第 i 个元素是一个双字符字符串，由 a[i] 的第一个字符和 a[i + 1] 的最后一个字符拼接而成。
如果不存在 a[i + 1]（即当 i 是最后一个元素的索引时），则循环回数组的开头。换句话说，对于最后一个元素，应使用 a[a.length - 1] 的第一个字符和 a[0] 的最后一个字符进行拼接。
返回这个由双字符字符串组成的结果数组。

Example
For a = ["cat", "dog", "ferret", "scorpion"], the output should be solution(a) = ["cg", "dt", "fn", "st"].
    i=0: "cat" 的第一个 'c' + "dog" 的最后一个 'g' -> "cg"
    i=1: "dog" 的第一个 'd' + "ferret" 的最后一个 't' -> "dt"
    i=2: "ferret" 的第一个 'f' + "scorpion" 的最后一个 'n' -> "fn"
    i=3: "scorpion" 的第一个 's' + "cat" (循环回开头) 的最后一个 't' -> "st"
    For a = ["singularity"], the output should be solution(a) = ["sy"].
    i=0: "singularity" 的第一个 's' + "singularity" (循环回开头) 的最后一个 'y' -> "sy"
'''
def solution(a):
    n = len(a)
    result = []

    for i in range(n):
        curr_str = a[i]
        next_str = a[(i + 1) % n]
        new_str = curr_str[0] + next_str[-1]
        result.append(new_str)
    
    return result

print(solution(["cat", "dog", "ferret", "scorpion"]))