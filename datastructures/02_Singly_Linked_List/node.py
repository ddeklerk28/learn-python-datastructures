class Node:
    def __init__(self, data, nxt: Node | None = None):
        self._data = data
        self._nxt = nxt

    @property
    def nxt(self):
        return self._nxt