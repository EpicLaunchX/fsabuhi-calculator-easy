from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def main(first_operand: int, second_operand: int, action):
    calculator = Calculator()
    operands = operands_factory(first_operand, second_operand)
    if action == "add":
        return calculator.add(operands)

    elif action == "subtract":
        return calculator.subtract(operands)
    elif action == "multiply":
        return calculator.multiply(operands)
    elif action == "divide":
        return calculator.divide(operands)
