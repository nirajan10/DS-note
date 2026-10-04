# Unit IV Exam Questions: Functions and Modules

[Back to the Unit IV notes](../unit-04-functions.md)

## Past Paper Questions

No past-paper question for this unit was found.

## Practice Questions (Not from Past Papers)

**P1. (Short answer)** What is a function? Give two reasons why programmers use functions.

??? success "Model Answer"

    A function is a named block of code that does one job. It is written once with `def` and can be run many times by calling its name.

    Two reasons: (1) it avoids repeating the same code, and (2) it makes a program easier to read and to fix, because a rule that changes is changed in one place only.

**P2. (Short answer)** What is the difference between a parameter and an argument? Show both in one example.

??? success "Model Answer"

    A parameter is the name written in the brackets of the `def` line. An argument is the real value given when the function is called.

    In `def percentage(marks, total):` the names `marks` and `total` are parameters. In the call `percentage(45, 60)` the values `45` and `60` are arguments.

**P3. (Predict the output)** What does this program print?

<!-- answer -->
```python
def show(name, marks=50):
    print(name, marks)

show("Asha")
show("Bikash", 70)
show(marks=64, name="Sita")
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    Asha 50
    Bikash 70
    Sita 64
    ```

    The first call uses the default value 50 for `marks`. The second call replaces it with 70. The third call uses keyword arguments, so the order does not matter.

**P4. (Predict the output)** What does this program print? Explain the last line.

<!-- answer -->
```python
def add(a, b):
    print(a + b)

result = add(2, 3)
print(result)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    5
    None
    ```

    The function prints `5` but has no `return` statement, so it gives back `None`. The variable `result` holds `None`.

**P5. (Short answer)** What is the difference between `print` and `return` inside a function? Which one lets you use the answer later in the program?

??? success "Model Answer"

    `print` only shows a value on the screen. `return` sends the value back to the place where the function was called and ends the function.

    Only `return` lets the program use the answer later, for example to store it in a variable, add it to another number or test it in an `if`.

**P6. (Write a program)** Write a function `mb_to_gb(mb)` that returns the data in GB (1 GB = 1024 MB), rounded to 2 decimal places. Use it in a loop for the daily data `[2048, 512, 3100]`.

??? success "Model Answer"

    ```python
    def mb_to_gb(mb):
        return round(mb / 1024, 2)

    for mb in [2048, 512, 3100]:
        print(mb, "MB =", mb_to_gb(mb), "GB")
    ```

    ```{ .text .output title="Output" }
    2048 MB = 2.0 GB
    512 MB = 0.5 GB
    3100 MB = 3.03 GB
    ```

**P7. (Short answer)** What are the base case and the recursive case of a recursive function? What happens if the base case is missing?

??? success "Model Answer"

    The base case is the smallest problem, which the function answers directly without calling itself. The recursive case is the part where the function calls itself with a smaller input.

    If the base case is missing, the function keeps calling itself and never stops. After about 1000 nested calls Python stops the program with a `RecursionError`.

**P8. (Predict the output)** What does this program print? Show how the answer is built.

<!-- answer -->
```python
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

print(total(4))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    10
    ```

    The base case is `n == 0`. The calls build `4 + (3 + (2 + (1 + 0)))`, so the answer is 10.

**P9. (Long answer)** Explain three ways of importing in Python. Give one example of each using the `math` module.

??? success "Model Answer"

    1. `import math` brings in the whole module. We write the module name before each function: `math.sqrt(16)`.
    2. `from math import sqrt` brings in only the named function. We use it without the module name: `sqrt(16)`.
    3. `import math as m` gives the module a shorter nickname: `m.sqrt(16)`. Data scientists use this style with `import pandas as pd` and `import numpy as np`.

    ```python
    import math
    from math import sqrt
    import math as m

    print(math.sqrt(16))
    print(sqrt(16))
    print(m.sqrt(16))
    ```

    ```{ .text .output title="Output" }
    4.0
    4.0
    4.0
    ```

**P10. (Write a program)** Write your own module `shop_tools.py` with a function `bill_with_tax(price, tax_rate=13)` that returns the price plus tax. Then import it in a second program and print the bill for Rs. 2000.

??? success "Model Answer"

    First file, saved as `shop_tools.py`:

    <!-- file: shop_tools.py -->
    ```python title="shop_tools.py"
    def bill_with_tax(price, tax_rate=13):
        return price + price * tax_rate / 100
    ```

    Second file, saved in the same folder:

    ```python
    from shop_tools import bill_with_tax

    print("Bill: Rs.", bill_with_tax(2000))
    ```

    ```{ .text .output title="Output" }
    Bill: Rs. 2260.0
    ```

**P11. (Predict the output)** What does this program print?

<!-- answer -->
```python
import statistics

data = [4, 8, 8, 10]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.mode(data))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    7.5
    8.0
    8
    ```

    The mean is the average (30 divided by 4). The median is the middle value: the two middle numbers are 8 and 8. The mode is the value that appears most often, which is 8.

**P12. (Long answer)** What is the difference between a module and a library? What does `pip install` do? Name three libraries used later in this course and say what each is for.

??? success "Model Answer"

    A module is one Python file that holds ready-made functions. A library is a bigger collection of modules built around one purpose.

    `pip install` downloads a library from the internet and installs it so that Python can `import` it. It is done once per computer, in a terminal (or with `!pip install` in a notebook).

    Three examples: NumPy for fast number arrays and maths, Pandas for tables of data, and Matplotlib for drawing charts. (Seaborn for statistical charts and Scikit-learn for machine learning are also correct.)
