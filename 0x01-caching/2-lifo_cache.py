#!/usr/bin/python3
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
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            first_key = self.key_indexes.pop(-1) # get first key
            print(f"DISCARD:{first_key}\n")  # pop first item
            del self.cache_data[first_key]  # remove first item

        self.cache_data[key] = item
        self.key_indexes.append(key)

    def get(self, key):
        """

        :param key: key
        :return: item
        """
        if key is None:
            return None

        return self.cache_data.get(key, None)