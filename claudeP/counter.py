class Counter:
    def __init__(self):
        self._count = 0
    def count(self):
        return self._count
    def increment(self):
        self._count += 1
    def decrement(self):
        self._count -= 1