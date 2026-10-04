# Unit III Exam Questions: Control Structures

[Back to the Unit III notes](../unit-03-control.md)

## Past Paper Questions

**Q1.** Define break and continue.

*Source: Python Programming Internal Exam (CCT), 2025, question 3. Listed under BCSIT on bcsitcenter.com; the page names no university or college. Marks not shown. [Page](https://bcsitcenter.com/material/python-programming-internal-exam-cct/).*

??? success "Model Answer (Written for These Notes)"

    `break` ends the whole loop at once. The program continues with the first line after the loop.

    `continue` skips the rest of the current round and jumps to the next round. The loop keeps running.

    ```python
    for n in range(1, 8):
        if n == 3:
            continue
        if n == 6:
            break
        print(n)
    ```

    ```{ .text .output title="Output" }
    1
    2
    4
    5
    ```

    The number 3 is skipped by `continue`. The loop stops at 6 because of `break`.

**Q2.** What are loops in Python? Explain for loop and while loop with examples.

*Source: Python Programming Internal Exam (CCT), 2025, question 6. Marks not shown. [Page](https://bcsitcenter.com/material/python-programming-internal-exam-cct/).*

??? success "Model Answer (Written for These Notes)"

    A **loop** repeats a block of code. Python has two loops.

    - A **for loop** repeats once for each item in a sequence, such as a list or a `range()`. Use it when you know how many times to repeat.
    - A **while loop** repeats as long as its condition is `True`. Use it when you do not know in advance how many rounds are needed.

    ```python
    marks = [78, 64, 92]
    for m in marks:
        print("Marks:", m)

    count = 1
    while count <= 3:
        print("Round", count)
        count = count + 1
    ```

    ```{ .text .output title="Output" }
    Marks: 78
    Marks: 64
    Marks: 92
    Round 1
    Round 2
    Round 3
    ```

## Practice Questions (Not from Past Papers)

**P1. (Short answer)** What is the difference between `=` and `==` in Python?

??? success "Model Answer"

    A single `=` **stores** a value in a variable: `marks = 45`. A double `==` **asks a question** and gives `True` or `False`: `marks == 45`. Writing `=` inside an `if` is a `SyntaxError`.

**P2. (Short answer)** Why is `elif` better than writing several separate `if` statements for grade bands?

??? success "Model Answer"

    Python checks the conditions of an `if`/`elif`/`else` chain from top to bottom and runs only the first one that is `True`. With separate `if` statements, Python checks every one, so a student with 85 marks would be given several grades.

**P3. (Short answer)** What is an infinite loop? Give one way it can happen and one way to stop it.

??? success "Model Answer"

    An **infinite loop** is a loop whose condition never becomes `False`, so the program never stops. It happens when the lines inside a `while` loop do not change the variable used in the condition. Press `Ctrl+C` in the terminal to stop it, and fix the loop so that something inside it changes.

**P4. (Short answer)** State the difference between `break` and `continue`.

??? success "Model Answer"

    `break` leaves the whole loop at once. `continue` skips the rest of the current round and goes on with the next round of the same loop.

**P5. (Predict the output)** What does this program print?

<!-- answer -->
```python
total = 0
for n in range(1, 5):
    total = total + n
print(total)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    10
    ```

    `range(1, 5)` gives 1, 2, 3 and 4, and the total adds them up.

**P6. (Predict the output)** What does this program print?

<!-- answer -->
```python
count = 0
while count < 3:
    print("Round", count)
    count = count + 1
print("Finished")
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    Round 0
    Round 1
    Round 2
    Finished
    ```

    The loop runs while `count` is 0, 1 and 2. When `count` becomes 3 the condition is `False`, so the loop ends.

**P7. (Predict the output)** What does this program print?

<!-- answer -->
```python
for n in range(1, 8):
    if n % 2 == 0:
        continue
    if n > 5:
        break
    print(n)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    1
    3
    5
    ```

    Even numbers are skipped by `continue`. When `n` reaches 7, it is odd but greater than 5, so `break` stops the loop before it prints.

**P8. (Predict the output)** What does this program print?

<!-- answer -->
```python
marks = 65
attendance = 70
if marks >= 80:
    print("A")
elif marks >= 65 and attendance >= 75:
    print("B")
elif marks >= 45:
    print("C")
else:
    print("Fail")
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    C
    ```

    The first condition is `False`. The second needs both parts to be `True`, but attendance is only 70, so it is `False`. The third condition is `True`, so the program prints `C`.

**P9. (Long answer)** Explain the `if`, `elif` and `else` statements with a flowchart and an example.

??? success "Model Answer"

    - `if` runs its lines only when its condition is `True`.
    - `elif` (else if) is checked only when the conditions above it were `False`.
    - `else` has no condition. It runs when every condition above was `False`.

    Python runs exactly one branch of the chain.

    ```mermaid
    flowchart TD
        A([Start]) --> B{"marks >= 80 ?"}
        B -- True --> C["Grade A"]
        B -- False --> D{"marks >= 45 ?"}
        D -- True --> E["Grade C"]
        D -- False --> F["Fail"]
        C --> G([End])
        E --> G
        F --> G
    ```

    ```python
    marks = 52
    if marks >= 80:
        print("Grade A")
    elif marks >= 45:
        print("Grade C")
    else:
        print("Fail")
    ```

    ```{ .text .output title="Output" }
    Grade C
    ```

**P10. (Long answer)** Compare the `for` loop and the `while` loop. When do you use each one?

??? success "Model Answer"

    | | `for` loop | `while` loop |
    |---|---|---|
    | Repeats | once for each item in a collection or `range()` | as long as a condition is `True` |
    | Number of rounds | known before the loop starts | not known before the loop starts |
    | Who changes the counter | Python moves to the next item | you must change the variable yourself |
    | Risk | very low | an infinite loop if the condition never becomes `False` |

    Use `for` to go through 40 marks in a list. Use `while` to keep asking until the user types the right password.

    ```python
    for day in range(1, 4):
        print("for loop, day", day)

    data_left = 3
    while data_left > 0:
        print("while loop, data left", data_left)
        data_left = data_left - 1
    ```

    ```{ .text .output title="Output" }
    for loop, day 1
    for loop, day 2
    for loop, day 3
    while loop, data left 3
    while loop, data left 2
    while loop, data left 1
    ```

**P11. (Write a program)** Write a program that prints the table of 7 from `7 x 1 = 7` to `7 x 10 = 70`.

??? success "Model Answer"

    ```python
    for i in range(1, 11):
        print("7 x", i, "=", 7 * i)
    ```

    ```{ .text .output title="Output" }
    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    7 x 4 = 28
    7 x 5 = 35
    7 x 6 = 42
    7 x 7 = 49
    7 x 8 = 56
    7 x 9 = 63
    7 x 10 = 70
    ```

**P12. (Write a program)** The list `[78, 64, 92, 38, 88, 41]` holds the marks of six students. Write a program that prints the roll number (starting from 1) of the first student who failed (below 45 marks). If nobody failed, print "All passed".

??? success "Model Answer"

    ```python
    marks = [78, 64, 92, 38, 88, 41]
    roll = 0
    found = False
    for m in marks:
        roll = roll + 1
        if m < 45:
            print("First failed: roll", roll, "with", m, "marks")
            found = True
            break
    if not found:
        print("All passed")
    ```

    ```{ .text .output title="Output" }
    First failed: roll 4 with 38 marks
    ```

    The variable `found` remembers whether `break` was used. Without it, "All passed" would be printed even after a failing student was found.
