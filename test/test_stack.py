import unittest
from src.stack import Stack, Node
from src.exceptions import (StackOverflowException,
                            StackUnderflowException)


s = Stack(10)
n = Node(10)


class NodeTest(unittest.TestCase):
    def test_init(self):
        n = Node(10)
        n.value == 10
        n.next = None

    def test_value_setter(self):
        with self.assertRaises(ValueError):
            n.value = "A"

    def test_next_setter(self):
        with self.assertRaises(ValueError):
            n.next = "A"

    def test_str(self):
        self.assertIsInstance(n.__str__(), str)


class StackTest(unittest.TestCase):
    def test_init(self):
        assert s.max_size == 10
        assert s.size == 0
        assert s.top == None

    def test_push(self):
        s = Stack(10)
        s.push(10)
        assert s.top.value == 10
        assert s.top.next == None
        s.push(20)
        assert s.top.value == 20
        assert s.top.next.value == 10

    def test_pop(self):
        s = Stack(10)
        s.push(20)
        s.push(10)
        value = s.pop()
        assert value == 10
        assert s.top.value == 20
        assert s.top.next == None
        s.pop()
        assert s.top == None

    def test_size(self):
        s = Stack(10)
        s.push(10)
        s.push(20)
        assert s.size == 2
        s.pop()
        s.pop()
        assert s.size == 0

    def test_exceptions(self):
        with self.assertRaises(StackUnderflowException):
            s = Stack(1)

            s.pop()
        with self.assertRaises(StackOverflowException):
            s = Stack(1)

            s.push(10)
            s.push(20)

    def test_empty(self):
        s = Stack(10)
        assert s.empty()

    def test_stack_exceptions(self):
        with self.assertRaises(ValueError):
            s = Stack("A")

        with self.assertRaises(ValueError):
            s = Stack(10)
            s.size = "A"

        with self.assertRaises(ValueError):
            s = Stack(10)
            s.top = "A"
