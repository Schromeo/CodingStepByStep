from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
test = Solution()
print(test.levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))  # [[3], [9, 20], [15, 7]]
print(test.levelOrder(TreeNode(1)))  # [[1]]
print(test.levelOrder(None))  # []
print(test.levelOrder(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))))  # [[1], [2, 3], [4, 5]]
print(test.levelOrder(TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, None, TreeNode(5)))))  # [[1], [2, 3], [4, 5]]
print(test.levelOrder(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6), None), None), TreeNode(3, None, TreeNode(5, None, TreeNode(7))))))  # [[1], [2, 3], [4, 5], [6, 7]]
print(test.levelOrder(TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))))  # [[1], [2], [3], [4]]
print(test.levelOrder(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), None), None), None)))  # [[1], [2], [3], [4]]
print(test.levelOrder(TreeNode(1, TreeNode(2), None)))  # [[1], [2]]
print(test.levelOrder(TreeNode(1, None, TreeNode(2))))  # [[1], [2]]
