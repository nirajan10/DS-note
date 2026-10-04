# Unit II Exam Questions: Python Programming Basics and Operators

[Back to the Unit II notes](../unit-02-basics.md)

## Past Paper Questions

**Q1.** Define Python Programming? What are its features and applications in Business?

*Source: Python Programming Internal Exam (CCT), 2025, question 1. Listed under BCSIT on bcsitcenter.com; the page names no university or college. Marks not shown. [Page](https://bcsitcenter.com/material/python-programming-internal-exam-cct/).*

??? success "Model Answer (Written for These Notes)"

    **Python** is a free, high-level programming language. High-level means its code reads close to everyday English.

    **Features:**

    - Simple and easy to read, so it is quick to learn.
    - Interpreted: Python runs the program line by line, with no separate compile step.
    - Free and open source.
    - Has a very large collection of ready-made libraries, such as Pandas and NumPy.
    - Portable: the same program runs on Windows, macOS and Linux.

    **Applications in business:**

    - Analysing sales and customer data with Pandas.
    - Drawing charts and dashboards for managers.
    - Predicting demand or customer behaviour with machine learning.
    - Automating repeated office work, such as reading Excel files and preparing reports.

**Q2.** Define Variable and Constant in Python.

*Source: Python Programming Internal Exam (CCT), 2025, question 2. Marks not shown. [Page](https://bcsitcenter.com/material/python-programming-internal-exam-cct/).*

??? success "Model Answer (Written for These Notes)"

    A **variable** is a name that refers to a value stored in memory. Its value can change while the program runs.

    A **constant** is a value that should never change. Python has no built-in constants. By convention, programmers write the name in capital letters to tell others "do not change this".

    ```python
    marks = 70
    marks = 82
    PASS_MARKS = 45
    print(marks, PASS_MARKS)
    ```

    ```{ .text .output title="Output" }
    82 45
    ```

    `marks` changed from 70 to 82. `PASS_MARKS` stays 45 only because we agree not to change it.

## Practice Questions (Not from Past Papers)

**P1. (Short answer)** Who created Python? When was it first released, why is it called Python, and when did Python 3 arrive?

??? success "Model Answer"

    Python was created by Guido van Rossum. He began writing it in December 1989 and released it to the public in February 1991. It is named after the British comedy show *Monty Python's Flying Circus*, of which he was a fan. Python 3.0 was released on 3 December 2008.

**P2. (Short answer)** State any four features of Python.

??? success "Model Answer"

    - Easy to read and learn: the code looks close to English.
    - Interpreted: the interpreter runs the code line by line, with no separate step to build a program.
    - Free: it can be downloaded and used at no cost.
    - Large collection of libraries: the standard library and many add-on libraries.
    - Portable: the same program runs on Windows, macOS and Linux.

**P3. (Short answer)** What is an IDE? Name two examples.

??? success "Model Answer"

    An IDE (Integrated Development Environment) is one program in which you write, run and fix your code. Examples: IDLE, PyCharm, VS Code. Jupyter Notebook is also used in the same way, although strictly it is a notebook tool.

**P4. (Short answer)** What is a variable? Write three rules for naming a variable.

??? success "Model Answer"

    A variable is a name that stores a value, created with the `=` operator.

    - Use only letters, digits and underscores, with no spaces.
    - Do not start the name with a digit.
    - Do not use a keyword such as `if` or `class`.
    - Names are case-sensitive: `marks` and `Marks` are different.

**P5. (Short answer)** What is the difference between `/` and `//`? Give an example of each.

??? success "Model Answer"

    `/` is true division. It always gives a `float`, for example `7 / 2` gives `3.5`, and `4 / 2` gives `2.0`. `//` is floor division. It gives only the whole part of the answer, for example `7 // 2` gives `3`.

**P6. (Predict the output)** What does this program print?

<!-- answer -->
```python
a = 23
b = 4
print(a // b)
print(a % b)
print(a ** 2)
print(a / b)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    5
    3
    529
    5.75
    ```

    23 divided by 4 is 5 with a remainder of 3, so `//` gives 5 and `%` gives 3. `**` is the power, 23 squared. `/` gives the exact decimal answer.

**P7. (Predict the output)** What does this program print? Work out the order of operations first.

<!-- answer -->
```python
x = 2 + 3 * 4 ** 2 - 10 // 3
print(x)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    47
    ```

    The order is `**` first: `4 ** 2 = 16`. Then `*` and `//`: `3 * 16 = 48` and `10 // 3 = 3`. Last, `+` and `-` from left to right: `2 + 48 - 3 = 47`.

**P8. (Predict the output)** What does this program print?

<!-- answer -->
```python
marks = 50
attendance = 80
print(marks >= 45 and attendance >= 85)
print(marks >= 45 or attendance >= 85)
print(not (marks > 60))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    False
    True
    True
    ```

    The first line needs both conditions, and the attendance one is `False`. The second needs only one, and the marks one is `True`. In the third line, `marks > 60` is `False`, and `not` turns it into `True`.

**P9. (Short answer)** What is type conversion? Why must we write `int(input(...))` when we read a number from the user?

??? success "Model Answer"

    Type conversion means changing a value from one type to another, with functions such as `int()`, `float()` and `str()`. The `input()` function always returns text (`str`), even when the user types digits. Python cannot do arithmetic on text, so `int()` turns the text into a whole number first. For example, `int("78") + 5` gives `83`.

**P10. (Predict the output)** What does this program print when the user types `15`?

<!-- stdin: 15 -->
<!-- error -->
<!-- answer -->
```python
age = input("Enter your age: ")
print("Next year you will be", age + 1)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    Enter your age: 15
    Traceback (most recent call last):
      File "example.py", line 2, in <module>
        print("Next year you will be", age + 1)
                                       ~~~~^~~
    TypeError: can only concatenate str (not "int") to str
    ```

    It gives a `TypeError`. The value of `age` is the text `"15"`, and Python cannot add a number to text. The fix is `age = int(input("Enter your age: "))`.

**P11. (Long answer)** Explain the different types of operators in Python with examples.

??? success "Model Answer"

    An operator is a symbol that does something with values, called operands. Python has these groups.

    - **Arithmetic:** `+`, `-`, `*`, `/`, `//` (whole part), `%` (remainder), `**` (power).
    - **Comparison:** `==`, `!=`, `>`, `<`, `>=`, `<=`. They give `True` or `False`.
    - **Logical:** `and`, `or`, `not`. They join conditions.
    - **Assignment:** `=` and the short forms `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`.

    ```python
    x = 17
    y = 5
    print(x // y, x % y, x ** 2)
    print(x > y, x == y)
    print(x > 10 and y > 10)
    x += 3
    print(x)
    ```

    ```{ .text .output title="Output" }
    3 2 289
    True False
    False
    20
    ```

**P12. (Write a program)** Write a program that reads the principal (Rs.), the yearly rate (percent) and the time (years), and prints the simple interest. Use the formula `interest = principal * rate * time / 100`. Show the answer with two decimal places.

??? success "Model Answer"

    <!-- stdin: 10000 | 8 | 3 -->
    ```python
    principal = float(input("Principal (Rs.): "))
    rate = float(input("Rate (percent per year): "))
    time = float(input("Time (years): "))

    interest = principal * rate * time / 100
    print(f"Simple interest: Rs. {interest:.2f}")
    ```

    ```{ .text .output title="Output" }
    Principal (Rs.): 10000
    Rate (percent per year): 8
    Time (years): 3
    Simple interest: Rs. 2400.00
    ```
