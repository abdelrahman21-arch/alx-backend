#!/usr/bin/python3
""" fifo class
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
        - derived class of BaseCaching
        - implements fifo chaching
    """
    def __init__(self):
        super().__init__() # init parent class

    def put(self, key, item):
        """

        :param key:  key
        :param item: value
        :return: new dict according to fifo
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            first_key = next(iter(self.cache_data)) # get first key
            print(f"DISCARD:{first_key}\n")  # pop first item
            del self.cache_data[first_key]  # remove first item

        self.cache_data[key] = item

    def get(self, key):
        """

        :param key: key
        :return: item
        """
        if key is None:
            return None

        return self.cache_data.get(key, None)