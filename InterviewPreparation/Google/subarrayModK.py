'''
我们要解决的问题是（我们用 M 代替那个大数字 6,000,009）：

给你一个正整数数组 nums 和两个整数 k 和 M。 你需要判断是否存在一个连续的非空子数组 nums[i...j] (从索引 i 到 j，包含 i 和 j)，使得这个子数组的数字和对 M 取余后，结果等于 k。

用数学的话说：(sum(nums[i...j]) % M) == k
'''

'''
我们要利用“模运算” (Modulo Arithmetic) 的一个神奇属性。

(A - B) % M 等价于 ( (A % M) - (B % M) + M ) % M

(注：多加一个 M 是为了防止 (A % M) - (B % M) 变成负数，这在数学上能保证结果正确)

现在，我们把这个属性应用到我们的目标等式上：

令 A = P[j]

令 B = P[i-1]

我们的目标 (P[j] - P[i-1]) % M == k 就等价于：

( (P[j] % M) - (P[i-1] % M) + M ) % M == k

'''
class Solution:
    def has_subarray_k_mod(nums: list[int], k: int, M: int) -> bool:
        """
        使用前缀和与哈希表，在 O(N) 时间内
        检查是否存在子数组和模 M 等于 k。
        """
    
        # 1. & 3. 初始化哈希集合，并预先存入 0
        #    这个 0 代表 P[-1] % M (数组开始前的前缀和模数)
        #    用于处理从索引 0 开始的子数组
        seen_mods = {0}
        
        # 2. 初始化当前的前缀和
        current_prefix_sum = 0
        
        # 4. 遍历数组
        for num in nums:
            
            # a. 更新前缀和
            current_prefix_sum += num
            
            # b. 计算当前的前缀和模 M
            #    (注：(a + b) % M == ((a % M) + (b % M)) % M)
            #    为了防止 current_prefix_sum 变得过大，
            #    我们可以在每一步都取模，但在这里直接加总更清晰
            current_mod = current_prefix_sum % M
            
            # c. 计算我们 "寻找" 的目标
            #    target = (current - k) % M
            target_past_mod = (current_mod - k + M) % M
            
            # d. 检查 "目标" 是否在 "过去" 出现过
            if target_past_mod in seen_mods:
                # 找到了！
                return True
                
            # e. 将 "当前" 变为 "过去"，存入哈希表
            seen_mods.add(current_mod)

        # 5. 循环结束，未找到
        return False