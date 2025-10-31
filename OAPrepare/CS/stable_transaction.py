'''
在一个财务监控系统中，你需要检测交易记录中的稳定期。给定一个非负整数数组 transactions（代表每日的交易净值）和一个正整数 k（代表一个稳定因子）。如果一个 transactions 的连续子数组的元素总和可以被 k 整除，则该子数组被视为一个稳定期。

你的任务是编写一个函数，找到最长稳定期的长度。
'''
def solution(t, k):
    # r_i (remainder_index): 存储 {余数: 第一次出现的索引}
    r_i = {}
    
    # ps (prefix_sum): 跟踪到目前为止的前缀和 % k
    ps = 0
    
    # ml (max_length): 跟踪找到的最长稳定期长度
    ml = 0
    
    for i, n in enumerate(t):
        # 1. 更新当前的前缀和 (模 k)
        ps = (ps + n) % k
        
        # 2. 检查: 如果 ps == 0
        if ps == 0:
            # 这意味着从 t[0] 到 t[i] 的总和可以被 k 整除
            # 这个稳定期的长度是 i + 1
            ml = i + 1
            
        # 3. 检查: 如果 ps 之前已经出现过
        elif ps in r_i:
            # 我们找到了一个循环!
            # 索引 r_i[ps] 处的 ps 和 索引 i 处的 ps 相同
            # 这意味着它们 "之间" 的子数组 t[r_i[ps]+1 ... i] 的和
            # 一定是 k 的倍数。
            #
            # 计算这个子数组的长度
            length = i - r_i[ps]
            
            # 更新最大长度
            ml = max(ml, length)
            
        # 4. 检查: 如果 ps 是第一次出现
        else:
            # 记录这个余数 ps 第一次出现的索引 i
            r_i[ps] = i
            
    # 5. 返回找到的最大长度
    return ml