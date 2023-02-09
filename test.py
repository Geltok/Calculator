import pytest

from App.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,1,1) == 2

    def test_devision_success(self):
        assert self.calc.division(self,4,2) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(self,5,6) == 30

    def test_substraction_success(self):
        assert self.calc.subtraction(self,2,2) == 0
