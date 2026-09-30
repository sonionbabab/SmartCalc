from calculator import Calculator
from scientific import ScientificCalculator
from history import History
from validator import safe_float


def main():
    calc = Calculator()
    sci = ScientificCalculator()
    history = History()

    while True:
        print("\n=== PYTHON CALCULATOR ===")
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        print("3. Calculation History")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                a = safe_float(input("Enter first number: "))
                op = input("Enter operation (+, -, *, /, %, **): ").strip()
                b = safe_float(input("Enter second number: "))

                result = calc.calculate(a, op, b)
                print("Result:", result)
                history.add(f"{a} {op} {b}", result)

            except (ValueError, ZeroDivisionError) as e:
                print("Error:", e)

        elif choice == "2":
            print("\nScientific operations: sqrt, sin, cos, tan, log, ln, factorial")
            op = input("Enter operation: ").strip().lower()

            try:
                value = safe_float(input("Enter value: "))
                result = sci.calculate(op, value)
                print("Result:", result)
                history.add(f"{op}({value})", result)

            except (ValueError, ZeroDivisionError) as e:
                print("Error:", e)

        elif choice == "3":
            history.show()

        elif choice == "4":
            print("Thank you for using Python Calculator.")
            break

        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()
