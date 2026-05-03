class Node:
    def __init__(self, value, nxt: Node | None = None):
        self._value = value
        self._nxt = nxt

    @property
    def nxt(self):
        return self._nxt

    @nxt.setter
    def nxt(self, other: Node | None):
        self._nxt = other

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value