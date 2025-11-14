from collections import deque
from typing import List
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bob_path = self.dfs(-1, 0, [], graph)
        for i in range(len(bob_path) // 2):
            amount[bob_path[i]] = 0
        if len(bob_path) % 2: # bob's path is odd, so bob and alice will definately meet in the center
            amount[bob_path[len(bob_path) // 2]] //= 2
        
        # using bfs to traverse alice path and add value
        queue = deque()
        queue.append((-1, 0, amount[0]))
        curr_max = None

        while queue:
            for _ in range(len(queue)):
                prev, node, value = queue.popleft()
                if len(graph[node]) == 1 and node != 0: # alice reaches the leave node
                    curr_max = max(curr_max, value) if curr_max is not None else value
                else:
                    for neighbor in graph[node]:
                        if neighbor != prev:
                            queue.append((node, neighbor, value + amount[neighbor]))
        
        return curr_max
    
    def dfs(self, prev, node, path, graph):
        path.append(node)
        if node == 0: # bob reached the start node
            return path
        for neighbor in graph[node]:
            if neighbor != prev:
                return_val = self.dfs(node, neighbor, path, graph)
                if return_val is not None:
                    return path
        path.pop()
        return None
    
