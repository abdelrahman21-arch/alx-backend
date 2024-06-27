#!/usr/bin/env python3
""" lfu class
"""

from base_caching import BaseCaching

from collections import defaultdict

class LFUCache(BaseCaching):
    """


        - derived class of BaseCaching
        - implements lfu caching
    """
    def __init__(self):
        super().__init__() # init parent class
        self.frequency = defaultdict(int)
        self.min_frequency = 0

    def put(self, key, item):
        """

        :param key:  key
        :param item: value
        :return: new dict according to lfu
        """

        if not key or not item:
            return

        if key in self.cache_data:


            # update item and freq
            self.cache_data[key] = item
            # increase freq
            freq = self.frequency[key]
            self.frequency[key] += 1

            # check min freq
            if freq == self.min_frequency and not any(f == self.min_frequency for f in self.frequency.values()):
                self.min_frequency += 1

        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Find the least frequently used key(s)
                lfu_keys = [k for k, v in self.frequency.items() if v == self.min_frequency]

                if lfu_keys:
                    lfu_key = lfu_keys[0]
                    print("DISCARD:", lfu_key)
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]

                    # Update the minimum frequency if necessary
                    if not any(f == self.min_frequency for f in self.frequency.values()):
                        self.min_frequency += 1

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.min_frequency = 1

    def get(self, key):
        """

        :param key: key
        :return: item
        """
        if key not in self.cache_data:
            return None

        # Increase the frequency of the key
        value = self.cache_data[key]
        freq = self.frequency[key]
        self.frequency[key] += 1

        # Update the minimum frequency if necessary
        if freq == self.min_frequency and not any(f == self.min_frequency for f in self.frequency.values()):
            self.min_frequency += 1

        return value

