#!/usr/bin/env python3

'''Task 0: Basic dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class `BasicCache` that inherits from `BaseCaching`
       and is a caching system
    '''
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys() and key is not None:
            return self.cache_data[key]
