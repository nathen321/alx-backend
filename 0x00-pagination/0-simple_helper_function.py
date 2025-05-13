#!/usr/bin/env python3
""" 0-simple_helper_function module """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end index for pagination."""
    if page == 1:
        return (0, page_size)
    else:
        indx = ((page - 1) * page_size)
        return (indx, indx + page_size)
