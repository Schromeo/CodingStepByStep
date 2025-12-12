'''
题目:

    实现一个数据结构 Tree，支持以下操作:
        createNode(parent)
            在给定父节点下创建一个新节点（树的容量有限）。
        getRandomNode()
            随机返回树上的任意一个节点，要求等概率。
    Follow-up:getRandomLeaf()
        随机返回树上的任意一个叶子节点，要求等概率。
        初始树只有一个节点 root，它既是节点也是叶子。
    要求所有操作最好能达到 O(1)。
'''
'''
Clarify Questions
Q1: 树是否只会“新增节点”，是否会删除节点？
A1: 是的，只有新增节点，没有删除操作。

Q2:初始树是什么状态？
A2: 只有一个 root 节点，它既是节点也是叶子节点。

Q3:树的容量 capacity 是什么意思？
A3: 最大允许的节点数。如果超过 capacity，应抛出异常或报错。

Q4:getRandomNode() 的要求？
A4:所有节点等概率被返回平均时间复杂度应为 O(1)

Q5（follow-up）:如何随机获取叶子？叶子定义是什么？

A5:
    叶子节点 = 没有 children 的节点
    要求所有叶子等概率
    时间复杂度同样应为 O(1)
'''

'''
解法思想：

    实现随机：必须把候选节点放进数组，并用随机索引选取
    nodes: 存所有节点 → 用于 getRandomNode
    leaves: 存所有叶子节点 → 用于 getRandomLeaf
    leafIndex: 记录某个叶子在 leaves 中的 index, 方便在 O(1) 时间删除一个叶子（通过覆盖/替换）

    我用两个数组分别管理节点集合和叶子集合。
    nodes[] 用于随机取任意节点，leaves[] 用于随机取叶子节点。
    插入新节点时，我检查 parent 是否为叶子。如果是，我在 O(1) 时间内把它在 leaves[] 中的 slot 替换成 child，同时更新 leafIndex。如果不是，我把 child append 到 leaves[]。
    整个过程都是 O(1)，随机查询也是 O(1)。
'''
import random
class TreeNode:
    def __init__(self):
        self.parent = None
        self.children = []

class Tree:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.root = TreeNode()

        self.nodes = [self.root]
        self.leaves = [self.root]
        self.leafIndex = {self.root: 0}
        self.rand = random.Random()
    
    def createNode(self, parent: TreeNode):
        if len(self.nodes) == self.capacity:
            raise Exception("Tree is Full")
        newNode = TreeNode()
        newNode.parent = parent
        parent.children.append(newNode)

        if parent in self.leafIndex:
            idx = self.leafIndex[parent]
            self.leaves[idx] = newNode
            self.leafIndex[newNode] = idx
            del self.leafIndex[parent]
        else:
            self.leaves.append(newNode)
            self.leafIndex[newNode] = len(self.leaves) - 1
        
        self.nodes.append(newNode)
        return newNode
    
    def getRandomNode(self) -> TreeNode:
        idx = self.rand.randint(0, len(self.nodes) - 1)
        return self.nodes[idx]
    
    def getRandomLeaf(self) -> TreeNode:
        idx = self.rand.randint(0, len(self.leaves)-1)
        return self.leaves[idx]

