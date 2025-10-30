'''
在 Unix 中，有两种常见的执行命令的方式：
输入命令名称，例如 "cp" 或 "ls"。
输入 "!<index>"：这个标记用来重复执行会话开始以来的第 index 个（1-based）命令。
给定一个用户在终端中输入的命令序列 commands。每个命令是 "cp", "ls", "mv" 或 "!<index>" 之一。
请计算 "cp", "ls", "mv" 这三个命令最终被执行的次数，并以如下形式返回一个包含三个整数的数组： 
    ["cp" 的执行次数, "ls" 的执行次数, "mv" 的执行次数]
'''
def solution(commands):
    cp, ls, mv = 0, 0, 0
    def ex(x):
        nonlocal cp, ls, mv
        if x == 'cp':
            cp += 1
        elif x == 'ls':
            ls += 1
        elif x == 'mv':
            mv += 1
        elif x.startswith('!'):
            ex(commands[int(x[1:]) -1])
    for x in commands:
        ex(x)
    
    return [cp, ls, mv]

print(solution(["ls", "cp", "mv", "mv", "!1", "!3", "!6"]))
