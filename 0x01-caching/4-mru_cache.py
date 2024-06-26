#!/usr/bin/env python3
""" mru class
"""

from base_caching import BaseCaching

from collections import OrderedDict

class LRUCache(BaseCaching):
    """


        - derived class of BaseCaching
        - implements lru caching
    """
    def __init__(self):
        super().__init__() # init parent class
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """

        :param key:  key
        :param item: value
        :return: new dict according to lru
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]

                else:
                    mru_key, _ = self.cache_data.popitem(True) # `_` is used to ignore the value part of the item
                    print("DISCARD:", mru_key)

            self.cache_data[key] = item

    def get(self, key):
        """

        :param key: key
        :return: item
        """
        if key in self.cache_data:
            # Move the key to the end to mark it as recently used
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
