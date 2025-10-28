'''
将一个二叉搜索树 (BST) “原地” (in-place) 转换成一个排序的循环双向链表。

原地 (In-place)： 我们不创建新的 Node 节点，而是重新利用树中已有的 left 和 right 指针。

转换后：

Node.left 指针将扮演双向链表中 prev (前一个) 指针的角色。

Node.right 指针将扮演双向链表中 next (后一个) 指针的角色。

循环 (Circular)： 链表的“头”的 prev 应该指向“尾”，链表的“尾”的 next 应该指向“头”。

排序 (Sorted)： 因为输入是二叉搜索树 (BST)，所以我们转换后的链表必须是按节点值升序排列的。

'''
class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bst_to_doubly_list(root: 'Node') -> 'Node':
        if not root:
            return None

        prev = None
        head = None

        def dfs(node: 'Node'):
            nonlocal prev, head
            if not node:
                return 
            dfs(node.left)
            if prev:
                prev.right = node
                node.left =  prev
            else:
                head = node
            prev = node

            dfs(node.right)
        
        dfs(root)
        head.left = prev
        prev.right = head
        return head

if __name__ == "__main__":
    def test_empty_tree():
        result = Solution.bst_to_doubly_list(None)
        assert result is None
        print("✓ Empty tree test passed")

    def test_single_node():
        root = Node(1)
        result = Solution.bst_to_doubly_list(root)
        assert result.val == 1
        assert result.left == result
        assert result.right == result
        print("✓ Single node test passed")

    def test_three_nodes():
        root = Node(2)
        root.left = Node(1)
        root.right = Node(3)
        
        result = Solution.bst_to_doubly_list(root)
        
        assert result.val == 1
        assert result.right.val == 2
        assert result.right.right.val == 3
        assert result.left.val == 3
        assert result.right.right.right.val == 1
        print("✓ Three nodes test passed")

    def test_larger_tree():
        root = Node(4)
        root.left = Node(2)
        root.right = Node(5)
        root.left.left = Node(1)
        root.left.right = Node(3)
        
        result = Solution.bst_to_doubly_list(root)
        
        values = []
        current = result
        for _ in range(5):
            values.append(current.val)
            current = current.right
        assert values == [1, 2, 3, 4, 5]
        assert current == result
        print("✓ Larger tree test passed")

    # Run all tests
    test_empty_tree()
    test_single_node()
    test_three_nodes()
    test_larger_tree()
    print("All tests passed!")