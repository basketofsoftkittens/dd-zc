from typing import Optional


class ListNode:
    def __init__(self, key, val, type="node"):
        self.key = key
        self.val = val
        self.type = type
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode(key="head", val="H", type="helper_node")
        self.tail = ListNode(key="tail", val="T", type="helper_node")
        self.head.next = self.tail
        self.tail.prev = self.head

    def _list_remove(self, node: ListNode) -> None:
        """Remove node from the linked list"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _list_append(self, node: ListNode) -> None:
        """Attach the node before the tail helper node in the linked list"""
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def _list_pop_left(self) -> ListNode:
        """Remove and return the most left (a.k.a. least recently used) element in the linked list."""
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        return self.head.next

    def get(self, key: int) -> Optional[int]:
        if key not in self.cache:
            return None
        node = self.cache[key]
        self._list_remove(node)
        self._list_append(node)
        return node.val

    def set(self, key: int, val: int) -> None:
        if self.cache.get(key):
            self._list_remove(self.cache.get(key))
            del self.cache[key]

        if len(self.cache) >= self.capacity:
            del self.cache[self.head.next.key]
            self._list_pop_left()

        new_node = ListNode(key=key, val=val)
        self._list_append(new_node)
        self.cache[key] = new_node


lru_cache = LRUCache(3)
