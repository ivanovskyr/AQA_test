import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()
    def test_multiply(self):
        assert self.calc.multiply(3, 2) == 6
    def test_division(self):
        assert self.calc.division(4, 2) == 2
    def test_substraction(self):
        assert self.calc.subtraction(5, 2) == 3
    def test_adding(self):
        assert self.calc.adding(6, 2) == 8
    def teardown(self):
        print("Выполнение тестов произведено")