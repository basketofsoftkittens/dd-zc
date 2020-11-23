import unittest

from lru_cache.lru_cache_ordereddict import LRUCache


class LRUCacheTestCase(unittest.TestCase):
    def setUp(self):
        self.lc = LRUCache(3)
        self.assertEqual(self.lc.cache, {})

    def test_flow(self):
        self.lc.set("jack", 11)
        self.lc.set("queen", 12)
        self.lc.set("king", 13)
        self.assertEqual(self.lc.cache, {"jack": 11, "queen": 12, "king": 13})
        self.lc.set("ace", 14)
        self.assertIsNone(self.lc.get("jack"))
        self.assertEqual(self.lc.cache, {"queen": 12, "king": 13, "ace": 14})
        self.assertEqual(self.lc.get("king"), 13)
        self.assertEqual(self.lc.cache, {"queen": 12, "ace": 14, "king": 13})
