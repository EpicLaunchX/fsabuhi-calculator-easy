class Calculator:
    def add(self, operands) -> int:
        ans = operands.first_operand + operands.second_operand
        return ans

    def subtract(self, operands) -> int:
        ans = operands.first_operand - operands.second_operand
        return ans

    def multiply(self, operands) -> int:
        ans = operands.first_operand * operands.second_operand
        return ans

    def divide(self, operands) -> int:
        ans = operands.first_operand / operands.second_operand
        return ans
