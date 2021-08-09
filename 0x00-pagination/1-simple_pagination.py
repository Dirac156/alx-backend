#!/usr/bin/env python3
""" """


import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """ get items in a page """
        assert page > 0 and type(page) == int
        assert page_size > 0 and type(page_size) == int

        index_tuple = index_range(page = page, page_size = page_size)
        start = index_tuple[0]

        csv_file = self.dataset()

        list_result = []

        if len(csv_file) < index_tuple[1]:
            return list_result

        while start != index_tuple[1]:
            list_result.append(csv_file[start])
            start += 1

        return list_result
