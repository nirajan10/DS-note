# Unit VI Exam Questions: File Handling and Exception

[Back to the Unit VI notes](../unit-06-files.md)

## Past Paper Questions

**Q1.** Explain Exception handling in Python with examples of try, except, else, finally.

*Source: Python Programming Internal Exam (CCT), 2025, question 9. Listed under BCSIT on bcsitcenter.com; the page names no university or college. Marks not shown. [Page](https://bcsitcenter.com/material/python-programming-internal-exam-cct/).*

??? success "Model Answer (Written for These Notes)"

    An **exception** is an error that happens while a program is running. **Exception handling** lets the program deal with the error instead of crashing.

    - `try`: the code that might fail.
    - `except`: runs only if the `try` code raised that error.
    - `else`: runs only if the `try` code had no error.
    - `finally`: always runs, error or not. It is used for clean-up.

    ```python
    def divide(a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Cannot divide by zero")
        else:
            print("Result:", result)
        finally:
            print("Done")

    divide(10, 2)
    divide(10, 0)
    ```

    ```{ .text .output title="Output" }
    Result: 5.0
    Done
    Cannot divide by zero
    Done
    ```

## Practice Questions (Not from Past Papers)

**P1. (Short answer)** What is the difference between opening a file in `"w"` mode and in `"a"` mode?

??? success "Model Answer"

    `"w"` (write) starts a fresh file. If the file already exists, its old content is erased first. `"a"` (append) keeps the old content and adds the new text at the end of the file. If the file does not exist, both modes create it.

**P2. (Short answer)** Why do we write `with open("marks.txt") as f:` instead of only `f = open("marks.txt")`?

??? success "Model Answer"

    The `with` statement closes the file automatically when its indented block ends, even if an error happens inside the block. A file that stays open can lose data or stay locked. With plain `open()` the programmer must remember to call `f.close()`.

**P3. (Predict the output)** What does this program print?

<!-- answer -->
```python
with open("data.txt", "w") as f:
    f.write("10\n")
    f.write("20\n")

with open("data.txt", "a") as f:
    f.write("30\n")

total = 0
with open("data.txt") as f:
    for line in f:
        total = total + int(line)
print(total)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    60
    ```

    The first block writes two lines. The second block appends a third line, so the file holds 10, 20 and 30. The loop reads each line as text, `int()` turns it into a number, and the total is 60.

**P4. (Predict the output)** What does this program print? Explain why.

<!-- answer -->
```python
with open("notes.txt", "w") as f:
    f.write("first\n")

with open("notes.txt", "w") as f:
    f.write("second\n")

with open("notes.txt") as f:
    print(f.read())
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    second
    ```

    The second `open()` uses `"w"`, which erases the old content. Only the word `second` is left in the file.

**P5. (Short answer)** The `csv` module reads a file where one column holds marks. Why can the program not add 10 to a mark straight away, and how is it fixed?

??? success "Model Answer"

    The `csv` module gives every value as a string, even when it looks like a number. Adding `10` to a string raises `TypeError`. The fix is to convert first: `int(row["math"]) + 10` (or `float()` for decimals).

**P6. (Write a program)** Write a program that reads `students.csv` with `csv.DictReader` and prints the name of every student whose science mark is above 80, then the number of such students.

??? success "Model Answer"

    ```python
    import csv

    count = 0
    with open("students.csv", newline="") as f:
        for row in csv.DictReader(f):
            if int(row["science"]) > 80:
                print(row["name"], row["science"])
                count = count + 1

    print("Students above 80:", count)
    ```

    ```{ .text .output title="Output" }
    Asha 85
    Chandra 88
    Elina 91
    Students above 80: 3
    ```

**P7. (Short answer)** Name the four main functions of the `json` module and say what each one does.

??? success "Model Answer"

    | Function | What it does |
    |---|---|
    | `json.load(file)` | reads a JSON file and gives Python data |
    | `json.dump(data, file)` | writes Python data into a JSON file |
    | `json.loads(text)` | turns a JSON string into Python data |
    | `json.dumps(data)` | turns Python data into a JSON string |

    The letter `s` stands for string. JSON objects become dictionaries and JSON arrays become lists.

**P8. (Write a program)** Write a program that reads `students.json` and writes a new CSV file `passed.csv` with the columns `name` and `math`, for every student with 45 or more maths marks. Then read `passed.csv` back and print how many students it holds.

??? success "Model Answer"

    ```python
    import csv
    import json

    with open("students.json") as f:
        students = json.load(f)

    with open("passed.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "math"])
        for s in students:
            if s["math"] >= 45:
                writer.writerow([s["name"], s["math"]])

    with open("passed.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    print("Students in passed.csv:", len(rows))
    ```

    ```{ .text .output title="Output" }
    Students in passed.csv: 9
    ```

    The header row is not counted, because `DictReader` uses it for the keys.

**P9. (Predict the output)** What does this program print?

<!-- answer -->
```python
def check(text):
    try:
        number = int(text)
    except ValueError:
        print("bad")
    else:
        print("good", number)
    finally:
        print("done")

check("12")
check("x")
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    good 12
    done
    bad
    done
    ```

    For `"12"` there is no exception, so `else` runs, then `finally`. For `"x"`, `int()` raises `ValueError`, so `except` runs, and `finally` runs again.

**P10. (Short answer)** What is a bare `except:` and why is it a bad habit? What should you write instead?

??? success "Model Answer"

    A bare `except:` has no exception name, so it catches every kind of error, including typing mistakes such as a wrong variable name. It hides the real problem and shows a wrong message. Catch only the exception you expect, such as `except ValueError:` or `except FileNotFoundError:`.

**P11. (Write a program)** Write a function `average_from_file(filename)` that reads whole numbers, one per line. It must skip lines that are not numbers, and it must print a message and return `None` when the file does not exist. Test it with a file that holds the lines `78`, `64`, `absent` and `92`, and with a file name that does not exist.

??? success "Model Answer"

    ```python
    def average_from_file(filename):
        try:
            with open(filename) as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(filename, "was not found")
            return None

        marks = []
        for line in lines:
            try:
                marks.append(int(line))
            except ValueError:
                print("Skipping:", line.strip())
        return sum(marks) / len(marks)

    with open("marks.txt", "w") as f:
        f.write("78\n64\nabsent\n92\n")

    print(average_from_file("marks.txt"))
    print(average_from_file("missing.txt"))
    ```

    ```{ .text .output title="Output" }
    Skipping: absent
    78.0
    missing.txt was not found
    None
    ```

    The outer `try` handles the missing file. The inner `try` handles one bad line at a time, so one bad line does not stop the whole read.

**P12. (Long answer)** Explain exception handling in Python. Say what an exception is, how it differs from a syntax error, and the job of `try`, `except`, `else` and `finally`. Give a short example.

??? success "Model Answer"

    A **syntax error** is a mistake in how the code is written, such as a missing colon. Python finds it before the program starts. An **exception** is an error that happens while the program is running, such as `int("abc")`, a missing file or a division by zero. If nothing handles it, the program stops and prints a traceback.

    Exception handling lets the program deal with the problem and carry on:

    - `try` holds the lines that might fail.
    - `except` runs only if the named exception happens. Several `except` lines can catch different exceptions.
    - `else` runs only if no exception happened.
    - `finally` always runs, for tidy-up work.

    ```python
    try:
        ratio = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Ratio:", ratio)
    finally:
        print("Finished")
    ```

    ```{ .text .output title="Output" }
    Cannot divide by zero
    Finished
    ```
