class Calculator:
    def calculate(self, a, operation, b):
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return a / b
        elif operation == "%":
            if b == 0:
                raise ZeroDivisionError("Cannot use zero as divisor.")
            return a % b
        elif operation == "**":
            return a ** b

        raise ValueError("Unsupported operation.")
