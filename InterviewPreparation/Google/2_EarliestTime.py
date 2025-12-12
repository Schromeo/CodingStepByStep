'''
Here we have an event log file which is produced by the Friends service like below:

    1648305616 Alice and Bob become friends
    1648305678 Charlie and Dan become friends
    1648306171 Bob and Charlie become friends
    1648306237 Alice and Erin become friends

Given a list of all users and the logs above, implement a function to find the earliest time when everyone became reachable to every other person through the friends.
Reachability is symmetric. That means if person A is friends with B, A is reachable from B and B is reachable from Reachability is transitive.
That means if person A is friends with B, and B is friends with C, C is reachable from A through B.
'''

'''
Clarify Question:

    1. 如果处理完所有的日志，所有的人依然没有相互认识，输出什么？
        输出None
    2. 输入是否可以按照这样的形式来： 每一条日志log [时间，用户1，用户2]？
        如果同意，就直接按照已经解析好的日志List进行处理
        不同意，就直接split，根据index取字段
    3. 日志的每一行的时间字段是否是有序的？
        如果无序，就按照时间从小到大排序
'''

class UnionFind:
    def __init__(self, n:int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.set_count = n
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y:int) -> bool:
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return False
        if self.size[rootx] < self.size[rooty]:
            rootx, rooty = rooty, rootx
        self.parent[rooty] = rootx
        self.size[rootx] += self.size[rooty]
        self.set_count -= 1
        return True

def parse_logs(logs: list[str]):
    paresd = []
    for log in logs:
        parts = log.split()
        log = [parts[0], parts[1], parts[3]]
        paresd.append(log)
    return paresd.sort(key=lambda x: x[0])

def getEarliestTime(users: list[str], logs: list[str]) -> int:
    '''
    1. 解析 + 排序日志
    2. 初始化 UF（每人一个集合）
    3. 建 user -> index 映射
    4. 按时间遍历每条日志：
         a) 找到双方 index
         b) 如果 union 真的合并了两个不同集合
             i) 集合数减一，如果现在集合数 == 1 → 返回当前时间
    5. 遍历完还没 return → 返回 None
    '''

    if not users:
        return None
    if len(users) == 1:
        return None
    parsed_logs = parse_logs(logs)
    m = len(users)
    user_to_index = {user: i for i, user in enumerate(users)}
    uf = UnionFind(m)

    for timestamp, user1, user2 in parse_logs:
        if user1 not in user_to_index or user2 not in user_to_index:
            continue
        u = user_to_index[user1]
        v = user_to_index[user2]

        merged = uf.union(u, v)
        if merged and uf.set_count == 1:
            return timestamp
    return None