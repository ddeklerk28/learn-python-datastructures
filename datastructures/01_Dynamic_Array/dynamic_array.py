import ctypes

class DynamicArray:
    """A dynamic array built on a raw C array via ctypes.

    Mimics the core behaviour of Python's list — O(1) amortised append,
    O(1) index access, O(n) insert/delete.

    Growth strategy  : double capacity when full
    Shrink strategy  : halve capacity when size drops to 25% of capacity
    Minimum capacity : 1 (never shrinks to zero)"""
    growth_factor = 2
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._array = self._make_array(1)

    ### Helper Methods ###
    def _make_array(self, capacity):
        """Allocate a raw C array of `capacity` Python object pointers."""
        return (ctypes.py_object * capacity)()

    def _resize(self, new_capacity: int):
        """Allocate a new backing array of new_capacity and copy elements across.
        O(n) — called rarely enough that append is O(1) amortised."""
        new_array = self._make_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def _check_index(self, index: int):
        """Normalise and validate an index, supporting negative indexing."""
        if index < 0:
            index = self._size + index
        if not (0 <= index < self._size):
            raise IndexError(f"index {index} out of range for size {self._size}")
        return index

    #### Core Interface ###
    def append(self, item):
        """Add item to the end.
        O(1) amortised — O(n) on resize, but resize doubles capacity so
        it happens logarithmically often."""
        if self._size == self._capacity:
            self._resize(self._capacity * DynamicArray.growth_factor)

        self._array[self._size] = item
        self._size += 1

    def insert(self, index: int, item):
        pass

    def delete(self, index: int):
        pass

    def __getitem__(self, index):
        index = self._check_index(index)
        return self._array[index]

    def __setitem__(self, index, item):
        index = self._check_index(index)
        self._array[index] = item

    def __len__(self):
        return self._size

    def __repr__(self):
        elements_str = ""
        for i in range(self._size):
            elements_str += f"{self._array[i]} "
        elements_str = ", ".join(elements_str.split(" ")[:-1])

        return f"DynamicArray([{elements_str}]) size={self._size} capacity={self._capacity}"

