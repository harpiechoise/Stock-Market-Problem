from src.exceptions import (StackUnderflowException,
                            StackOverflowException)


class NodeBase:
    pass


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            self._value = value
        else:
            raise ValueError(f"Value {value} isn't a int")

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        if isinstance(value, Node) or isinstance(value, type(None)):
            self._next = value
        else:
            raise ValueError(f"Value {value} isn't a node isntance")


class Stack:
    def __init__(self, max_size: int):
        self.max_size: int = max_size
        self.size: int = 0
        self.top: int = None

    @property
    def max_size(self):
        return self._max_size

    @property
    def size(self):
        return self._size

    @property
    def top(self):
        return self._top

    @max_size.setter
    def max_size(self, value):
        if isinstance(value, int):
            self._max_size = value
        else:
            raise ValueError("Max size must be Integer")

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            raise ValueError("Size must be Integer")

    @top.setter
    def top(self, value):
        if isinstance(value, Node) or isinstance(value, type(None)):
            self._top = value
        else:
            raise ValueError("Top must be a node")

    def push(self, value: int):
        if self.size >= self.max_size:
            raise StackOverflowException("The Stack is Full")

        if self.top == None:
            self.top = Node(value)
        else:
            top = self.top
            new_value = Node(value)
            new_value.next = top
            self.top = new_value
        self.size += 1

    def pop(self) -> int:
        if self.top == None:
            raise StackUnderflowException("The Stack is empty")
        value = self.top
        self.top = value.next
        self.size -= 1
        return value.value

    def empty(self) -> bool:
        return self.size == 0
