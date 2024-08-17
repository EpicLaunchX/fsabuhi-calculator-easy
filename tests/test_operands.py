from src.pytemplate.domain.models import Operands


def declare_instance():
    operands = Operands()
    assert isinstance(operands, Operands)


def test_variable_types():
    operands = Operands()
    operands.first_operand = 1
    operands.second_operand = 2
    assert isinstance(operands.first_operand, int)
    assert isinstance(operands.second_operand, int)
