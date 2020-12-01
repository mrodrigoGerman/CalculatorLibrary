"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)
        assert 7 == calculator.add(1, 4)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
