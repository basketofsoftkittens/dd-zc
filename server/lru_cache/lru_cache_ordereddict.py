from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache.get(key)

    def set(self, key, val):
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = val


lru_cache = LRUCache(3)
