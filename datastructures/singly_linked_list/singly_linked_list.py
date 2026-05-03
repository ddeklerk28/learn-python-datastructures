from .node import Node

class SinglyLinkedList:
    ### Dunder methods ###
    def __init__(self):
        self._head: Node | None = None
        self._tail: Node | None = None
        self._size: int = 0

    def __len__(self) -> int:
        """Return the number of elements. O(1)"""
        return self._size

    def __contains__(self, item) -> bool:
        """Support `x in list` syntax. O(n)."""

    def __iter__(self):
        """Support iteration via for loops. O(n)."""
        curr = self._head
        while curr is not None:
            yield curr
            curr = curr.nxt

    def __repr__(self) -> str:
        """Human-readable representation for debugging."""

    ### Help Methods ###
    def _check_index(self, index: int):
        """Normalise and validate an index, supporting negative indexing."""
        if index < 0:
            index = self._size + index
        if not (0 <= index < self._size):
            err = f"index {index} out of range for size {self._size}"
            raise IndexError(err)
        return index

    ### Main API Methods ###
    def prepend(self, value) -> None:
        """Insert item at the head. O(1)."""
        if self.is_empty():
            self._head = Node(value, None)
        else:
            temp = Node(value, self._head)
            self._head = temp
        self._size += 1

    def append(self, value) -> None:
        """Insert item at the tail. O(n)."""
        if self.is_empty():
            self._head = Node(value, None)
        else:
            curr = self._head
            while curr.nxt is not None:
                curr = curr.nxt
            curr.nxt = Node(value, None)
        self._size += 1

    def insert(self, index: int, value) -> None:
        """Insert item before the element currently at index. O(n)."""
        index = self._check_index(index)
        if index == 0:
            self.prepend(value)
        else:
            next_index = 1
            curr = self._head
            while next_index is not index:
                curr = curr.nxt
                next_index += 1
            curr.nxt = Node(value, curr.nxt)
        self._size += 1


    def delete_at(self, index: int) -> any:
        """Remove and return element at index. O(n)."""

    def delete_value(self, item) -> bool:
        """Remove first occurrence of item. Return True if found, False if not. O(n)."""

    def search(self, item) -> int:
        """Return index of first occurrence of item, or -1 if not found. O(n)."""

    def get(self, index: int) -> any:
        """Return element at index without removing it. O(n)."""

    def reverse(self) -> None:
        """Reverse the list in place. O(n)."""

    def is_empty(self) -> bool:
        """Return True if the list has no elements. O(1)."""
        return self._head is None

    def print_list(self):
        temp_str = ""
        for item in self:
            temp_str += f"({item.value})->"
        print(f"{temp_str}{"None" if self._size else "empty"}")
