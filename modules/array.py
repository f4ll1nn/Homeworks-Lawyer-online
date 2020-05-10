""" Module of realization array data structure """
import ctypes


class Array:
    """ Class of arrays """

    def __init__(self, size):
        """ Creates array"""
        assert size > 0, "Array size must be > 0"
        self._size = size
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        self.clear(None)

    def __len__(self):
        """ Returns size """
        return self._size

    def __getitem__(self, index):
        """ Gets value of item by index """
        assert 0 < index < len(self), "Array subscript out of range"
        return self._elements[index]

    def __setitem__(self, index, value):
        """ sets value in item by index """
        assert 0 < index < len(self), "Array subscript out of range"
        self._elements[index] = value

    def clear(self, value):
        """ Del all elements """
        for i in range(len(self)):
            self._elements[i] = value

    def __str__(self):
        """ Returns list as sting """
        string_list = "["
        for element in self._elements:
            string_list += str(element) + ", "
        string_list = string_list[:-2] + "]"
        return string_list

    def __iter__(self):
        """ Realize opportunity to iterates """
        return _ArrayIterator(self._elements)


class _ArrayIterator:
    """ Class of iteration """

    def __init__(self, the_array):
        """ Creates iteration """
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        """ Iteration """
        return self

    def __next__(self):
        """ Returns next """
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        raise StopIteration
