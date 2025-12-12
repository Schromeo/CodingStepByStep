'''
There is a company whichh has a CEO and a hierachy of employees.
All employees have a unique ID, name, and a pointer to their manager and their reports.
Please implement the whoIsOurBoss() method to find the closest manager for two given employees
(i.e. the manager farthest from the CEO that both employees report up to)

'''


'''
Clarify Questions:

    1. 是否这些节点构成了一个树？
        是Tree
    2. 如果输入两个节点，其中一个CEO，应该返回什么？
        返回None
    3. 会不会出现输入的两个节点是同一个节点？
        返回两个点的父节点
    4. 给一个例子
'''

class TreeNode:
    def __init__(self):
        self.Id = None
        self.manager = None
        self.reports = None

def getDepth(emp: TreeNode) -> int:
    depth = 0
    while emp:
        depth += 1
        emp = emp.manager
    return depth

def whoIsOurBoss(emp1: TreeNode, emp2:TreeNode) -> TreeNode:
    emp1_copy = emp1
    emp2_copy = emp2
    depth1 = getDepth(emp1)
    depth2 = getDepth(emp2)
    diff = abs(depth1 - depth2)
    if depth1 > depth2:
        emp1, emp2 = emp2, emp1
    for _ in range(diff):
        emp2 = emp2.manager
    while emp1 != emp2:
        emp1 = emp1.manager
        emp2 = emp2.manager
    LCA = emp1
    if LCA == emp1_copy or LCA == emp2_copy:
        LCA = LCA.manager
    return LCA

'''
Notes:
你可以在脑子里把这题归类成：

    「带 parent 指针的 LCA 模板 + 特殊业务规则」

模板步骤固定三句：

    getDepth(node)：
    一路往上 .manager 数层数

    先对齐高度：
    把更深的那个往上抬差值层

    一起往上走：
    同步往上直到相遇，返回相遇点

然后这道题的业务补丁是：

    如果相遇点是输入的其中一个节点（包括俩人相同） → 再往上走一层

    如果那一层是 None（说明本来就是 CEO） → 返回 None

'''