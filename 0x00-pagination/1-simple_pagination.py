#!/usr/bin/env python3
"""Task 1: Simple pagination.
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Calculate the start and end index for pagination."""
    if page == 1:
        return (0, page_size)
    else:
        indx = ((page - 1) * page_size)
        return (indx, indx + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of data from the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data = self.dataset()
        idex = index_range(page, page_size)
        if idex[0] > len(data):
            return []
        return data[idex[0]:idex[1]]
