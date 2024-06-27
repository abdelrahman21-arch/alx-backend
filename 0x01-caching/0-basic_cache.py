#!/usr/bin/python3
""" BaseCaching class
"""


from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
       - derived class of BaseCaching
       - implements put and get methods
    """
    def __init__(self):
        """ initialize
        """
        super().__init__() # call the base class initializer

    def put(self, key, item):
        """

        :param key: key to the dict
        :param item:  value
        :return: added dict
        """


        if key is None or item is None:
            return None
        self.cache_data[key] = item

    def get(self, key):
        """

        :param key: key to the dict
        :param item:  value
        :return: returned item
        """
        return self.cache_data.get(key, None)
