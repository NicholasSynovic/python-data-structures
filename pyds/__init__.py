from collections import OrderedDict
from typing import Any, Iterable


class OrderedSet:
    def __init__(self) -> None:
        self.set: OrderedDict = OrderedDict()

    def add(self, value: Any) -> None:
        self.set[value] = None

    def extend(self, _iterable: Iterable) -> None:
        foo: Any
        for foo in _iterable:
            self.add(value=foo)

    def __contains__(self, item):
        return item in self.set

    def __len__(self):
        return len(self.set)

    def __iter__(self):
        return iter(self.set.keys())

    def __repr__(self):
        return f"OrderedSet({list(self.set.keys())})"
