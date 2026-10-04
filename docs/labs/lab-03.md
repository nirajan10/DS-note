# Lab 3: Conditions, Loops, Break and Continue

## Objective

Write a grade report with `if`, `elif` and `else` inside a `for` loop. Then use `continue` to skip a value and `break` to stop a `while` loop early.

## What You Need

- The maths marks of the ten students in `students.csv`, typed into the program as a list. No file is read in this lab.
- Background: [Unit III](../unit-03-control.md).

## Steps

1. Open a new file `grades.py`.
2. Type the list of ten marks. These are the `math` column of `students.csv`.
3. Write the `for` loop. Inside it, use `if`, `elif` and `else` to set the grade.
4. Count how many students passed (45 or more). Print the count after the loop.
5. Run it and compare. Then do Your Turn, which adds `continue` and `break`.

## Starter Code

```python
marks = [78, 64, 92, 45, 88, 56, 73, 81, 39, 67]   # math column of students.csv

passed = 0
for m in marks:
    if m >= 80:
        grade = "A"
    elif m >= 65:
        grade = "B"
    elif m >= 45:
        grade = "C"
    else:
        grade = "Fail"
    print(m, "grade", grade)
    if grade != "Fail":
        passed = passed + 1

print("Passed:", passed, "out of", len(marks))
```

```{ .text .output title="Output" }
78 grade B
64 grade C
92 grade A
45 grade C
88 grade A
56 grade C
73 grade B
81 grade A
39 grade Fail
67 grade B
Passed: 9 out of 10
```

## Your Turn

1. Print the average of only the passing marks. Use `continue` to skip every mark below 45.
2. Use a `while` loop and `break` to find the first mark of 80 or more. Print its roll number (the first student has roll 1).

??? success "Solution"

    ```python
    marks = [78, 64, 92, 45, 88, 56, 73, 81, 39, 67]

    total = 0
    count = 0
    for m in marks:
        if m < 45:
            continue
        total = total + m
        count = count + 1
    print("Average of passing marks:", round(total / count, 1))
    ```

    ```{ .text .output title="Output" }
    Average of passing marks: 71.6
    ```

    ```python
    marks = [78, 64, 92, 45, 88, 56, 73, 81, 39, 67]

    i = 0
    while i < len(marks):
        if marks[i] >= 80:
            print("First mark of 80 or more: roll", i + 1, "with", marks[i])
            break
        i = i + 1
    ```

    ```{ .text .output title="Output" }
    First mark of 80 or more: roll 3 with 92
    ```

## Check Yourself

- [ ] My grade report prints one line for each of the ten students.
- [ ] I can explain why the order of `if`, `elif` and `else` matters.
- [ ] I can say the difference between `break` and `continue`.
- [ ] I changed the variable inside my `while` loop so that it ends.
