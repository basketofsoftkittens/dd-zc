import unittest

from lru_cache.lru_cache import LRUCache


class LRUCacheTestCase(unittest.TestCase):
    def test_flow_1(self):
        lc = LRUCache(3)
        self.assertEqual(lc.cache, {})

        lc.set("jack", 11)
        lc.set("queen", 12)
        lc.set("king", 13)
        self.assertEqual(11, lc.cache["jack"].val)
        self.assertEqual(12, lc.cache["queen"].val)
        self.assertEqual(13, lc.cache["king"].val)
        self.assertEqual(3, len(lc.cache))
        self.assertEqual("jack", lc.head.next.key)
        self.assertEqual("king", lc.tail.prev.key)

        lc.set("ace", 14)
        self.assertEqual(3, len(lc.cache))
        self.assertNotIn("jack", lc.cache)
        self.assertEqual(12, lc.cache["queen"].val)
        self.assertEqual(13, lc.cache["king"].val)
        self.assertEqual(14, lc.cache["ace"].val)
        self.assertEqual("queen", lc.head.next.key)
        self.assertEqual("ace", lc.tail.prev.key)

        lc.get("king")
        self.assertEqual("queen", lc.head.next.key)
        self.assertEqual("king", lc.tail.prev.key)

    def test_flow_2(self):
        lc = LRUCache(2)
        self.assertEqual(lc.cache, {})
        self.assertIsNone(lc.get(2))
        lc.set(2, 6)
        self.assertIsNone(lc.get(1))
        lc.set(1, 5)
        lc.set(1, 2)
        self.assertEqual(2, lc.get(1))
        self.assertEqual(6, lc.get(2))
