# 假设 Node 类的定义如上
class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        # (为了方便演示，我们加一个 id)
        self.id = id(self) 

    def __repr__(self):
        # 方便打印
        return f"Node({self.val}, id={self.id % 100})"

def count_graph_islands(all_nodes: list[Node]) -> int:
    """
    计算一个“图”结构中由 1 组成的岛屿数量。
    """
    
    island_count = 0
    
    # 最大的不同：我们必须用一个 "visited" 集合
    visited = set()
    
    # 1. 我们的主循环：不再是 for r... for c...
    #    而是遍历我们拿到的所有节点
    for node in all_nodes:
        
        # 检查是否满足“发现新大陆”的条件：
        # 1. 它必须是陆地 (val == 1)
        # 2. 它必须是 *还未被访问过* 的陆地
        if node.val == 1 and node not in visited:
            
            # 找到了一个新岛屿！
            island_count += 1
            
            # 2. "淹没" 这个岛屿上所有相连的陆地
            #    我们把 visited 集合传进去
            _dfs_sink_graph(node, visited)
            
    return island_count


def _dfs_sink_graph(node: Node, visited: set):
    """
    (DFS 淹没函数 - 图版本)
    从 'node' 出发，"淹没" (即, 添加到 visited)
    所有与之相连的、且 val 为 1 的节点。
    """
    
    # --- DFS 的 base cases (终止条件) ---
    
    # Base Case 1: 如果节点已经被访问过，停止
    if node in visited:
        return
        
    # Base Case 2: 如果节点是 "水" (val == 0)，停止
    if node.val == 0:
        return
        
    # --- 核心操作 ---
    
    # 1. "淹没" 当前节点：将其标记为已访问
    visited.add(node)
    
    # 2. 递归地去 "淹没" 所有的邻居
    #    这就是 "找邻居" 的方式从 "上下左右" 
    #    变成了 "遍历 neighbors 列表"
    for neighbor in node.neighbors:
        if neighbor not in visited:
            _dfs_sink_graph(neighbor, visited)