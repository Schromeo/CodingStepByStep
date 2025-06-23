"""
LeetCode 101: Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree.

Args:
    root (TreeNode): The root node of the binary tree.

Returns:
    bool: True if the tree is symmetric, False otherwise.

Example:
    Input: [1,2,2,3,4,4,3]
    Output: True

    Input: [1,2,2,None,3,None,3]
    Output: False

LeetCode Link:
    https://leetcode.com/problems/symmetric-tree/
"""
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def solve(root1, root2):
            if root1 is None and root2 is None:
                return True

            if root1 is None or root2 is None or root1.val != root2.val:
                return False
            
            return solve(root1.left, root2.right) and solve(root1.right, root2.left)
        return solve(root, root) if root else True

