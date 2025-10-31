'''
给定一个字符串 message 和一个整数 n，你需要将字符串中的每第 n 个辅音字母替换为字母表中的下一个辅音字母，同时保持大小写一致（例如，'b' 变为 'c', 'B' 变为 'C'）。'z' 必须被替换为 'b'（'Z' 替换为 'B'）。

注意：

辅音字母表: b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z

元音字母: a, e, i, o, u
'''
def solution(message, n):
    """
    替换字符串中的每第 n 个辅音字母。
    """
    
    # --- 1. 定义辅助常量 ---
    LOWER_CONSONANTS = "bcdfghjklmnpqrstvwxyz"
    UPPER_CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZ"
    VOWELS = "aeiouAEIOU"
    
    # 创建一个字典以便快速查找 "下一个" 辅音
    # e.g., 'b' -> 'c', 'z' -> 'b'
    next_lower_map = {LOWER_CONSONANTS[i]: LOWER_CONSONANTS[(i + 1) % 21] for i in range(21)}
    next_upper_map = {UPPER_CONSONANTS[i]: UPPER_CONSONANTS[(i + 1) % 21] for i in range(21)}

    # --- 2. 主逻辑 ---
    consonant_count = 0
    # 将字符串转为列表, 因为 Python 字符串是不可变的
    result_list = list(message)

    for i in range(len(result_list)):
        char = result_list[i]
        
        # 检查是否是元音或非字母 (如 ' ', ',')
        if char in VOWELS or not char.isalpha():
            continue
            
        # --- 此时, char 必定是一个辅音 ---
        consonant_count += 1
        
        # 检查这是否是我们要替换的第 n 个辅音
        if consonant_count % n == 0:
            # 是, 执行替换
            if char.islower():
                result_list[i] = next_lower_map[char]
            else:
                result_list[i] = next_upper_map[char]

    # --- 3. 返回结果 ---
    # 将列表重新组合成字符串
    return "".join(result_list)

# --- 测试 (使用示例) ---
message1 = "CodeSignal"
n1 = 3
print(f"'{message1}' (n=3) -> '{solution(message1, n1)}'")
# 输出: 'CodeSignal' (n=3) -> 'CodeTignam'

message2 = "Quiz, citizenship, puzzle"
n2 = 5
print(f"'{message2}' (n=5) -> '{solution(message2, n2)}'")
# 输出: 'Quiz, citizenship, puzzle' (n=5) -> 'Quiz, citi benship, puqzle'