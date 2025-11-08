'''
# 电脑中的每个程序都可以被视为一个进程。
# 每个进程都会占用一些内存块，并有一个唯一的进程ID。
# 你将获得一个代表进程ID的整数列表。

# 索引 i 处的元素 x 代表一个 ID 为 x 的进程，
# 占用了内存块 i。

# 给定一个 start_index (起始索引)、一个 end_index (结束索引) 和一个
# processId (进程ID)，返回该进程在起始和结束索引
# 之间 (包含两者) 占用了多少个内存块。
# 如果边界无效，返回 0。

# 示例:
# 输入: ids = [12, 6, 12, 32, 12, 12, 6, 12, 9, 8],
#        left = 2, right = 5, processId = 12
# 输出: 3
# 解释: 在索引 2 和 5 之间，进程ID 12
# 占用了 3 个内存块，分别位于索引 2, 4, 和 5。
'''
def count_memory_blocks(process_ids, start_index, end_index, target_process_id):
    """
    计算一个进程ID在指定索引范围内占用的内存块数量。

    Args:
        process_ids (list): 代表内存块的进程ID列表。
        start_index (int): 起始索引 (包含)。
        end_index (int): 结束索引 (包含)。
        target_process_id (int): 要查找的目标进程ID。

    Returns:
        int: 目标进程ID在范围[start, end]内出现的次数。
    """
    
    # --- 1. 处理无效边界 ---
    
    list_length = len(process_ids)
    
    # 检查:
    # 1. start_index 是否为负
    # 2. end_index 是否超出了数组范围
    # 3. start_index 是否大于 end_index
    if start_index < 0 or end_index >= list_length or start_index > end_index:
        return 0

    # --- 2. 遍历和计数 ---
    
    count = 0
    # 遍历从 start_index 到 end_index (包含！)
    for i in range(start_index, end_index + 1):
        if process_ids[i] == target_process_id:
            count += 1
            
    return count

# --- 运行示例 ---
ids = [12, 6, 12, 32, 12, 12, 6, 12, 9, 8]
left = 2
right = 5
processId = 12

print(f"输入: ids={ids}, left={left}, right={right}, processId={processId}")
print(f"输出: {count_memory_blocks(ids, left, right, processId)}")

# 另一个边界测试
left_invalid = 6
right_invalid = 5
print(f"\n输入: ids={ids}, left={left_invalid}, right={right_invalid}, processId={processId}")
print(f"输出: {count_memory_blocks(ids, left_invalid, right_invalid, processId)}")