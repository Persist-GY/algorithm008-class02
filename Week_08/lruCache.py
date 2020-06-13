import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()


    def get(self, key: int) -> int:
        if key in self.dic:
            # 存在key
            v = self.dic.pop(key)
            self.dic[key] = v
            return v
        else:
            return -1
        


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            # key存在字典中 删除
            self.dic.pop(key)
        else:
            if self.capacity == 0:
                # 没有容量了 删除最近最少使用的
                self.dic.popitem(last=False)
            else:
                # 容量减1
                self.capacity -= 1
        self.dic[key] = value