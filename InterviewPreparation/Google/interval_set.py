'''
请你设计一个类 IntervalSet，它需要支持以下两种操作：

    void add(int left, int right):

        添加一个新的区间 [left, right] 到集合中。

        注意：这个新的区间可能会与集合中已有的区间产生重叠或相邻。

    boolean query(int point):

        查询一个点 point 是否被任何已经添加的区间所覆盖。

        如果 point 落在至少一个区间内（包括端点），则返回 true；否则返回 false。

'''
class IntervalSet_sorted_list:
    def __init__(self):
        self.intervals = []

    # ----------------------------------------------------
    # 辅助方法：手写二分查找 (我们的核心替换)
    # ----------------------------------------------------
    
    def _find_first_greater(self, point: int) -> int:
        """
        手写二分查找 (替换 bisect_right)
        功能：找到第一个区间 [start, end]，使得 start > point。
        返回这个区间的索引 i。
        如果所有区间的 start都 <= point，则返回 len(self.intervals)。
        """
        low, high = 0, len(self.intervals)
        
        while low < high:
            mid = (low + high) // 2
            
            # 我们只关心区间的 start 值
            if self.intervals[mid][0] <= point:
                # [mid] 的 start 不够大，我们去右边找
                low = mid + 1
            else: # self.intervals[mid][0] > point
                # [mid] 可能是答案，但我们尝试在左边找个更早的
                high = mid
                
        # low (或 high) 就是第一个 start > point 的位置
        return low

    def _find_insertion_point(self, left: int) -> int:
        """
        手写二分查找 (替换 bisect_left)
        功能：找到第一个区间 [start, end]，使得 start >= left。
        返回这个区间的索引 i。
        """
        low, high = 0, len(self.intervals)
        
        while low < high:
            mid = (low + high) // 2
            
            if self.intervals[mid][0] < left:
                # [mid] 的 start 太小了，去右边找
                low = mid + 1
            else: # self.intervals[mid][0] >= left
                # [mid] 可能是答案，去左边找更早的
                high = mid
                
        # low (或 high) 就是第一个 start >= left 的位置
        return low

    # ----------------------------------------------------
    # 主要方法：现在使用我们的辅助函数
    # ----------------------------------------------------

    def add(self, left: int, right: int) -> None:
        """
        添加区间，时间复杂度: O(N)
        (O(logN) 查找 + O(N) 插入 + O(N) 合并)
        """
        new_interval = [left, right]
        
        # 步骤 1: O(log N) 找到插入点
        index_to_insert = self._find_insertion_point(left)
        
        # 步骤 2: O(N) 插入
        # list.insert() 是一个 O(N) 操作，因为它需要移动后续所有元素
        self.intervals.insert(index_to_insert, new_interval)
        
        # 步骤 3: O(N) 合并 (这部分逻辑和之前一样)
        merged = []
        for interval in self.intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        self.intervals = merged

    def query(self, point: int) -> bool:
        """
        查询点，时间复杂度: O(log N)
        (使用我们 O(log N) 的 _find_first_greater)
        """
        # 1. 找到第一个 start > point 的区间索引
        i = self._find_first_greater(point)
        
        # 2. 如果 i = 0, 说明 point 在所有区间之前
        if i == 0:
            return False
            
        # 3. 唯一的可能性是 point 落在 i-1 这个区间
        candidate_interval = self.intervals[i-1]
        start = candidate_interval[0]
        end = candidate_interval[1]
        
        # 4. 检查 point 是否真的在 [start, end] 范围内
        return start <= point <= end


