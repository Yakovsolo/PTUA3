"""Task Nr.2:

Create a class called MyQueue that has __bool__, __repr__ and __len__ methods defined.

The __bool__ method should return True if the queue has any items and False if it is empty.
The __repr__ method should return a string in the format MyQueue(items) where items is the list of items in the queue.
The __len__ method should return the number of items in the queue."""

from typing import List, Optional


class MyQueue:
    def __init__(self, items: List[Optional[int]]) -> None:
        self.items = items

    def __bool__(self) -> bool:
        if len(self.items) == 0:
            return False
        return True

    def __repr__(self) -> str:
        return f"MyQueue({self.items})"

    def __len__(self) -> int:
        return len(self.items)


my_queue = MyQueue(items=[1, 2, 3, 4, 5])

print(len(my_queue))
print(repr(my_queue))
print(bool(my_queue))

# Output:
# 5
# MyQueue([1, 2, 3, 4, 5])
# True
