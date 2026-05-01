class Node:
    def __init__(self, data, node: Node):
        self._data = data
        self._next = node