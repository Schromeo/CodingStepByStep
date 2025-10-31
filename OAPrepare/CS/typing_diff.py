'''
在一个打字练习应用中，你需要验证用户输入的“一致性”。给定一个包含大小写英文字母的字符串 typedText，你需要计算该字符串中大写字母的数量与小写字母的数量之间的差值。以整数形式返回这个差值。

示例
typedText = "CodeSignal", 输出应为 -6。

解释： 有 2 个大写字母 ('C', 'S') 和 8 个小写字母。差值为 2 - 8 = -6。

typedText = "a", 输出应为 -1。

解释： 有 0 个大写字母和 1 个小写字母。差值为 0 - 1 = -1。

typedText = "AbCdEf", 输出应为 0。

解释： 有 3 个大写字母和 3 个小写字母。差值为 3 - 3 = 0。
'''
def solution(typedText):
    """
    计算字符串中 (大写字母数) - (小写字母数) 的差值。
    """
    
    # 1. 初始化两个计数器
    uppercase_count = 0
    lowercase_count = 0
    
    # 2. 遍历字符串中的每一个字符
    for char in typedText:
        # 3. 检查字符是大写还是小写
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
            
    # 4. 返回差值
    return uppercase_count - lowercase_count

# --- 测试 ---
print(f"CodeSignal: {solution('CodeSignal')}") # 输出: -6
print(f"a: {solution('a')}")                 # 输出: -1
print(f"AbCdEf: {solution('AbCdEf')}")           # 输出: 0