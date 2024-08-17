from src.pytemplate.domain.models import Operands


def declare_instance():
    operands = Operands()
    assert isinstance(operands, Operands)


def test_variable_types():
    operands = Operands(1, 2)
    assert isinstance(operands.first_operand, int)
    assert isinstance(operands.second_operand, int)
