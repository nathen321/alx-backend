#!/usr/bin/env python3

'''Task 1: Basic dictionary
'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class `BasicCache` that inherits from `BaseCaching`
       and is a caching system
    '''
    def __init__(self):
        """ initialize
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print("DISCARD: {0}".format(first_key))

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys() and key is not None:
            return self.cache_data[key]
