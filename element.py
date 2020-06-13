class Element:
    def __init__(self, value):
        self._value = value

    def __eq__(self, other):
        return self._value == other._value

    def __gt__(self, other):
        return self._value > other._value

    def __ge__(self, other):
        return self._value >= other._value

    def __str__(self):
        return str(self._value)