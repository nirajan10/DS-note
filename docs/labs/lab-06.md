# Lab 6: Files, CSV, JSON and Exceptions

## Objective

Read a **CSV file** (a plain-text table, with commas between the values), save data as a **JSON file** (a plain-text format of keys and values, like a dictionary), and use `try` and `except` so that a missing file does not crash the program.

## What You Need

- `students.csv` in your folder ([Practice Data Files](../setup.md#practice-data-files)).
- Libraries: `csv` and `json`. Both come with Python.
- Background: [Unit VI](../unit-06-files.md).

## Steps

1. Open a new file `files.py`. Check that `students.csv` is in the same folder.
2. Read the file with `csv.DictReader` inside a `try` block. Handle `FileNotFoundError`.
3. Build a dictionary of name and maths marks. The CSV gives text, so convert each mark with `int()`.
4. Save the dictionary to `math_marks.json` with `json.dump()`. Read it back with `json.load()`.
5. Try to open a file that does not exist, and see the `except` message instead of a crash.

## Starter Code

```python
import csv
import json

try:
    with open("students.csv", newline="") as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    print("students.csv is not in this folder")
    rows = []

summary = {}
for row in rows:
    summary[row["name"]] = int(row["math"])   # CSV gives text, so convert

with open("math_marks.json", "w") as f:
    json.dump(summary, f, indent=2)

with open("math_marks.json") as f:
    back = json.load(f)
print("Students saved:", len(back))
print("Asha:", back["Asha"])

try:
    open("results_2025.csv")
except FileNotFoundError:
    print("File not found, but the program goes on")
```

```{ .text .output title="Output" }
Students saved: 10
Asha: 78
File not found, but the program goes on
```

## Your Turn

1. Write the students who scored 45 or more in maths into a new file `passed.csv` with `csv.writer`. Read it back and print how many rows it has.
2. Ask the user for a number with `input()`. If the user types text such as `abc`, catch the `ValueError` and print `Please type a number`.

??? success "Solution"

    ```python
    import csv

    with open("students.csv", newline="") as f:
        rows = list(csv.DictReader(f))

    with open("passed.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "math"])
        for row in rows:
            if int(row["math"]) >= 45:
                writer.writerow([row["name"], row["math"]])

    with open("passed.csv", newline="") as f:
        saved = list(csv.reader(f))
    print("Rows in passed.csv:", len(saved) - 1, "students")
    ```

    ```{ .text .output title="Output" }
    Rows in passed.csv: 9 students
    ```

    <!-- stdin: abc -->
    ```python
    try:
        number = int(input("Type a number: "))
        print("Double is", number * 2)
    except ValueError:
        print("Please type a number")
    ```

    ```{ .text .output title="Output" }
    Type a number: abc
    Please type a number
    ```

## Check Yourself

- [ ] I used `with open(...)`, so my files close by themselves.
- [ ] I know why `int()` was needed after reading from a CSV.
- [ ] I wrote a JSON file and read it back.
- [ ] My program printed a friendly message instead of a crash when a file was missing.
