from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int


def operands_factory(first_operand: int, second_operand: int) -> Operands:
    operands_instance = Operands(first_operand, second_operand)
    return operands_instance
