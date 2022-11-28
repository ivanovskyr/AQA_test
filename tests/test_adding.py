import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2
    def test_adding_unsuccess(self):
        assert self.calc.adding(1, 1) == 3
    def test_zero_divizion(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)
    def teardown(self):
        print("Выполнение метода Teardown")

