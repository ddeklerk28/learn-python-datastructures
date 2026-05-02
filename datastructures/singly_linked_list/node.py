class Node:
    def __init__(self, value, nxt: Node | None = None):
        self._value = value
        self._nxt = nxt

    @property
    def nxt(self):
        return self._nxt

    @property
    def value(self):
        return self._value