class IntervalSetSegmentTree:
    """
    使用线段树（带懒惰传播）实现区间集合。
    
    这个实现假设所有操作都在一个固定的 [0, max_range] 范围内。
    
    - self.tree 存储: "这个节点代表的区间是否 *完全* 被覆盖了"
    - self.lazy 存储: "这个节点是否有 '待覆盖' 标记要传递给子节点"
    """
    
    def __init__(self, max_range: int):
        # 1. 初始化范围
        self.max_range = max_range
        
        # 2. 初始化线段树和懒惰标记数组
        #    为什么是 4*N ? 这是构建满二叉树所需空间的一个安全上界。
        size = 4 * (self.max_range + 1)
        self.tree = [False] * size  # 节点：是否被覆盖 (True/False)
        self.lazy = [False] * size  # 节点：是否需要向下传播 "覆盖" 标记

    
    def _push_down(self, node: int, node_l: int, node_r: int):
        """
        懒惰传播的核心：将当前节点的 'lazy' 标记下推给子节点。
        """
        # 如果当前节点 (node) 根本没有 lazy 标记，就什么也不做
        if not self.lazy[node]:
            return
            
        # 1. 清除当前节点的 lazy 标记
        self.lazy[node] = False
        
        # 2. 将 "True" (覆盖) 标记应用到当前节点
        self.tree[node] = True
        
        # 3. 如果不是叶子节点，将 lazy 标记传递给两个子节点
        if node_l != node_r:
            self.lazy[2 * node + 1] = True  # 标记左孩子
            self.lazy[2 * node + 2] = True  # 标记右孩子

            
    def add(self, left: int, right: int) -> None:
        """
        公共方法：在 [left, right] 区间添加覆盖。
        这是一个 O(log M) 操作 (M 是总范围 max_range)。
        """
        # 我们从根节点 (node=0) 开始，它代表整个范围 [0, max_range]
        self._update_range(0, 0, self.max_range, left, right)

        
    def _update_range(self, node: int, node_l: int, node_r: int, add_l: int, add_r: int):
        """
        私有方法：递归地更新 [add_l, add_r] 区间。
        """
        
        # 1. 在处理任何逻辑之前，先处理并下推当前节点的 lazy 标记
        self._push_down(node, node_l, node_r)
        
        # --- 递归的终止条件 ---
        
        # Case 1: [add_l, add_r] 与 [node_l, node_r] 完全没有交集
        if add_l > node_r or add_r < node_l:
            return
            
        # Case 2: [node_l, node_r] 完全包含在 [add_l, add_r] 内部
        #    (例如：add(0, 50)，当前节点是 [10, 20])
        if add_l <= node_l and node_r <= add_r:
            # 在当前节点打上 lazy 标记
            self.lazy[node] = True
            # ...然后立刻处理它，更新自己并 (如果需要) 标记孩子
            self._push_down(node, node_l, node_r)
            return
            
        # --- 递归的深入 ---
        
        # Case 3: 部分重叠
        #    (例如：add(0, 10)，当前节点是 [0, 20])
        # 我们必须递归地去处理左右子树
        mid = (node_l + node_r) // 2
        self._update_range(2 * node + 1, node_l, mid, add_l, add_r)
        self._update_range(2 * node + 2, mid + 1, node_r, add_l, add_r)
        
        # 4. (重要) 回溯时，更新父节点的 "is_covered" 状态
        #    一个父节点被覆盖 = 它的左孩子被覆盖 OR 它的右孩子被覆盖
        self.tree[node] = self.tree[2 * node + 1] or self.tree[2 * node + 2]


    def query(self, point: int) -> bool:
        """
        公共方法：查询 'point' 是否被覆盖。
        这是一个 O(log M) 操作 (M 是总范围 max_range)。
        """
        return self._query_point(0, 0, self.max_range, point)

        
    def _query_point(self, node: int, node_l: int, node_r: int, point: int) -> bool:
        """
        私有方法：递归地查询 'point'。
        """
        
        # 1. (极其重要) 在查询之前，必须先处理 lazy 标记！
        #    否则我们可能会读到过时的数据
        self._push_down(node, node_l, node_r)

        # 2. 如果我们已经知道这个节点 [node_l, node_r] 被覆盖了
        #    那么里面的 'point' 肯定也被覆盖了
        if self.tree[node]:
            return True

        # 3. 如果没被覆盖，并且已经是叶子节点了，那 'point' 肯定没被覆盖
        if node_l == node_r:
            return self.tree[node] # 此时一定是 False

        # --- 递归的深入 ---
        
        # 4. 向下走到包含 'point' 的那个子树
        mid = (node_l + node_r) // 2
        if point <= mid:
            # 'point' 在左半边
            return self._query_point(2 * node + 1, node_l, mid, point)
        else:
            # 'point' 在右半边
            return self._query_point(2 * node + 2, mid + 1, node_r, point)



# 创建一个实例
s = IntervalSet_sorted_list()

# 添加 [1, 5]
s.add(1, 5) 
# s.intervals 现在是: [[1, 5]]

# 添加 [8, 10] (不重叠)
s.add(8, 10)
# s.intervals 现在是: [[1, 5], [8, 10]]

# 添加 [3, 7] (重叠了 [1, 5])
s.add(3, 7)
# 1. 插入后，列表是: [[1, 5], [3, 7], [8, 10]] (排序了，但未合并)
# 2. 合并后，列表是: [[1, 7], [8, 10]] (完美！)

# 添加 [7, 12] (重叠了 [1, 7] 和 [8, 10])
s.add(7, 12)
# 1. 插入后: [[1, 7], [7, 12], [8, 10]] (注意 7 在 8 前面)
# 2. 合并后: [[1, 12]] (全部合并了！)

# 查询
print(f"查询 4: {s.query(4)}")   # True (在 [1, 12] 中)
print(f"查询 12: {s.query(12)}")  # True (在 [1, 12] 中)
print(f"查询 13: {s.query(13)}") # False (在 [1, 12] 之外)
print(f"查询 0: {s.query(0)}")   # False (在 [1, 12] 之外)
'''
方案,add (插入) 复杂度,query (查询) 复杂度,关键依赖/限制
1. 基础列表 (只追加),O(1) (最快),O(N) (最慢),N 必须很小
2. 排序合并列表 (核心解法),O(N) (较慢),O(logN) (极快),N 不能太大
3. 布尔数组 (位图),O(R) (最慢),O(1) (最快),M (范围) 必须很小
4. 线段树 (高级解法),O(logM) (极快),O(logM) (极快),M (范围) 必须固定

场景一：“如果 insert (add) 更多？”答案： 
    我们选择 方案 1：基础列表 (只追加)。
    理由： 我们的主要操作是 add，这个方案的 add 复杂度是 $O(1)$，是所有方案中最快的。我们愿意牺牲 query 的速度（让它变成 $O(N)$ 遍历）来换取 add 的极致性能。
场景二：“如果 query 更多？” 
    (标准情况)答案： 我们选择 方案 2：排序合并列表 (核心解法)。
    理由： 这是最标准的答案。我们通过二分查找，将 query 优化到了 $O(\log N)$，这非常快。我们愿意为此牺牲 add 的性能，让它承担 $O(N)$ 的“插入并合并”的脏活累活。
场景三：“如果 query 极其 频繁，且坐标范围很小 (如 0-100万)？”
    答案： 我们选择 方案 3 (布尔数组) 或 方案 4 (线段树)。
    理由：方案 3 (布尔数组) 提供了 $O(1)$ 的“瞬时”查询，这是最快的 query，但它的 add 代价 $O(R)$ 非常高，且极其消耗内存。
        方案 4 (线段树) 是最平衡的“高级解”。它的 add 和 query 都是 $O(\log M)$。因为 M 是固定的 (比如 $10^6$)，$\log M$ (约 20) 几乎是一个常数。这使得它在 $N$ (区间数) 变得非常大时，表现会优于方案 2。
'''