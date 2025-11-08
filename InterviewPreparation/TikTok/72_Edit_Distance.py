def min_distance(word1: str, word2: str) -> int:
    """
    计算将 word1 转换为 word2 所需的最小操作次数。
    """
    n = len(word1)
    m = len(word2)

    # 1. 创建 DP 表
    # dp[i][j] 表示 word1 的前 i 个字符 转换为 word2 的前 j 个字符
    # 需要的最小操作数。
    # 我们需要 (n+1) x (m+1) 的大小来处理空字符串的情况。
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 2. 初始化 (处理边界情况)
    # 当 word2 是空字符串时 (j=0)
    # word1 的前 i 个字符 变为空字符串，需要 i 次删除
    for i in range(n + 1):
        dp[i][0] = i

    # 当 word1 是空字符串时 (i=0)
    # 空字符串 变为 word2 的前 j 个字符，需要 j 次插入
    for j in range(m + 1):
        dp[0][j] = j

    # 3. 状态转移 (填写 DP 表)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 注意：dp[i][j] 对应的是 word1[i-1] 和 word2[j-1]
            char1 = word1[i - 1]
            char2 = word2[j - 1]

            if char1 == char2:
                # 两个字符相同，不需要额外操作
                # 操作数等于它们“前一个状态”的操作数
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 两个字符不同，必须进行 1 次操作 (增、删、改)
                # 我们选择这三种操作中，总代价最小的那一个
                
                # 1. 修改 (Replace):
                #    把 word1[i-1] 修改成 word2[j-1]
                #    代价 = 1 + (word1前i-1 变为 word2前j-1 的代价)
                replace_cost = dp[i - 1][j - 1] + 1
                
                # 2. 删除 (Delete):
                #    把 word1[i-1] 删掉
                #    代价 = 1 + (word1前i-1 变为 word2前j 的代价)
                delete_cost = dp[i - 1][j] + 1
                
                # 3. 插入 (Insert):
                #    在 word1[i-1] 后面插入 word2[j-1]
                #    代价 = 1 + (word1前i 变为 word2前j-1 的代价)
                insert_cost = dp[i][j - 1] + 1
                
                dp[i][j] = min(replace_cost, delete_cost, insert_cost)

    # 4. 返回最终答案
    # 整个 word1 (前n个) 变为 整个 word2 (前m个) 的代价
    return dp[n][m]

# --- 运行示例 ---
w1 = "horse"
w2 = "ros"
print(f"把 '{w1}' 变成 '{w2}' 的最小操作数是: {min_distance(w1, w2)}") 
# 预期输出: 3