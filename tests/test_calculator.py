from src.pytemplate.domain.models import Operands, operands_factory
from src.pytemplate.service.calculator import Calculator

operands = operands_factory(1, 2)


def test_add():
    calculator = Calculator()
    assert calculator.add(operands) == 3


def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(operands) == -1


def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(operands) == 2


def test_divide():
    calculator = Calculator()
    assert calculator.divide(operands) == 0.5
