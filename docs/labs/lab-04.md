# Lab 4: Functions and Modules

## Objective

Write your own functions with parameters and return values, put them in a small **module** of your own, and **import** them. A module is a Python file whose functions other programs can reuse. You also use the built-in `math` and `statistics` modules.

## What You Need

- Two files in one folder: `helpers.py` (your module) and `lab4.py` (the program that imports it).
- Background: [Unit IV](../unit-04-functions.md).

## Steps

1. Create `helpers.py` and type the two functions below. Save it.
2. Create `lab4.py` in the same folder. The file names must match the `import` line.
3. In `lab4.py`, import `math`, `statistics` and `helpers`.
4. Call `helpers.grade()` for each mark. Notice that it **returns** the grade instead of printing it.
5. Run `lab4.py` and compare the output.

## Starter Code

First the module. It is a file, so it is saved and not run on its own.

<!-- file: helpers.py -->
```python title="helpers.py"
def grade(marks):
    # Return a grade letter for one marks value
    if marks >= 80:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 45:
        return "C"
    return "Fail"


def average(numbers):
    return sum(numbers) / len(numbers)
```

Now the program that uses it.

```python
import math
import statistics
import helpers

marks = [78, 64, 92, 45, 88]

for m in marks:
    print(m, helpers.grade(m))

print("Average:", round(helpers.average(marks), 1))
print("Median:", statistics.median(marks))
print("Square root of 81:", math.sqrt(81))
```

```{ .text .output title="Output" }
78 B
64 C
92 A
45 C
88 A
Average: 73.4
Median: 78
Square root of 81: 9.0
```

## Your Turn

1. In `lab4.py`, write a function `percentage(obtained, full=100)` that returns the percentage, rounded to 1 place. Call it as `percentage(78)` and as `percentage(342, 400)`.
2. Print the standard deviation of `marks` rounded to 2 places with `statistics.stdev`, and the average rounded up to a whole number with `math.ceil`.

??? success "Solution"

    ```python
    import math
    import statistics
    import helpers


    def percentage(obtained, full=100):
        return round(obtained / full * 100, 1)


    marks = [78, 64, 92, 45, 88]

    print(percentage(78))
    print(percentage(342, 400))
    print("Standard deviation:", round(statistics.stdev(marks), 2))
    print("Average rounded up:", math.ceil(helpers.average(marks)))
    ```

    ```{ .text .output title="Output" }
    78.0
    85.5
    Standard deviation: 19.2
    Average rounded up: 74
    ```

## Check Yourself

- [ ] My function uses `return`, and I used its result in a `print()`.
- [ ] I can say what a default parameter is, and I used one.
- [ ] My own module `helpers.py` imports without an error.
- [ ] I used at least one function from `math` and one from `statistics`.
