'''
参考LeetCode 380

'''


import random

class RandomizedSet:

    def __init__(self):
        self.mp = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        self.arr.append(val)
        self.mp[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        self.mp[self.arr[-1]] = self.mp[val]
        self.arr[self.mp[val]], self.arr[-1] = self.arr[-1], self.arr[self.mp[val]]
        del self.mp[val]
        self.arr.pop()
        return True 

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()