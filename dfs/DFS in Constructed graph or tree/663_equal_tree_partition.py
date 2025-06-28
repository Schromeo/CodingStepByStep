'''# LeetCode 663: Equal Tree Partition
# Given a binary tree with n nodes, determine if you can partition the tree into two trees with equal sum by removing exactly one edge.
# The problem requires checking if there exists a subtree whose sum is exactly half of the total sum of the tree.
# If such a subtree exists (excluding the entire tree), return True; otherwise, return False.
# Args:
#     root (TreeNode): The root node of the binary tree.
# Returns:
#     bool: True if the tree can be partitioned into two equal sum trees, False otherwise.
# Example:
#     Input: [5,10,10,2,3,3,2]
#     Output: True
# 
# '''
from collections import defaultdict
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        sub_sum_count = defaultdict(int)
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            total = left + right + node.val
            sub_sum_count[total] += 1
            return total
        
        total_sum = dfs(root)
        sub_sum_count[total_sum] -= 1  # Exclude the total sum itself
        if total_sum % 2 != 0:
            return False
        return (total_sum // 2) in sub_sum_count