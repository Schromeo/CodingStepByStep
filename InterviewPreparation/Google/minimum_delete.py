'''
通过最少删除，让 list2 的“新”前 K 个元素，与 list1 的“前 K 个”元素没有交集。

"给定list1、list2(长度不定)和值K，返回删除最少元素的list2，使得list1与list2中前K个
elements没有交集"
'''
def solve_optimal(list1: list, list2: list, K: int) -> list:
    """
    使用哈希集合和一次遍历，以 O(N+K) 的时间复杂度解决问题。
    N = len(list2)
    K = K (或 len(list1))
    """
    
    # 1. 建立“违禁”名单 (哈希集合)，O(K)
    #    我们只关心 list1 的前 K 个元素
    forbidden_set = set(list1[:K])
    
    # 2. 初始化两个“篮子”
    safe_prefix = []
    rest_of_list = []
    
    # 3. 遍历 list2 一次，O(N)
    for x in list2:
        
        # 情况一：我们的 "安全区" 还没满
        if len(safe_prefix) < K:
            
            # 检查 x 是否被禁止 (O(1) 查询)
            if x not in forbidden_set:
                # 不在！它是安全的，加入 "安全区"
                safe_prefix.append(x)
            else:
                # 在！它被 "删除" (即，我们跳过它)
                pass
                
        # 情况二：我们的 "安全区" 已经满了
        else:
            # 我们的任务已经完成。
            # 剩下的所有元素都无条件保留，以满足“最少删除”
            rest_of_list.append(x)
            
    # 4. 拼接并返回结果，O(N)
    return safe_prefix + rest_of_list