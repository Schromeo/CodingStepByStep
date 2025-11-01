'''
假设有一个团队聊天室，有很多用户在里面发消息。聊天支持两种操作：

"MESSAGE" (消息): 向一组用户发送消息。格式为 ["MESSAGE", "<timestamp>", "<mentions>"]。<mentions> 字符串包含以下用空格分隔的标记：

id<number>：@ 某个特定用户 (例如 "id1", "id34")。

ALL：@ 所有人。

HERE：@ 所有“活跃”用户。

"OFFLINE" (离线): 使一个给定 id 的用户“非活跃” 60 个时间单位。该用户将在 <timestamp> + 60 时刻自动恢复“活跃”。保证当此操作应用时，该用户一定是活跃的。格式为 ["OFFLINE", "<timestamp>", "<id>"]。

注意：所有的 events（事件）都已按时间戳 timestamp 排序。

你的任务是计算“@提及”统计。给定聊天室的用户列表 (members) 和一系列聊天事件 (events)，计算每个用户被消息“@提及”了多少次。

返回一个字符串数组，每个字符串的格式为 "[user id]=[mentions count]"。该数组必须按 user id 的字母顺序升序排列。
'''
from collections import defaultdict

def solution(members, events):
    
    # 1. 初始化
    
    # total_mention_counts: 存储每个成员的总提及次数
    total_mention_counts = {member: 0 for member in members}
    
    # active_users: 一个集合，跟踪当前 "在线/活跃" 的用户
    active_users = set(members)
    
    # offline_users_end_time: 一个字典，存储 "离线" 用户
    # 键 = user_id, 值 = 他们将 "恢复在线" 的时间戳
    offline_users_end_time = {}

    # --- 2. 遍历所有事件 (已按时间排序) ---
    for event in events:
        operation = event[0]
        timestamp = int(event[1])

        # --- 3. 状态更新：在处理事件 *之前*，先让离线的用户恢复在线 ---
        #
        # 找出所有 "离线结束时间" <= "当前时间" 的用户
        users_back_online = []
        for user_id, end_time in offline_users_end_time.items():
            if timestamp >= end_time:
                users_back_online.append(user_id)
                
        # 让这些用户恢复 "活跃" 状态
        for user_id in users_back_online:
            active_users.add(user_id)
            # 从离线字典中移除
            del offline_users_end_time[user_id]

        # --- 4. 处理 "MESSAGE" 操作 ---
        if operation == "MESSAGE":
            # 找出本次消息中 @提及 的 *所有* 用户的集合
            mentioned_in_this_message = set()
            
            # 检查是否有提及字符串 (e[2])
            if len(event) > 2:
                mention_string = event[2]
                parts = mention_string.split()
                
                for part in parts:
                    if part == "ALL":
                        # 添加所有成员
                        mentioned_in_this_message.update(members)
                    elif part == "HERE":
                        # 添加所有 *当前* 活跃的用户
                        mentioned_in_this_message.update(active_users)
                    elif part.startswith("id"):
                        # 添加特定的 "idX"
                        mentioned_in_this_message.add(part)
            
            # 5. 累加计数
            # 遍历本次消息@到的所有人
            for user in mentioned_in_this_message:
                # 检查这个被@的人是否是 "合法" 成员 (防止@不存在的人)
                if user in total_mention_counts:
                    total_mention_counts[user] += 1

        # --- 6. 处理 "OFFLINE" 操作 ---
        elif operation == "OFFLINE":
            user_id = event[2]
            
            # (题目保证用户此时一定是活跃的)
            if user_id in active_users:
                active_users.remove(user_id)
                # 记录他们将在 "当前时间 + 60" 时恢复
                offline_users_end_time[user_id] = timestamp + 60

    # --- 7. 格式化输出 ---
    
    # 按字母顺序排序
    sorted_members = sorted(members)
    
    # 使用列表推导式构建最终的格式化字符串
    result_strings = []
    for member in sorted_members:
        count = total_mention_counts[member]
        result_strings.append(f"{member}={count}")
        
    return result_strings

# --- 运行示例 ---
members = ["id1", "id2", "id3"]
events = [
    ["MESSAGE", "0", "id1"],                  # id1=1
    ["MESSAGE", "9", "HERE id3"],             # id1=2, id2=1, id3=1 (假设都活跃)
    ["OFFLINE", "10", "id1"],                 # id1 离线
    ["MESSAGE", "20", "HERE ALL"],            # id2=2, id3=2 (HERE) | id1=3 (ALL)
    ["MESSAGE", "80", "id1"]                  # id1 在 10+60=70 时恢复在线。id1=4
]

print(f"成员: {members}")
print(f"事件: {events}")
print(f"结果: {solution(members, events)}")
# 预期: ['id1=4', 'id2=2', 'id3=2']