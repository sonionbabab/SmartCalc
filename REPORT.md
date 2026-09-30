# Python Scientific Calculator - Project Report

## 1. Introduction
The Python Scientific Calculator is a modular command-line application designed to perform basic and scientific mathematical calculations. The project demonstrates Python programming concepts through separate modules, validation, exception handling, and testing.

## 2. Problem Statement
A small calculator can be used as a practical application for demonstrating programming fundamentals while keeping the user interaction simple and understandable.

## 3. Objectives
- Implement arithmetic operations.
- Implement common scientific functions.
- Maintain calculation history.
- Validate user input.
- Handle calculation errors safely.
- Demonstrate modular Python programming.
- Test important calculator functions.

## 4. Functional Requirements
### FR1 - Basic Calculation
The system shall perform addition, subtraction, multiplication, division, modulo and power.

### FR2 - Scientific Calculation
The system shall support square root, trigonometric functions, logarithms and factorial.

### FR3 - History
The system shall store and display previous calculations during the current session.

### FR4 - Validation
The system shall reject invalid numeric input and unsupported operations.

### FR5 - Testing
The project shall include automated unit tests for core operations.

## 5. Non-Functional Requirements
- **Usability:** Menu-based interaction should be simple and understandable.
- **Reliability:** Invalid input and division by zero should be handled without crashing.
- **Maintainability:** Features are separated into Python modules.
- **Performance:** Calculations should complete immediately for normal user inputs.
- **Resource Efficiency:** The application uses lightweight standard Python modules.

## 6. System Architecture
The application uses a modular architecture:
User -> main.py -> Calculator / ScientificCalculator / History / Validator -> Output

## 7. Workflow
1. Start application.
2. Display main menu.
3. User selects a module.
4. User provides input.
5. Input is validated.
6. Calculation is performed.
7. Result is displayed.
8. Calculation is stored in history when applicable.
9. User returns to the main menu or exits.

## 8. Design Decisions
Python's standard library was selected to keep the project lightweight and easy to execute. Separate modules were used to improve maintainability and demonstrate modular programming.

## 9. Implementation Details
`main.py` manages user interaction. `calculator.py` performs basic arithmetic. `scientific.py` handles scientific functions. `history.py` stores session calculations. `validator.py` validates numeric input. `test_calculator.py` verifies core functionality.

## 10. Testing Approach
Unit tests are implemented using Python's `unittest` framework. Tests cover arithmetic operations, power, square root and division-by-zero handling.

## 11. Challenges Faced
- Handling invalid numeric input.
- Preventing division by zero.
- Validating mathematical restrictions such as logarithms and square roots.
- Keeping the project modular while maintaining a simple interface.

## 12. Learnings
The project demonstrates modular programming, classes, functions, exception handling, input validation, testing, and basic software organization.

## 13. Future Enhancements
- Graphical user interface.
- Persistent history using SQLite.
- Expression parsing.
- More advanced scientific functions.
- Exporting calculation history.

## 14. References
- Python Standard Library documentation
- Python `math` module documentation
- Python `unittest` documentation
