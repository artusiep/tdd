import random
from copy import copy

from element import Element


class RandomList:
    def __init__(self, n):
        self._container = [Element(x) for x in random.sample(range(0, 100), n)]

    def __len__(self):
        return len(self._container)

    def __iter__(self):
        return iter(self._container)

    def __getitem__(self, element):
        return self._container[element]

    def __str__(self):
        return str([str(x) for x in self._container])

    def sort_list(self):
        # We start from 1 since the first element is trivially sorted
        for index in range(1, len(self._container)):
            current_value = self._container[index]
            current_position = index

            # As long as we haven't reached the beginning and there is an element
            # in our sorted self._container larger than the one we're trying to insert - move
            # that element to the right
            while current_position > 0 and self._container[current_position - 1] > current_value:
                self._container[current_position] = self._container[current_position - 1]
                current_position = current_position - 1

            # We have either reached the beginning of the self._container or we have found
            # an element of the sorted self._container that is smaller than the element
            # we're trying to insert at index current_position - 1.
            # Either way - we insert the element at current_position
            self._container[current_position] = current_value
        result = copy(self)
        result._container = self._container
        return result
