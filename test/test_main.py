import unittest
from main import calculate_span


class NodeTest(unittest.TestCase):
    def test_calculate_span_exceptions(self):
        with self.assertRaises(ValueError):
            calculate_span(stock_price="a")
        with self.assertRaises(ValueError):
            calculate_span(stock_price=["a"])
        with self.assertRaises(ValueError):
            calculate_span(stock_price=[])

    def test_calculate_span(self):
        assert calculate_span([100, 80, 60, 70, 60, 75, 85]) == [
            1, 1, 1, 2, 1, 4, 6]
