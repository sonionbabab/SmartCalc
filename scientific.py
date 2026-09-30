import math


class ScientificCalculator:
    def calculate(self, operation, value):
        if operation == "sqrt":
            if value < 0:
                raise ValueError("Square root requires a non-negative number.")
            return math.sqrt(value)

        elif operation == "sin":
            return math.sin(math.radians(value))

        elif operation == "cos":
            return math.cos(math.radians(value))

        elif operation == "tan":
            return math.tan(math.radians(value))

        elif operation == "log":
            if value <= 0:
                raise ValueError("Logarithm requires a positive number.")
            return math.log10(value)

        elif operation == "ln":
            if value <= 0:
                raise ValueError("Natural logarithm requires a positive number.")
            return math.log(value)

        elif operation == "factorial":
            if value < 0 or not value.is_integer():
                raise ValueError("Factorial requires a non-negative integer.")
            return math.factorial(int(value))

        raise ValueError("Unsupported scientific operation.")
