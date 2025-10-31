'''
你需要实现一个函数 solution(word)，该函数接收一个字符串 word，并执行以下操作：两种操作：
    反转前 k 个字符：选择一个 k（$k$ 从 1 到字符串长度 $n$），将字符串的前 k 个字符反转。
    反转后 k 个字符：选择一个 k（$k$ 从 1 到字符串长度 $n$），将字符串的后 k 个字符反转。
目标：你需要尝试所有可能的 k 值（对于前反转和后反转）。
在所有生成的新字符串中，找到并返回按字母顺序排列最小的那一个。
'''
def solution(word):
    mn = word  # 初始化最小字符串为原始字符串
    n = len(word)
    for k in range(1, n + 1):
        # 反转前 k 个字符
        front_reversed = word[:k][::-1] + word[k:]
        mn = min(mn, front_reversed)
        
        # 反转后 k 个字符
        back_reversed = word[:-k] + word[-k:][::-1]
        mn = min(mn, back_reversed)
    return mn