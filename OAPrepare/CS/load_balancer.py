'''
假设你正在实现一个简化的负载均衡器，将用户请求路由到多个服务器。
你将获得一个整数数组 serversPowers，其中 serversPowers[i] 代表第 i 个服务器的容量——即它在每个周期内能处理的最大请求数。
你还将获得一个字符串数组 events，其中 events[i] 是以下之一：

    "REQUEST" - 用户请求
    "FAIL <i>" - 关闭第 i 个服务器（0-indexed），使其无法再服务任何请求

负载均衡器按循环顺序将请求路由到服务器。 （根据示例轨迹）路由逻辑如下：
系统维护一个 currentServerIndex（下一个要检查的服务器）。
当一个 "REQUEST" 到达时，系统从 currentServerIndex 开始，按循环顺序检查服务器。
它将请求分配给第一个尚未失败且当前周期容量 > 0 的服务器。
分配后，currentServerIndex 更新为 (i + 1) % n。
如果它检查了所有服务器，发现它们要么已满，要么已失败，它会重置所有非失败服务器的容量，将 currentServerIndex 设为 0，然后重新尝试路由该请求。

注意：
    路由时，负载均衡器应跳过所有已失败的服务器。
    保证始终至少有一个服务器在运行。
    返回总共服务了最多请求的服务器的索引。如果平局，返回这些服务器中索引最大的那个。
'''
def solution(serversPowers, events):
    """
    模拟负载均衡器，跟踪累积请求并处理周期性容量重置。
    """
    n = len(serversPowers)
    
    # --- 1. 状态变量 ---
    
    # totalRequestCounts 跟踪每个服务器的总请求数 (永不重置)
    totalRequestCounts = [0] * n
    
    # currentCapacities 跟踪当前周期的剩余容量
    # (在循环重置时会重置)
    currentCapacities = list(serversPowers)
    
    # isDown 跟踪失败的服务器
    isDown = [False] * n
    
    # 下一个要检查的服务器的索引
    currentServerIndex = 0

    # --- 2. 辅助函数：重置周期容量 ---
    def reset_capacities():
        nonlocal currentCapacities
        for i in range(n):
            if not isDown[i]:
                # 只重置非失败服务器的容量
                currentCapacities[i] = serversPowers[i]
            else:
                # 失败的服务器容量保持为 0
                currentCapacities[i] = 0
    
    # --- 3. 辅助函数：处理请求 ---
    def handle_request():
        nonlocal currentServerIndex
        
        # 从 currentServerIndex 开始, 检查所有服务器 (最多 n 次)
        for i in range(n):
            idx_to_check = (currentServerIndex + i) % n
            
            # 检查服务器是否 UP 且有 CAPACITY
            if not isDown[idx_to_check] and currentCapacities[idx_to_check] > 0:
                # --- 服务器找到 ---
                totalRequestCounts[idx_to_check] += 1
                currentCapacities[idx_to_check] -= 1
                
                # 下一个请求将从该服务器的 "下一个" 开始检查
                currentServerIndex = (idx_to_check + 1) % n
                return True # 请求已处理
        
        # --- 没有服务器可用 (全部已满或已失败) ---
        return False # 请求未处理

    # --- 4. 主事件循环 ---
    for event_str in events:
        parts = event_str.split()
        command = parts[0]
        
        if command == "REQUEST":
            # 尝试处理请求
            if not handle_request():
                # --- 周期重置 ---
                # 如果 handle_request 返回 False (所有服务器都满了)
                # 1. 重置容量
                reset_capacities()
                # 2. 将 currentServerIndex 重置为 0
                currentServerIndex = 0
                # 3. 重新尝试处理该请求 (这次必定成功)
                handle_request()
                
        elif command == "FAIL":
            fail_idx = int(parts[1])
            isDown[fail_idx] = True
            currentCapacities[fail_idx] = 0 # 立即将其当前容量设为 0

    # --- 5. 寻找获胜者 ---
    max_requests = -1
    result_index = -1
    
    # 遍历索引 0, 1, 2...
    for i in range(n):
        # 如果 > max, 则重置
        if totalRequestCounts[i] > max_requests:
            max_requests = totalRequestCounts[i]
            result_index = i
        # 如果 == max, 则更新为更大的索引 (平局规则)
        elif totalRequestCounts[i] == max_requests:
            result_index = i
            
    return result_index

# --- 测试 ---
serversPowers = [1, 2, 1, 2, 1]
events = ["REQUEST", "REQUEST", "FAIL 2", "REQUEST", "FAIL 3", "REQUEST", "REQUEST"]
print(f"示例 1 (预期 1): {solution(serversPowers, events)}")
# 轨迹:
# REQ -> 0 (counts=[1,0,0,0,0], caps=[0,2,1,2,1], next=1)
# REQ -> 1 (counts=[1,1,0,0,0], caps=[0,1,1,2,1], next=2)
# FAIL 2   (isDown=[F,F,T,F,F], caps=[0,1,0,2,1])
# REQ -> 1 (counts=[1,2,0,0,0], caps=[0,0,0,2,1], next=2)
# FAIL 3   (isDown=[F,F,T,T,F], caps=[0,0,0,0,1])
# REQ -> 4 (counts=[1,2,0,0,1], caps=[0,0,0,0,0], next=0)
# REQ -> RESET! (caps=[1,2,0,0,1], next=0)
#     -> 0 (counts=[2,2,0,0,1], caps=[0,2,0,0,1], next=1)
# 最终 counts: [2, 2, 0, 0, 1]
# max=2, tie at 0 and 1. 返回最大索引 1.