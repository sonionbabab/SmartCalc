# Design Diagrams

## 1. Use Case Diagram

```text
                 +---------------------------+
                 |   Python Calculator       |
                 |                           |
User ----------> | Perform Basic Calculation |
  |              | Perform Scientific Calc.  |
  |              | View Calculation History  |
  |              | Validate Input            |
  |              | Exit Application          |
                 +---------------------------+
```

## 2. Workflow Diagram

```text
[Start]
   |
[Main Menu]
   |
   +--> [Basic Calculator] ------+
   |                             |
   +--> [Scientific Calculator] -+--> [Validate Input]
   |                                      |
   +--> [View History]                    v
   |                               [Perform Calculation]
   |                                      |
   |                               [Display Result]
   |                                      |
   +--------------------------------------+
                                          |
                                   [Return to Menu]
                                          |
                                       [Exit?]
                                      /                                           Yes        No
                                    |          |
                                  [End] <--- [Menu]
```

## 3. Class Diagram

```text
+----------------------+
|      Calculator      |
+----------------------+
| + calculate()        |
+----------------------+

+------------------------------+
|   ScientificCalculator       |
+------------------------------+
| + calculate()                |
+------------------------------+

+----------------------+
|       History        |
+----------------------+
| records              |
| + add()              |
| + show()             |
| + clear()            |
+----------------------+

+----------------------+
|       Validator      |
+----------------------+
| + safe_float()       |
+----------------------+

              ^
              |
           main.py
```

## 4. Sequence Diagram

```text
User -> main.py: Select Basic Calculator
main.py -> Validator: Validate input
Validator --> main.py: Valid numbers
main.py -> Calculator: calculate(a, op, b)
Calculator --> main.py: Result
main.py -> History: add(expression, result)
History --> main.py: Stored
main.py --> User: Display result
```

## 5. Component / Architecture Diagram

```text
+-------------------+
|       User        |
+---------+---------+
          |
          v
+-------------------+
|      main.py      |
+----+----+----+----+
     |    |    |
     v    v    v
 Calculator Scientific History
     |    |    |
     +----+----+
          |
       Validator
          |
        Output
```
