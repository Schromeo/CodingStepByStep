import heapq
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        id = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, id, l))
                id += 1
        dummy = ListNode(0)
        current = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id, node.next))
                id += 1
        return dummy.next