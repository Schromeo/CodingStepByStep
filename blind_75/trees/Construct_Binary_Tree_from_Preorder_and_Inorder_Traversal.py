from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        in_map = {val: idx for idx, val in enumerate(inorder)}
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            in_root_idx = in_map[root_val]
            left_size = in_root_idx - in_start
            root.left = helper(pre_start+1, pre_end, in_start, in_root_idx-1)
            root.right = helper(pre_start+ left_size+1, pre_end, in_root_idx+1, in_end)
            return root
        return helper(0, len(preorder)-1, 0, len(inorder)-1)
    