from src.pytemplate.domain.models import Operands, operands_factory


def test_return_type():
    first = 1
    second = 2

    result = operands_factory(first_operand=first, second_operand=second)
    assert isinstance(result, Operands)
