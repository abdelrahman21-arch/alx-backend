#!/usr/bin/env python3
""" lifo class
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
        - derived class of BaseCaching
        - implements lifo caching
    """
    def __init__(self):
        super().__init__() # init parent class
        self.key_indexes = []

    def put(self, key, item):
        """

        :param key:  key
        :param item: value
        :return: new dict according to fifo
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    del self.cache_data[self.key_indexes[self.MAX_ITEMS - 1]]
                    item_discarded = self.key_indexes.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """

        :param key: key
        :return: item
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
