'''
You are given a graph with N nodes and E edges.  
Each edge e has a security level S(e).

Given a security key with security level S, you are allowed to traverse 
only the edges whose security levels are ≤ S.

Your task is to determine the minimum security level required to travel 
from a start node u to an end node v.

In other words, consider any path from u to v.  
The cost of a path is defined as the maximum edge security level on that path.  
You must find a path whose cost is minimized.

---

Example:

Nodes: 1, 2, 3, 4

Edges (format: (u, v) -> S(u, v)):

(1, 2) -> 3  
(1, 3) -> 1  
(2, 4) -> 5  
(3, 4) -> 2

Start node: u = 1  
End node: v = 4

Possible paths:

1 → 2 → 4  
  - maximum edge level = max(3, 5) = 5

1 → 3 → 4  
  - maximum edge level = max(1, 2) = 2

Since we want the minimum security level required to travel from 1 to 4,  
the answer is 2.

给你一个图（无向图或有向图都可按同样方式处理），每条边有一个安全等级：

    边 (u, v) 的安全等级 = S(u, v)
如果你拥有一个安全等级为 S 的 key，那么你只能走安全等级 ≤ S 的边
你希望找到 从起点 u 走到终点 v 所需的最小安全等级值
这个“所需等级” = 你选的路径上所有边的 security level 的 最大值
所以我们要最小化路径的：
    max edge weight on the path

这叫：
    Minimize the maximum edge weight along the path
    → Minimum Bottleneck Path
    → Minimax Path

'''

'''
Clarifying Questions

Q1：边是有向还是无向？
A：若未特别说明，一般视为无向，但你的算法需要同时支持两者。

Q2：图是否可能不连通？若无法到达怎么办？
A：如果无法到达终点，应返回 -1 或 None。

Q3：边权是否都是正数？
A：是，安全等级一定为正整数。

Q4：节点数量是否很大？
A：可能很大，因此需要 O(E log V) 或 O(E α(n))（并查集）

Q5：是否可以修改输入结构？
A：可以，构建 adjacency list / edge list 都可以。
'''

import heapq
from collections import defaultdict

def minSecurityLevel(n, edges, start, end):
    """
    n: number of nodes (1-indexed)
    edges: list of (u, v, w)
    start, end: start and end nodes
    """

    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))   # if undirected

    # dist[x] = minimum possible maximum edge weight from start → x
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    # Min-heap stores (current_max_edge_in_path, node)
    pq = [(0, start)]

    while pq:
        max_so_far, node = heapq.heappop(pq)

        if node == end:
            return max_so_far

        if max_so_far > dist[node]:
            continue

        for nei, weight in graph[node]:
            new_cost = max(max_so_far, weight)
            if new_cost < dist[nei]:
                dist[nei] = new_cost
                heapq.heappush(pq, (new_cost, nei))

    return None  # unreachable
'''
✅ 面试官讲解思路（口述版）

“这道题要求我们从起点走到终点，同时最小化路径中出现的最大边权。这类问题通常被称为 minimax path 或者 bottleneck path。

核心思想是：
一条路径的代价不是所有边的和，而是所有边的最大值，我们希望让这个最大值尽量小。
因此传统 Dijkstra 的“加法”不适用，但我们可以把状态定义稍微修改一下：

🧠 状态定义

dist[x] 表示：
从起点到节点 x 所能达到的最小 possible 的最大边权。

也就是说，到达 x 的所有路径里，选一个让 路径最大边权 最小的。

🔄 状态转移

从当前节点走一条边 (x → y, 权重 w) 时，“代价”变成：

new_cost = max(dist[x], w)


如果这个 new_cost 比目前记录的 dist[y] 更小，我们就更新它并 push 进小根堆。

📦 算法框架

算法整体跟 Dijkstra 一模一样，只是把“路径和”替换成了 “路径最大值的最小化”。
因为 max() 也是单调操作，所以 Dijkstra 的贪心性质仍然成立。

我们用一个最小堆存 (当前路径最大边权, 节点)，每次取出当前 bottleneck 最小的节点。
当我们第一次从堆中取到目标节点时，它的 dist 值就是最终答案。

⏱️ 时间复杂度

因为流程和 Dijkstra 是一致的，所以复杂度是：

O(E log V)


足以应对大规模图。

📝 总结

这是一个典型的 minimax path 问题

解法是把 Dijkstra 的“加法”换成 max()

用最小堆保持当前最优 bottleneck

第一次 pop 到目标节点时即可返回答案

这个方法既直观又具有最优的复杂度。”
'''