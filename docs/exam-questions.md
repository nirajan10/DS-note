# Exam Questions

This page collects questions for every unit. Each unit has two parts: **Past Paper Questions**, copied word for word from a published paper, and **Practice Questions (Not from Past Papers)**, written for these notes. Every answer is hidden. Try the question first, then open **Model Answer**.

## Where These Questions Come From

!!! warning "No DSC 481 Paper Was Found"

    When these notes were written, no past paper or model question for Pokhara University **DSC 481 Fundamentals of Data Science** (BCSIT) could be found online. The course is new, and the sites that collect old papers have none for it. The past-paper questions below come from **related courses**. They are not DSC 481 questions. Use them to see what kind of questions are asked about the same topics.

**20 past-paper questions** are included, each with its source. Every one was read on the page linked under it. The sources do not show marks, so no marks are given. The model answers are written for these notes. They are not taken from any paper.

| Source | Course and year | Questions used |
|--------|-----------------|----------------|
| [BCSIT Center](https://bcsitcenter.com/material/python-programming-internal-exam-cct/) | Python Programming Internal Exam (CCT), 2025. A college internal exam listed under BCSIT. The page names no university or college. | 7 |
| [Hamro CSIT](https://hamrocsit.com/semester/seventh/data-mining/question-bank/2081) | Tribhuvan University, BSc CSIT, Data Warehousing and Data Mining (CSC410), 2078, 2079, 2080 and 2081 BS | 6 |
| [Hamro CSIT](https://hamrocsit.com/semester/second/stat-i/question-bank/2081) | Tribhuvan University, BSc CSIT, Statistics I (STA169), 2076, 2080, 2080-new, 2081 and 2082 BS | 7 |

Only questions that match this syllabus were kept. Questions on topics outside it (for example classes and objects, or decision-tree algorithms) were left out. Units I, IV, X and XI have no past-paper question because none was found for those topics.

**129 practice questions** were written for these notes. They are mixed: short answer, long answer, predict the output, and write a program. Every output shown in an answer comes from really running the code.

| Unit | Past-paper questions | Practice questions |
|------|----------------------|--------------------|
| Unit I: Introduction to Data Science and Python | 0 | 11 |
| Unit II: Python Programming Basics and Operators | 2 | 12 |
| Unit III: Control Structures | 2 | 12 |
| Unit IV: Functions and Modules | 0 | 12 |
| Unit V: Data Structures in Python | 2 | 12 |
| Unit VI: File Handling and Exception | 1 | 12 |
| Unit VII: Data Collection and Cleaning with Python | 5 | 11 |
| Unit VIII: Exploratory Data Analysis | 6 | 12 |
| Unit IX: Introduction to Machine Learning with Python | 2 | 14 |
| Unit X: Data Visualization and Reporting | 0 | 11 |
| Unit XI: Practical Lab Work | 0 | 10 |

## Unit I: Introduction to Data Science and Python

[Back to the Unit I notes](unit-01-intro.md)

### Past Paper Questions

No past-paper question for this unit was found.

### Practice Questions (Not from Past Papers)

**P1. (Short answer)** What is data science? Give one everyday example.

??? success "Model Answer"

    Data science is the work of using data to answer questions and to make better decisions. It combines collecting data, cleaning it, exploring it for patterns and sharing what the patterns mean.

    Example: a shop owner studies the sales records of past weeks to decide how many packets of rice to stock next week.

**P2. (Short answer)** List the steps of the data science workflow in the correct order.

??? success "Model Answer"

    1. Ask a question
    2. Collect data
    3. Clean data
    4. Explore data
    5. Build a model
    6. Share results

    The answer often leads to a new question, so the cycle starts again.

**P3. (Long answer)** Explain the data science workflow using the example of a shop owner who wants to know which items to stock.

??? success "Model Answer"

    The workflow is a cycle of six steps.

    1. **Ask a question.** The owner asks, "Which three items sell the most each week?"
    2. **Collect data.** The owner gathers the sales records from the shop book or billing machine.
    3. **Clean data.** Missing values, repeated rows and typing mistakes are fixed, because real data is never perfect.
    4. **Explore data.** The owner looks at totals, averages and charts to see what the data says.
    5. **Build a model.** A model is a small program that learns a pattern from past data and predicts, for example, next week's sales.
    6. **Share results.** The answer is shown in a chart or a short report that the owner understands.

    The result may raise a new question, such as "Do sales rise before a festival?", and the cycle begins again.

**P4. (Short answer)** Name three areas where data science is used. For each, write one question that its data can answer.

??? success "Model Answer"

    - Weather forecast: "Will it rain in Pokhara tomorrow?"
    - A bank: "Is this payment very different from the customer's usual payments?"
    - A school: "Which subject has the most failures this year?"

**P5. (Short answer)** Give four reasons why Python is popular for data science.

??? success "Model Answer"

    - It is easy to read and learn, because the code looks close to English.
    - It is free to download and use.
    - It has many libraries, such as `pandas`, `numpy`, `matplotlib` and `scikit-learn`.
    - It has a large community, so help is easy to find.
    - It runs on Windows, macOS and Linux.

**P6. (Short answer)** What is a library? Name three libraries used in this course and say what each is used for.

??? success "Model Answer"

    A library is a ready-made toolbox of code written by other people, which we use instead of writing everything ourselves.

    - `pandas`: tables of data, such as loading, cleaning and summarising.
    - `matplotlib`: drawing charts.
    - `scikit-learn`: machine learning models.

**P7. (Predict the output)** What does this program print?

<!-- answer -->
```python
x = 12
y = 4.5
print(type(x))
print(type(y))
print(x * 2 + y)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    <class 'int'>
    <class 'float'>
    28.5
    ```

    `12` is a whole number (`int`) and `4.5` has a decimal point (`float`). The last line works out `12 * 2 = 24` first, then adds `4.5`, giving `28.5`.

**P8. (Predict the output)** What does this program print?

<!-- answer -->
```python
a = 40
b = 35
c = 60
print((a + b + c) / 3)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    45.0
    ```

    The brackets make Python add first: 40 + 35 + 60 = 135. Then it divides by 3. The `/` operator gives a decimal number, so the answer is `45.0`.

**P9. (Long answer)** Differentiate between Anaconda, Jupyter Notebook and Google Colab.

??? success "Model Answer"

    | | Anaconda | Jupyter Notebook | Google Colab |
    |---|---|---|---|
    | What it is | A package that installs Python, data science libraries and tools | A browser tool for writing and running Python in cells | A free notebook service run by Google |
    | Where code runs | On your own computer | On your own computer | On Google's computers |
    | Installation | Needs a large download and install | Comes with Anaconda | None; open it in a browser |
    | Internet | Needed once to download | Not needed to run | Needed all the time |
    | Account | None | None | A Google account |
    | Files | Stay on your computer | Stay on your computer | Uploaded files are deleted when the session ends |

**P10. (Short answer)** How do you run a cell in a notebook? Why does running a cell that uses a variable give a `NameError` in a fresh notebook?

??? success "Model Answer"

    Click the cell and press `Shift+Enter`. A notebook remembers a variable only after the cell that creates it has been run. If a cell uses `marks` before the cell that sets `marks` has run, Python does not know the name yet and shows `NameError`. Run the cells in order from the top.

**P11. (Write a program)** Write a program that stores a student's name and marks in Maths and Science in variables. It should print the name and the total marks in one line.

??? success "Model Answer"

    ```python
    name = "Asha"
    math = 78
    science = 64
    total = math + science
    print(name, "scored", total, "marks in total")
    ```

    ```{ .text .output title="Output" }
    Asha scored 142 marks in total
    ```

## Unit II: Python Programming Basics and Operators

[Back to the Unit II notes](unit-02-basics.md)

### Past Paper Questions

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

### Practice Questions (Not from Past Papers)

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

## Unit III: Control Structures

[Back to the Unit III notes](unit-03-control.md)

### Past Paper Questions

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

### Practice Questions (Not from Past Papers)

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

## Unit IV: Functions and Modules

[Back to the Unit IV notes](unit-04-functions.md)

### Past Paper Questions

No past-paper question for this unit was found.

### Practice Questions (Not from Past Papers)

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

## Unit V: Data Structures in Python

[Back to the Unit V notes](unit-05-structures.md)

### Past Paper Questions

**Q1.** Write difference between Tuple and List

*Source: Python Programming Internal Exam (CCT), 2025, question 4. Listed under BCSIT on bcsitcenter.com; the page names no university or college. Marks not shown. [Page](https://bcsitcenter.com/material/python-programming-internal-exam-cct/).*

??? success "Model Answer (Written for These Notes)"

    | | List | Tuple |
    |---|---|---|
    | Brackets | `[ ]` | `( )` |
    | Can items be changed? | Yes (mutable) | No (immutable) |
    | Methods | Many: `append()`, `remove()`, `sort()` | Few: `count()`, `index()` |
    | Use it for | Data that changes, such as a list of marks you keep adding to | Fixed data, such as a (latitude, longitude) pair |

    ```python
    marks_list = [70, 82]
    marks_list[0] = 75
    print(marks_list)
    ```

    ```{ .text .output title="Output" }
    [75, 82]
    ```

    <!-- error -->
    ```python
    marks_tuple = (70, 82)
    marks_tuple[0] = 75
    ```

    ```{ .text .output title="Output" }
    Traceback (most recent call last):
      File "example.py", line 2, in <module>
        marks_tuple[0] = 75
        ~~~~~~~~~~~^^^
    TypeError: 'tuple' object does not support item assignment
    ```

**Q2.** Define Dictionary in Python

*Source: Python Programming Internal Exam (CCT), 2025, question 5. Marks not shown. [Page](https://bcsitcenter.com/material/python-programming-internal-exam-cct/).*

??? success "Model Answer (Written for These Notes)"

    A **dictionary** stores data as **key: value** pairs inside curly brackets `{ }`. You look up a value by its key, not by a position number. Keys must be unique.

    ```python
    student = {"name": "Asha", "math": 78, "science": 85}
    print(student["name"])
    student["english"] = 72
    print(student)
    ```

    ```{ .text .output title="Output" }
    Asha
    {'name': 'Asha', 'math': 78, 'science': 85, 'english': 72}
    ```

### Practice Questions (Not from Past Papers)

**P1. (Long answer)** Compare the four Python data structures: list, tuple, set and dictionary. Mention their brackets, whether they can be changed, whether they allow duplicates, and give one use for each.

??? success "Model Answer"

    | | List | Tuple | Set | Dictionary |
    |---|---|---|---|---|
    | Brackets | `[ ]` | `( )` | `{ }` | `{key: value}` |
    | Can be changed? | yes | no | yes | yes |
    | Duplicates | allowed | allowed | not allowed | keys must be unique |
    | Order | kept | kept | not kept | kept |
    | Example use | marks of a class | location `(28.2, 84.0)` | different cities in a sales list | details of one student |

    A list holds an ordered, changeable collection. A tuple holds a fixed record. A set keeps only unique items and supports union, intersection and difference. A dictionary stores key-value pairs and finds a value by its key.

**P2. (Predict the output)** What does this program print?

<!-- answer -->
```python
marks = [78, 64, 92, 45, 88]
print(marks[0], marks[-1])
print(marks[1:3])
print(len(marks), max(marks))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    78 88
    [64, 92]
    5 92
    ```

    Index 0 is the first item and index `-1` is the last. The slice `[1:3]` starts at index 1 and stops before index 3, so it gives the items at indexes 1 and 2.

**P3. (Predict the output)** What does this program print after each step?

<!-- answer -->
```python
marks = [50, 80]
marks.append(65)
print(marks)
marks.insert(0, 90)
print(marks)
removed = marks.pop()
print(removed, marks)
marks.sort()
print(marks)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    [50, 80, 65]
    [90, 50, 80, 65]
    65 [90, 50, 80]
    [50, 80, 90]
    ```

    `append` adds at the end. `insert(0, 90)` adds at the front. `pop()` removes and returns the last item. `sort()` puts the remaining items in order.

**P4. (Short answer)** What is the difference between `marks.sort()` and `sorted(marks)`? What does `marks.sort()` return?

??? success "Model Answer"

    `marks.sort()` sorts the list itself and changes it. It returns `None`. `sorted(marks)` leaves the original list as it is and returns a new sorted list.

    So `ranked = marks.sort()` stores `None` in `ranked`, which is a common mistake. Write `ranked = sorted(marks)` instead.

**P5. (Write a program)** The marks of six students are `[78, 38, 92, 45, 41, 66]`. Write a program that puts the passing marks (45 or more) into a new list and prints that list, how many students passed and the average of the passing marks.

??? success "Model Answer"

    ```python
    marks = [78, 38, 92, 45, 41, 66]
    passed = []
    for m in marks:
        if m >= 45:
            passed.append(m)
    print("Passing marks:", passed)
    print("Students passed:", len(passed))
    print("Average of passed:", sum(passed) / len(passed))
    ```

    ```{ .text .output title="Output" }
    Passing marks: [78, 92, 45, 66]
    Students passed: 4
    Average of passed: 70.25
    ```

**P6. (Short answer)** How is a tuple different from a list? When would you choose a tuple? What is unpacking?

??? success "Model Answer"

    A list can be changed after it is made (it is mutable). A tuple cannot be changed (it is immutable). A list uses square brackets and a tuple uses round brackets.

    Choose a tuple for values that should stay fixed, such as a location `(28.2, 84.0)` or a student record, and for the two values a function returns.

    Unpacking copies the items of a tuple into separate variables in one line, for example `name, roll, marks = ("Asha", 101, 78)`.

**P7. (Predict the output)** What happens when this program runs?

<!-- error; answer -->
```python
student = ("Asha", 101, 78)
print(student[0])
student[2] = 85
print(student)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    Asha
    Traceback (most recent call last):
      File "example.py", line 3, in <module>
        student[2] = 85
        ~~~~~~~^^^
    TypeError: 'tuple' object does not support item assignment
    ```

    Reading `student[0]` works and prints `Asha`. Changing an item of a tuple is not allowed, so Python stops with a `TypeError` and the last line never runs.

**P8. (Predict the output)** What does this program print?

<!-- answer -->
```python
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(sorted(a | b))
print(sorted(a & b))
print(sorted(a - b))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    [1, 2, 3, 4, 5]
    [3, 4]
    [1, 2]
    ```

    `a | b` is the union (everything in either set). `a & b` is the intersection (in both). `a - b` is the difference (in `a` but not in `b`). We use `sorted()` because a set has no fixed order.

**P9. (Short answer)** What is a set? Name two of its properties, and show how to remove duplicates from a list.

??? success "Model Answer"

    A set is a collection of unique items written in curly brackets. Two properties: it keeps no duplicates, and it has no order, so it cannot be indexed.

    To remove duplicates, turn the list into a set:

    ```python
    cities = ["Pokhara", "Butwal", "Pokhara", "Kathmandu"]
    print(sorted(set(cities)))
    ```

    ```{ .text .output title="Output" }
    ['Butwal', 'Kathmandu', 'Pokhara']
    ```

**P10. (Predict the output)** What does this program print?

<!-- answer -->
```python
usage = {"Mon": 850, "Tue": 920}
usage["Wed"] = 1500
usage["Mon"] = 900
print(usage.get("Thu", 0))
for day, mb in usage.items():
    print(day, mb)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    0
    Mon 900
    Tue 920
    Wed 1500
    ```

    `"Wed"` is a new key, so it is added. `"Mon"` already exists, so its value is replaced. `get("Thu", 0)` gives the default `0` because `"Thu"` is not a key. The loop prints each key with its value.

**P11. (Short answer)** What is a `KeyError`? How does `get()` help to avoid it?

??? success "Model Answer"

    A `KeyError` is raised when we read a dictionary with square brackets and the key is not in it, for example `student["email"]`.

    The method `get()` does not raise an error. It returns `None` when the key is missing, or a default value that we choose: `student.get("email", "not given")`.

**P12. (Write a program)** Each student is stored as a dictionary in a list. Write a program that prints the name of every student who scored 45 or more in both subjects, and then the name of the topper (highest total).

??? success "Model Answer"

    ```python
    students = [
        {"name": "Asha", "math": 78, "science": 85},
        {"name": "Bikash", "math": 40, "science": 70},
        {"name": "Sita", "math": 92, "science": 88},
        {"name": "Ram", "math": 45, "science": 52},
    ]
    best_total = 0
    topper = ""
    for s in students:
        if s["math"] >= 45 and s["science"] >= 45:
            print("Passed both:", s["name"])
        total = s["math"] + s["science"]
        if total > best_total:
            best_total = total
            topper = s["name"]
    print("Topper:", topper)
    ```

    ```{ .text .output title="Output" }
    Passed both: Asha
    Passed both: Sita
    Passed both: Ram
    Topper: Sita
    ```

## Unit VI: File Handling and Exception

[Back to the Unit VI notes](unit-06-files.md)

### Past Paper Questions

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

### Practice Questions (Not from Past Papers)

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

## Unit VII: Data Collection and Cleaning with Python

[Back to the Unit VII notes](unit-07-cleaning.md)

### Past Paper Questions

**Q1.** Describe any two methods of handling noisy data.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Data Warehousing and Data Mining (CSC410), 2081 BS, Section B, question 4. Marks not shown. [Question bank](https://hamrocsit.com/semester/seventh/data-mining/question-bank/2081).*

??? success "Model Answer (Written for These Notes)"

    **Noise** is a random error or a wrong value in the data, for example a mark of 880 typed instead of 88.

    1. **Binning.** Sort the values and split them into small groups (bins). Replace each value with the mean of its bin. This smooths out small random errors.
    2. **Regression.** Fit a line to the data and replace each value by the value on the line. Points far from the line are treated as noise.

    ```python
    values = [4, 8, 15, 21, 21, 24, 25, 28, 34]
    for start in range(0, len(values), 3):
        bin_values = values[start:start + 3]
        mean = sum(bin_values) / len(bin_values)
        print(bin_values, "->", mean)
    ```

    ```{ .text .output title="Output" }
    [4, 8, 15] -> 9.0
    [21, 21, 24] -> 22.0
    [25, 28, 34] -> 29.0
    ```

    Each group of three values is replaced by its mean.

**Q2.** Discuss different ways of smoothing noisy data along with suitable examples.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Data Warehousing and Data Mining (CSC410), 2080 BS, Section B, question 5. Marks not shown. [Question bank](https://hamrocsit.com/semester/seventh/data-mining/question-bank/2080).*

??? success "Model Answer (Written for These Notes)"

    1. **Smoothing by bin means.** Replace every value in a bin by the bin's mean.
    2. **Smoothing by bin boundaries.** Replace every value in a bin by the closest of the bin's smallest or largest value.
    3. **Regression.** Fit a line and use the fitted values.
    4. **Outlier analysis.** Group similar values together (clustering). Values that fall outside every group are outliers and can be removed or corrected.

    ```python
    values = [4, 8, 15, 21, 21, 24, 25, 28, 34]
    for start in range(0, len(values), 3):
        b = values[start:start + 3]
        low, high = min(b), max(b)
        smoothed = [low if v - low <= high - v else high for v in b]
        print(b, "-> bin boundaries ->", smoothed)
    ```

    ```{ .text .output title="Output" }
    [4, 8, 15] -> bin boundaries -> [4, 4, 15]
    [21, 21, 24] -> bin boundaries -> [21, 21, 24]
    [25, 28, 34] -> bin boundaries -> [25, 25, 34]
    ```

**Q3.** Why data normalization is important in data mining? Explain min-max and Z-score normalization approach.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Data Warehousing and Data Mining (CSC410), 2079 BS, question 6. Marks not shown. [Question bank](https://hamrocsit.com/semester/seventh/data-mining/question-bank/2079).*

??? success "Model Answer (Written for These Notes)"

    **Why it matters.** Columns can be on very different scales, such as age (10 to 80) and income (10,000 to 500,000). Many methods use distances between rows, so the large-scale column would dominate. Normalization brings every column to a similar scale.

    - **Min-max:** `(x - min) / (max - min)`. The result is between 0 and 1.
    - **Z-score:** `(x - mean) / standard deviation`. The result has mean 0 and standard deviation 1.

    ```python
    import pandas as pd

    marks = pd.Series([39, 45, 56, 64, 78, 92])
    min_max = (marks - marks.min()) / (marks.max() - marks.min())
    z_score = (marks - marks.mean()) / marks.std()
    print(pd.DataFrame({"marks": marks, "min_max": min_max.round(2), "z_score": z_score.round(2)}))
    ```

    ```{ .text .output title="Output" }
       marks  min_max  z_score
    0     39     0.00    -1.16
    1     45     0.11    -0.86
    2     56     0.32    -0.32
    3     64     0.47     0.08
    4     78     0.74     0.78
    5     92     1.00     1.48
    ```

**Q4.** Define data discretization. Describe the tasks for data preprocessing.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Data Warehousing and Data Mining (CSC410), 2078 BS, Section B. Marks not shown. [Question bank](https://hamrocsit.com/semester/seventh/data-mining/question-bank/2078).*

??? success "Model Answer (Written for These Notes)"

    **Data discretization** turns continuous numbers into a small number of intervals or labels, such as marks into grade bands.

    **Tasks of data preprocessing:**

    1. **Data cleaning:** fix missing values, remove duplicates, handle noise and outliers.
    2. **Data integration:** combine data from several sources into one table.
    3. **Data transformation:** change the form of the data, for example normalization and type conversion.
    4. **Data reduction:** make the data smaller, for example by choosing only the useful columns.

    ```python
    import pandas as pd

    marks = pd.Series([39, 45, 56, 64, 78, 92])
    bands = pd.cut(marks, bins=[0, 44, 64, 100], labels=["Fail", "Pass", "Good"])
    print(pd.DataFrame({"marks": marks, "band": bands}))
    ```

    ```{ .text .output title="Output" }
       marks  band
    0     39  Fail
    1     45  Pass
    2     56  Pass
    3     64  Pass
    4     78  Good
    5     92  Good
    ```

    This course covers cleaning and transformation in [Unit VII](unit-07-cleaning.md).

**Q5.** Differentiate between primary data and secondary data. What are the sources of secondary data?

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Statistics I (STA169), 2080 BS. Marks not shown. [Question bank](https://hamrocsit.com/semester/second/stat-i/question-bank/2080).*

??? success "Model Answer (Written for These Notes)"

    | | Primary data | Secondary data |
    |---|---|---|
    | Collected by | You, for your own study | Someone else, for another purpose |
    | How | Surveys, interviews, experiments, measurements | Taken from existing records |
    | Cost and time | High | Low |
    | Example | A teacher records the marks of her own class | Using a published results report |

    **Sources of secondary data:** government reports and censuses, published research papers and books, company records, newspapers, and websites or open-data portals.

### Practice Questions (Not from Past Papers)

**P1. (Short answer)** What is a DataFrame? What do `head()`, `shape` and `info()` show?

??? success "Model Answer"

    A DataFrame is the main table object of Pandas. It has rows (records) and columns (properties), like a spreadsheet inside Python. `head()` shows the first rows, `shape` gives the number of rows and columns as a pair such as `(42, 6)`, and `info()` lists each column with its type and the count of non-missing values.

**P2. (Short answer)** Which Pandas function reads a CSV file, an Excel file and a JSON file? Which extra library does reading an `.xlsx` file need?

??? success "Model Answer"

    `pd.read_csv()`, `pd.read_excel()` and `pd.read_json()`. Reading `.xlsx` files needs the library `openpyxl`, which can be installed with `pip install openpyxl`. For nested JSON, `pd.json_normalize()` can flatten the records into a table.

**P3. (Predict the output)** What does this program print?

<!-- answer -->
```python
import pandas as pd

df = pd.DataFrame({"name": ["Asha", "Bikash", "Chandra"],
                   "marks": [78, None, 92]})
print(df["marks"].isna().sum())
print(df["marks"].fillna(df["marks"].mean()).tolist())
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    1
    [78.0, 85.0, 92.0]
    ```

    One value is missing. The mean of the other two marks (78 and 92) is 85, so the gap is filled with 85.0.

**P4. (Short answer)** A student writes `df["marks"].fillna(0)` and finds that the missing values are still in `df`. Why, and how should the line be written?

??? success "Model Answer"

    `fillna()` does not change the table. It returns a new column, and the result was thrown away. The result must be assigned back: `df["marks"] = df["marks"].fillna(0)`.

**P5. (Predict the output)** What does this program print?

<!-- answer -->
```python
import pandas as pd

df = pd.DataFrame({"city": ["Pokhara", "Butwal", "Pokhara", "Butwal"],
                   "sales": [10, 20, 10, 30]})
print(len(df.drop_duplicates()))
print(len(df.drop_duplicates(subset=["city"])))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    3
    2
    ```

    By default a row is a duplicate only when every column matches. Only rows 0 and 2 are identical, so 3 rows stay. With `subset=["city"]` only the city is compared, so one row per city stays: 2 rows.

**P6. (Short answer)** What is an outlier? Describe the IQR rule and name two ways to handle an outlier.

??? success "Model Answer"

    An outlier is a value far away from the rest of the data. It may be a mistake (a typing error) or a real rare event. The IQR rule: find `Q1` (`quantile(0.25)`) and `Q3` (`quantile(0.75)`), then `IQR = Q3 - Q1`. A value below `Q1 - 1.5 * IQR` or above `Q3 + 1.5 * IQR` is flagged as an outlier. It is only a flag, so the person decides what to do. Ways to handle it: filter (remove) the row, cap the value to a limit with `clip()`, or replace it with a sensible value such as the median.

**P7. (Write a program)** Using `shop_sales.csv`, add a column `total` (`quantity` times `price`), then print the total sales of each city and the name of the city with the highest total.

??? success "Model Answer"

    ```python
    import pandas as pd

    sales = pd.read_csv("shop_sales.csv")
    sales["total"] = sales["quantity"] * sales["price"]

    by_city = sales.groupby("city")["total"].sum()
    print(by_city)
    print("Best city:", by_city.idxmax())
    ```

    ```{ .text .output title="Output" }
    city
    Butwal       3340
    Kathmandu    8265
    Pokhara      8315
    Name: total, dtype: int64
    Best city: Pokhara
    ```

**P8. (Predict the output)** What does this program print?

<!-- answer -->
```python
import pandas as pd

marks = pd.Series([40, 60, 100])
scaled = (marks - marks.min()) / (marks.max() - marks.min())
print(scaled.round(2).tolist())
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    [0.0, 0.33, 1.0]
    ```

    This is min-max scaling. The smallest mark (40) becomes 0, the largest (100) becomes 1, and 60 becomes (60 - 40) / (100 - 40) = 0.33.

**P9. (Short answer)** Why do we normalize columns before some analysis? Give the min-max formula and the z-score formula.

??? success "Model Answer"

    Columns can have very different scales (attendance is below 100, mobile data is in thousands). Many methods treat larger numbers as more important, so the large-scale column would dominate. Normalization puts columns on a similar scale. Min-max: `(x - min) / (max - min)`, which gives values from 0 to 1. Z-score: `(x - mean) / std`, which gives a mean near 0 and a standard deviation near 1. Outliers should be handled first, or they squash the other values.

**P10. (Write a program)** `students_raw.csv` stores `attendance` as text like `92%` and `joined` as a text date. Write a program that converts `attendance` to whole numbers and `joined` to dates, then prints the new types of the two columns and the mean attendance rounded to one decimal.

??? success "Model Answer"

    ```python
    import pandas as pd

    df = pd.read_csv("students_raw.csv")
    df["attendance"] = df["attendance"].str.replace("%", "").astype(int)
    df["joined"] = pd.to_datetime(df["joined"])

    print(df[["attendance", "joined"]].dtypes)
    print("Mean attendance:", df["attendance"].mean().round(1))
    ```

    ```{ .text .output title="Output" }
    attendance             int64
    joined        datetime64[us]
    dtype: object
    Mean attendance: 83.8
    ```

    The `%` sign must be removed with `str.replace` first, because `astype(int)` cannot read `92%`.

**P11. (Long answer)** List the steps of cleaning a messy dataset in a sensible order. For each step name the Pandas tool you would use.

??? success "Model Answer"

    | Step | What to do | Pandas tool |
    |---|---|---|
    | 1. Load | read the file into a DataFrame | `read_csv`, `read_excel`, `read_json` |
    | 2. Inspect | look at size, types and gaps | `head()`, `shape`, `info()`, `isna().sum()` |
    | 3. Drop duplicates | remove repeated rows (before filling gaps, so copies do not change the mean) | `duplicated()`, `drop_duplicates()` |
    | 4. Fix missing values | drop rows or fill with the mean, median or a fixed value | `dropna()`, `fillna()` |
    | 5. Handle outliers | find with the IQR rule, then filter, cap or replace | `quantile()`, `clip()`, `where()` |
    | 6. Convert types | make text into numbers and dates | `astype()`, `pd.to_numeric()`, `pd.to_datetime()` |
    | 7. Save | write the clean table to a file | `to_csv(..., index=False)` |

    Always assign each result back to the DataFrame (`df = df.drop_duplicates()`), because these methods return new objects.

## Unit VIII: Exploratory Data Analysis

[Back to the Unit VIII notes](unit-08-eda.md)

### Past Paper Questions

**Q1.** What do your mean by measurement scale? Describe the different types of measurement scales used in statistics.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Statistics I (STA169), 2076 BS, question 12. Marks not shown. [Question bank](https://hamrocsit.com/semester/second/stat-i/question-bank/2076).*

??? success "Model Answer (Written for These Notes)"

    A **measurement scale** is the rule used to give a value to something we measure. The scale decides which calculations make sense.

    | Scale | What it tells you | Example | Sensible statistic |
    |---|---|---|---|
    | Nominal | Names or categories, no order | City: Pokhara, Kathmandu, Butwal | Mode, counts |
    | Ordinal | Categories with an order, but gaps are not equal | Grade: C, B, A | Median, mode |
    | Interval | Equal gaps, but zero is only a position | Temperature in degrees Celsius | Mean, standard deviation |
    | Ratio | Equal gaps and a true zero | Marks, height, mobile data in MB | All of them, and ratios |

**Q2.** Define statistics and discuss its importance in the field of computational sciences. The following are the numbers of minutes that a person had to wait for the bus to work on 20 working days : 15, 10, 2, 17, 5, 8, 3, 10, 2, 9, 5, 9, 13, 1, 10, 12, 5, 10, 8, 4. Compute mean, median, mode, standard, variance and coefficient of variation.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Statistics I (STA169), 2080-new BS, Section A, question 1. Marks not shown. [Question bank](https://hamrocsit.com/semester/second/stat-i/question-bank/2080-new).*

??? success "Model Answer (Written for These Notes)"

    **Statistics** is the science of collecting, organising, analysing and interpreting data to make decisions.

    **Importance in computational sciences:** it is the base of data analysis and machine learning. It summarises large data, shows patterns and relations, measures uncertainty, and tests whether a model works on new data.

    The 20 waiting times are a sample, so the standard deviation and variance below divide by n - 1. If the data were the whole population, they would divide by n.

    ```python
    import statistics as st

    waits = [15, 10, 2, 17, 5, 8, 3, 10, 2, 9, 5, 9, 13, 1, 10, 12, 5, 10, 8, 4]
    mean = st.mean(waits)
    sd = st.stdev(waits)
    print("mean:", mean)
    print("median:", st.median(waits))
    print("mode:", st.mode(waits))
    print("variance:", round(st.variance(waits), 2))
    print("standard deviation:", round(sd, 2))
    print("coefficient of variation:", round(sd / mean * 100, 1), "%")
    ```

    ```{ .text .output title="Output" }
    mean: 7.9
    median: 8.5
    mode: 10
    variance: 19.88
    standard deviation: 4.46
    coefficient of variation: 56.4 %
    ```

    The coefficient of variation is the standard deviation divided by the mean, times 100.

**Q3.** The following scores represent the final examination score for an elementary statistics course: 45, 65, 23, 32, 57, 74, 60, 30, 17, 19, 80, 59. (i) Compute five number summary. (ii) Construct a box and whisker plot and interpret the result.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Statistics I (STA169), 2081 BS, question 7. Marks not shown. [Question bank](https://hamrocsit.com/semester/second/stat-i/question-bank/2081).*

??? success "Model Answer (Written for These Notes)"

    The **five number summary** is the minimum, the first quartile (Q1), the median, the third quartile (Q3) and the maximum. This answer finds each quartile as the median of one half of the sorted data. Books differ slightly in how they find quartiles, so follow the rule your teacher uses.

    ```python
    def median(values):
        s = sorted(values)
        mid = len(s) // 2
        return s[mid] if len(s) % 2 else (s[mid - 1] + s[mid]) / 2

    def five_number_summary(values):
        s = sorted(values)
        half = len(s) // 2
        lower, upper = s[:half], s[half + len(s) % 2:]
        return min(s), median(lower), median(s), median(upper), max(s)

    scores = [45, 65, 23, 32, 57, 74, 60, 30, 17, 19, 80, 59]
    names = ["Minimum", "Q1", "Median", "Q3", "Maximum"]
    for name, value in zip(names, five_number_summary(scores)):
        print(name, value)
    ```

    ```{ .text .output title="Output" }
    Minimum 17
    Q1 26.5
    Median 51.0
    Q3 62.5
    Maximum 80
    ```

    <!-- figure: ex-box-scores -->
    ```python
    import matplotlib.pyplot as plt

    scores = [45, 65, 23, 32, 57, 74, 60, 30, 17, 19, 80, 59]
    plt.boxplot(scores, orientation="horizontal")
    plt.title("Final Exam Scores")
    plt.xlabel("Score")
    plt.yticks([])
    plt.show()
    ```

    ![Box plot of the twelve exam scores. The box runs from about 28 to 61 with the median line at 51; the whiskers reach 17 and 80. There are no outliers.](assets/img/ex-box-scores.png#only-light)
    ![Box plot of the twelve exam scores. The box runs from about 28 to 61 with the median line at 51; the whiskers reach 17 and 80. There are no outliers.](assets/img/ex-box-scores-dark.png#only-dark)

    Matplotlib finds quartiles by interpolation, so the box edges it draws (about 28 and 61) are a little different from the hand-calculated 26.5 and 62.5.

    **Interpretation:** The scores are widely spread: they run from 17 to 80, and the middle half of the students scored between 26.5 and 62.5. The median is 51. The median line is closer to the upper edge of the box, but the upper whisker is longer than the lower one, so there is no clear skew. No score is an outlier, because none lies more than 1.5 times the interquartile range (62.5 - 26.5 = 36) beyond a quartile.

**Q4.** Maximal static in respiratory pressure is an index of respiratory muscle strength. The following data show the measure of maximal static in respiratory for 11 cystic fibrosis patients: 115, 95, 100, 85, 90, 70, 45, 115, 40, 115, and 95 i) Calculate five number summary. ii) Construct a box-and-whisker plot. Also comment on the shape of the distribution.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Statistics I (STA169), 2082 BS, question 4 (Group B). Marks not shown. [Question bank](https://hamrocsit.com/semester/second/stat-i/question-bank/2082).*

??? success "Model Answer (Written for These Notes)"

    This uses the same median-of-halves rule as the previous question. With 11 values (an odd number), the median itself is left out of both halves.

    ```python
    def median(values):
        s = sorted(values)
        mid = len(s) // 2
        return s[mid] if len(s) % 2 else (s[mid - 1] + s[mid]) / 2

    def five_number_summary(values):
        s = sorted(values)
        half = len(s) // 2
        lower, upper = s[:half], s[half + len(s) % 2:]
        return min(s), median(lower), median(s), median(upper), max(s)

    pressure = [115, 95, 100, 85, 90, 70, 45, 115, 40, 115, 95]
    names = ["Minimum", "Q1", "Median", "Q3", "Maximum"]
    for name, value in zip(names, five_number_summary(pressure)):
        print(name, value)
    ```

    ```{ .text .output title="Output" }
    Minimum 40
    Q1 70
    Median 95
    Q3 115
    Maximum 115
    ```

    **Box plot:** draw a box from Q1 = 70 to Q3 = 115 with a line at the median, 95. Draw a whisker from 70 down to the minimum, 40. There is no whisker above the box, because Q3 and the maximum are both 115.

    **Shape:** The distribution is **left-skewed** (negatively skewed). The lower whisker is long, the upper whisker has no length, and the median is closer to Q3 than to Q1. Most patients have high readings, and a few low readings pull the tail to the left.

**Q5.** Define positive and negative correlation. What are the required assumptions for correlation analysis? A data analytic company wants to find the relation between traffic in website (X) per day and server downtime (Y) in minutes per day. The collected data are:

| X | 9 | 10 | 12 | 9 | 10 | 13 | 13 | 19 |
|---|---|----|----|---|----|----|----|----|
| Y | 26 | 38 | 27 | 45 | 55 | 80 | 84 | 100 |

(i) Find the correlation coefficient between x and y. Interpret the value. (ii) Find the regression equation of y on x. Estimate the value of y when x = 16. (iii) Interpret the value of y-intercept and slope of the line.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Statistics I (STA169), 2081 BS, question 2. The data table is shown here in table form. Marks not shown. [Question bank](https://hamrocsit.com/semester/second/stat-i/question-bank/2081).*

??? success "Model Answer (Written for These Notes)"

    **Positive correlation:** when X goes up, Y also goes up. **Negative correlation:** when X goes up, Y goes down.

    **Assumptions:** both variables are numbers; the pairs of values are collected together (one X for each Y); the relation is roughly a straight line; and there are no extreme outliers that dominate the result.

    ```python
    import numpy as np

    x = np.array([9, 10, 12, 9, 10, 13, 13, 19])
    y = np.array([26, 38, 27, 45, 55, 80, 84, 100])
    r = np.corrcoef(x, y)[0, 1]
    slope, intercept = np.polyfit(x, y, 1)
    print(f"correlation r = {r:.3f}")
    print(f"regression line: y = {intercept:.2f} + {slope:.2f} * x")
    print(f"estimate at x = 16: {intercept + slope * 16:.1f}")
    ```

    ```{ .text .output title="Output" }
    correlation r = 0.804
    regression line: y = -23.74 + 6.79 * x
    estimate at x = 16: 84.9
    ```

    **Interpretation:**

    - (i) r = 0.804 is a strong positive correlation. Days with more traffic tend to have more downtime.
    - (ii) The regression line is y = -23.74 + 6.79x. For x = 16 the estimated downtime is about 84.9 minutes per day.
    - (iii) The slope 6.79 means each extra unit of traffic adds about 6.79 minutes of downtime on average. The intercept -23.74 is the value of y when x = 0. A negative downtime is impossible, so the intercept has no real meaning here: x = 0 is far outside the data.

**Q6.** Discuss the meaning of i. positive ii. negative iii. perfect correlation between two variables. The following show the improvement (gain in reading speed) of 8 students in a speed reading program and the number of weeks they have been in program.

| Number of weeks | 4 | 5 | 3 | 9 | 7 | 10 | 4 | 5 |
|---|---|---|---|---|---|----|---|---|
| Speed gain | 85 | 120 | 48 | 192 | 164 | 234 | 74 | 110 |

a. Compute correlation coefficient and interpret its result. b. Find the regression equation of speed gain on number of weeks. c. Estimate speed gain of a student who has been in program for 6 weeks and interpret the slope of the line.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Statistics I (STA169), 2080 BS. Marks not shown. [Question bank](https://hamrocsit.com/semester/second/stat-i/question-bank/2080).*

??? success "Model Answer (Written for These Notes)"

    **Positive:** both variables rise together. **Negative:** one rises while the other falls. **Perfect:** the points lie exactly on a straight line, so r is +1 (perfect positive) or -1 (perfect negative).

    ```python
    import numpy as np

    weeks = np.array([4, 5, 3, 9, 7, 10, 4, 5])
    gain = np.array([85, 120, 48, 192, 164, 234, 74, 110])
    r = np.corrcoef(weeks, gain)[0, 1]
    slope, intercept = np.polyfit(weeks, gain, 1)
    print(f"correlation r = {r:.3f}")
    print(f"regression line: gain = {intercept:.2f} + {slope:.2f} * weeks")
    print(f"estimate at 6 weeks: {intercept + slope * 6:.1f}")
    ```

    ```{ .text .output title="Output" }
    correlation r = 0.989
    regression line: gain = -17.26 + 24.79 * weeks
    estimate at 6 weeks: 131.5
    ```

    **Interpretation:**

    - (a) r = 0.989 is a very strong positive correlation. Students who stayed longer in the program gained more speed.
    - (b) The regression line is gain = -17.26 + 24.79 x weeks.
    - (c) For 6 weeks the estimated gain is about 131.5. The slope 24.79 means that each extra week in the program adds about 24.79 to the speed gain on average.

### Practice Questions (Not from Past Papers)

**P1. (Short answer)** What are the mean and the median? Why is the median a better "typical value" than the mean for the daily mobile data use of a phone that had one day of 6200 MB, when all the other days were near 900 MB?

??? success "Model Answer"

    The **mean** is the sum of all values divided by how many there are. The **median** is the middle value after sorting.

    One huge day (an outlier) pulls the mean upwards, so the mean is higher than what a normal day looks like. The median is only the middle value, so one extreme day hardly changes it. For this phone the median (936 MB) describes a normal day better than the mean (1155.1 MB).

**P2. (Predict the output)** What does this program print?

<!-- answer -->
```python
import pandas as pd

marks = pd.Series([4, 8, 6, 5, 7])
print(marks.mean())
print(marks.median())
print(marks.max() - marks.min())
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    6.0
    6.0
    4
    ```

    The five values add up to 30, so the mean is 6.0. Sorted, they are 4, 5, 6, 7, 8, so the middle value is 6.0. The range is the maximum minus the minimum: 8 - 4 = 4.

**P3. (Predict the output)** The same eight numbers are given to NumPy and to Pandas. What does this program print? Why are the two answers different?

<!-- answer -->
```python
import numpy as np
import pandas as pd

values = [2, 4, 4, 4, 5, 5, 7, 9]
print(round(np.std(values), 2))
print(round(pd.Series(values).std(), 2))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    2.0
    2.14
    ```

    Both measure the standard deviation, but they divide by a different number. NumPy's `np.std()` has `ddof=0` and divides by `n` (here 8). Pandas `std()` has `ddof=1` and divides by `n - 1` (here 7). Dividing by the smaller number gives the larger answer. Writing `np.std(values, ddof=1)` makes NumPy match Pandas.

**P4. (Predict the output)** What does this program print?

<!-- answer -->
```python
import pandas as pd

marks = pd.Series([10, 20, 30, 40, 50])
print(marks.quantile([0.25, 0.5, 0.75]))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    0.25    20.0
    0.50    30.0
    0.75    40.0
    dtype: float64
    ```

    The 25th, 50th and 75th percentiles are the three quartiles. The middle one (0.50) is the median. The distance from Q1 to Q3 is the interquartile range: 40 - 20 = 20.

**P5. (Write a program)** The file `cricket.csv` has the columns `player`, `runs` and `balls_faced`. Write a program that adds a column `strike_rate` (runs per 100 balls, rounded to 1 decimal place) and prints the name and strike rate of the batter with the highest strike rate.

??? success "Model Answer"

    ```python
    import pandas as pd

    cricket = pd.read_csv("cricket.csv")
    cricket["strike_rate"] = (cricket["runs"] / cricket["balls_faced"] * 100).round(1)
    best = cricket.sort_values("strike_rate", ascending=False).head(1)
    print(best[["player", "strike_rate"]])
    ```

    ```{ .text .output title="Output" }
      player  strike_rate
    8  Ishan        133.3
    ```

    The new column is calculated for all rows at once. `sort_values(..., ascending=False)` puts the biggest value first, and `head(1)` keeps only the first row.

**P6. (Write a program)** Using `tips.csv`, write a program that prints the average `tip` for lunch and for dinner (column `time`), rounded to 2 decimal places.

??? success "Model Answer"

    ```python
    import pandas as pd

    tips = pd.read_csv("tips.csv")
    print(tips.groupby("time")["tip"].mean().round(2))
    ```

    ```{ .text .output title="Output" }
    time
    Dinner    3.10
    Lunch     2.73
    Name: tip, dtype: float64
    ```

    `groupby("time")` splits the rows into Dinner and Lunch groups, `["tip"]` picks the column, and `mean()` finds the average of each group.

**P7. (Short answer)** Which chart would you choose for each question, and which Matplotlib function draws it? (a) How did the daily sales of a shop change over 30 days? (b) How are the marks of 60 students spread out? (c) Is there a link between hours studied and marks? (d) Which of four product categories sold the most?

??? success "Model Answer"

    (a) A **line plot**, `plt.plot()`, because it shows change over time. (b) A **histogram**, `plt.hist()`, because it shows the shape of one number column. (c) A **scatter plot**, `plt.scatter()`, because it shows the link between two number columns. (d) A **bar chart**, `plt.bar()`, because it compares categories.

**P8. (Short answer)** A box plot of marks shows a box from 58 to 80 with a line inside it at 70, whiskers reaching down to 39 and up to 92, and no dots. Describe what each part tells you.

??? success "Model Answer"

    The line at 70 is the median: half of the students scored below 70. The box runs from Q1 (58) to Q3 (80), so the middle half of the students scored between 58 and 80. The whiskers show the lowest (39) and the highest (92) normal marks. There are no dots, so the data has no outliers.

**P9. (Short answer)** A student draws a histogram of 60 marks with `bins=2` and another with `bins=40`. Why are both histograms poor, and how do you choose a better number?

??? success "Model Answer"

    With `bins=2` the data is squeezed into two wide bars, so the shape (where most values lie, whether there are gaps) is hidden. With `bins=40` each bin holds only one or two values, so the chart breaks into thin spikes and gaps that are just noise. Try a middle value (for example 8 to 15 for a few hundred values) and compare two or three settings before choosing.

**P10. (Predict the output)** What does this program print?

<!-- answer -->
```python
import pandas as pd

df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [2, 4, 6, 8, 10],
    "z": [5, 4, 3, 2, 1],
})
print(df.corr().round(2))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
         x    y    z
    x  1.0  1.0 -1.0
    y  1.0  1.0 -1.0
    z -1.0 -1.0  1.0
    ```

    `y` is always twice `x`, so they move together perfectly: r = 1.0. `z` falls by one each time `x` rises by one, so `x` and `z` move in exactly opposite directions: r = -1.0. Every column has a correlation of 1.0 with itself.

**P11. (Long answer)** Explain covariance and correlation. Why is correlation usually easier to interpret? Then explain, with one example, why "correlation is not causation".

??? success "Model Answer"

    **Covariance** measures whether two columns move together. A positive value means that when one rises the other tends to rise; a negative value means it tends to fall. But its size depends on the units: measuring study time in minutes instead of hours makes the covariance 60 times larger, though the link is the same.

    **Correlation** rescales covariance to a number between -1 and +1 that does not depend on units. Near +1 is a strong positive link, near -1 a strong negative link, and near 0 means no straight-line link. So it is easy to compare different pairs of columns.

    **Correlation is not causation:** two columns can move together because a third factor drives both. For example, ice cream sales and sunburn cases both rise in hot months with a correlation near 0.99, but ice cream does not cause sunburn. The hidden cause is the hot weather.

**P12. (Short answer)** In a table of correlations, `hours_studied` and `marks` have r = 0.94, and `attendance` and `marks` have r = 0.17. What do these two numbers tell you? Does r = 0.94 prove that studying more causes higher marks?

??? success "Model Answer"

    Hours studied has a very strong positive link with marks. Students who study more tend to score more. Attendance has only a weak positive link with marks. r = 0.94 does not by itself prove a cause. It only shows that the two move together. Other factors, such as how keen a student is, could affect both.

## Unit IX: Introduction to Machine Learning with Python

[Back to the Unit IX notes](unit-09-ml.md)

### Past Paper Questions

**Q1.** What is confusion matrix? Discuss various classification measures along with their mathematical formulae.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Data Warehousing and Data Mining (CSC410), 2079 BS, question 9. Marks not shown. [Question bank](https://hamrocsit.com/semester/seventh/data-mining/question-bank/2079).*

??? success "Model Answer (Written for These Notes)"

    A **confusion matrix** is a small table that compares the real answers with the answers a classifier predicted. Take "Pass" as the positive class.

    |  | Predicted Pass | Predicted Fail |
    |---|---|---|
    | **Actual Pass** | TP (true positive) | FN (false negative) |
    | **Actual Fail** | FP (false positive) | TN (true negative) |

    | Measure | Formula | Meaning |
    |---|---|---|
    | Accuracy | (TP + TN) / (TP + TN + FP + FN) | How often the model is right |
    | Error rate | (FP + FN) / (TP + TN + FP + FN) | How often it is wrong |
    | Precision | TP / (TP + FP) | Of those predicted Pass, how many really passed |
    | Recall (sensitivity) | TP / (TP + FN) | Of those who really passed, how many were found |
    | Specificity | TN / (TN + FP) | Of those who really failed, how many were found |
    | F1 score | 2 x precision x recall / (precision + recall) | One number that balances precision and recall |

    ```python
    from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score

    actual = ["Pass", "Pass", "Pass", "Fail", "Fail", "Pass", "Fail", "Pass"]
    predicted = ["Pass", "Fail", "Pass", "Fail", "Pass", "Pass", "Fail", "Pass"]
    print(confusion_matrix(actual, predicted, labels=["Pass", "Fail"]))
    print("accuracy:", accuracy_score(actual, predicted))
    print("precision:", round(precision_score(actual, predicted, pos_label="Pass"), 2))
    print("recall:", round(recall_score(actual, predicted, pos_label="Pass"), 2))
    print("f1:", round(f1_score(actual, predicted, pos_label="Pass"), 2))
    ```

    ```{ .text .output title="Output" }
    [[4 1]
     [1 2]]
    accuracy: 0.75
    precision: 0.8
    recall: 0.8
    f1: 0.8
    ```

    Rows are the actual classes and columns are the predicted classes, in the order Pass, Fail.

**Q2.** Apply K(=2)- Means algorithm over the data (185, 72), (170, 56), (168, 60), (179, 68), (182, 72), (188, 77) up to two iterations and show the clusters. Initially choose first two objects as initial centroids.

*Source: Tribhuvan University, Institute of Science and Technology, BSc CSIT, Data Warehousing and Data Mining (CSC410), 2078 BS, Section B. Marks not shown. [Question bank](https://hamrocsit.com/semester/seventh/data-mining/question-bank/2078).*

??? success "Model Answer (Written for These Notes)"

    K-means steps: (1) pick the starting centroids; (2) give every point to its nearest centroid by straight-line (Euclidean) distance; (3) move each centroid to the mean of its points; (4) repeat. Here the centroids start at the first two points, (185, 72) and (170, 56).

    ```python
    import numpy as np

    points = np.array([[185, 72], [170, 56], [168, 60], [179, 68], [182, 72], [188, 77]])
    centroids = points[:2].astype(float)

    for iteration in (1, 2):
        # distance of every point to every centroid
        distances = np.linalg.norm(points[:, None] - centroids, axis=2)
        labels = distances.argmin(axis=1)
        centroids = np.array([points[labels == k].mean(axis=0) for k in range(2)])
        print("Iteration", iteration)
        print("  cluster of each point:", labels.tolist())
        print("  new centroids:", centroids.round(2).tolist())
    ```

    ```{ .text .output title="Output" }
    Iteration 1
      cluster of each point: [0, 1, 1, 0, 0, 0]
      new centroids: [[183.5, 72.25], [169.0, 58.0]]
    Iteration 2
      cluster of each point: [0, 1, 1, 0, 0, 0]
      new centroids: [[183.5, 72.25], [169.0, 58.0]]
    ```

    Cluster 0 holds the taller, heavier people. Cluster 1 holds the others. The clusters did not change in the second iteration, so the algorithm has finished.

### Practice Questions (Not from Past Papers)

**P1. (Short answer)** What is machine learning? How is it different from an ordinary program in which the programmer writes the rules?

??? success "Model Answer"

    Machine learning means letting a computer learn a pattern from example data instead of being given the rules. In an ordinary program the programmer supplies the rules and the data, and the program gives answers. In machine learning we supply the data and the known answers, and the computer works out the rules. The learned pattern is stored in a **model**, which can then predict for new data.

**P2. (Short answer)** Define **feature** and **label**. For predicting a student's marks from `study_marks.csv`, name two features and the label.

??? success "Model Answer"

    A feature is an input column that the model looks at. The label (target) is the answer column that we want to predict. To predict marks, the features are `hours_studied` and `attendance`, and the label is `marks`.

**P3. (Short answer)** Explain the difference between supervised and unsupervised learning. Give one everyday example of each.

??? success "Model Answer"

    In supervised learning the training data has a label column, so the model learns from examples with known answers. Example: predicting Pass or Fail from hours studied. In unsupervised learning there is no label, and the model finds structure in the data by itself. Example: grouping shop customers by how often they visit and how much they spend.

**P4. (Short answer)** Name the three kinds of task in this unit. For each, say what comes out of the model and give one example.

??? success "Model Answer"

    | Task | What comes out | Example |
    |---|---|---|
    | Regression | a number | predicting marks from hours studied |
    | Classification | a category (class) | predicting Pass or Fail |
    | Clustering | a group number | grouping shop customers into three groups |

    Regression and classification are supervised. Clustering is unsupervised.

**P5. (Predict the output)** What does this program print?

<!-- answer -->
```python
import pandas as pd
from sklearn.linear_model import LinearRegression

X = pd.DataFrame({"hours": [1, 2, 3, 4]})
y = [10, 20, 30, 40]

model = LinearRegression()
model.fit(X, y)

new_student = pd.DataFrame({"hours": [6]})
print(round(model.predict(new_student)[0], 1))
print(round(model.coef_[0], 1))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    60.0
    10.0
    ```

    The marks go up by 10 for every extra hour, so the line is `marks = 0 + 10 * hours`. For 6 hours the model predicts 60. The slope (`coef_[0]`) is 10.

**P6. (Predict the output)** What does this program print? Which points does K-means put in the same cluster?

<!-- answer -->
```python
import pandas as pd
from sklearn.cluster import KMeans

points = pd.DataFrame({"x": [1, 2, 10, 11], "y": [1, 1, 10, 10]})

model = KMeans(n_clusters=2, n_init=10, random_state=42)
model.fit(points)
print(model.labels_)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    [0 0 1 1]
    ```

    The first two points are close together, so they share one label. The last two points are close together, so they share the other label. Which number (0 or 1) goes to which group is arbitrary; only the grouping matters.

**P7. (Short answer)** Why do we split data into a training set and a test set? What do `test_size=0.2` and `random_state=42` do in `train_test_split`?

??? success "Model Answer"

    A model must be judged on data it has never seen. The training set is used by `fit`, and the test set is kept hidden and used only to measure the model. `test_size=0.2` keeps 20% of the rows for testing. `random_state=42` fixes the random shuffle, so the same split is produced every time.

**P8. (Predict the output)** What does this program print? How many predictions were correct?

<!-- answer -->
```python
from sklearn.metrics import accuracy_score, confusion_matrix

actual    = ["Pass", "Fail", "Pass", "Pass", "Fail", "Pass"]
predicted = ["Pass", "Fail", "Fail", "Pass", "Fail", "Pass"]

print(confusion_matrix(actual, predicted, labels=["Pass", "Fail"]))
print(round(accuracy_score(actual, predicted), 2))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    [[3 1]
     [0 2]]
    0.83
    ```

    Rows are the actual classes and columns are the predicted classes, in the order Pass, Fail. The correct answers are on the diagonal: 3 passes and 2 fails, so 5 of 6 are correct and the accuracy is 5 / 6 = 0.83. The single mistake is a student who really passed but was predicted to fail.

**P9. (Short answer)** A model scores 100% on its training data but only 70% on the test data. What has probably happened? Which score should you trust?

??? success "Model Answer"

    The model has memorised the training examples instead of learning the pattern, so it does badly on new data. You should trust the test score (70%), because it measures the model on data it has never seen.

**P10. (Short answer)** A student writes `model.fit(students["hours_studied"], students["marks"])` and scikit-learn raises a `ValueError`. Why does it fail, and how is it fixed?

??? success "Model Answer"

    `students["hours_studied"]` is a single column (a Series). Scikit-learn expects the features `X` to be a 2D table, even when there is only one feature. Use two pairs of brackets: `students[["hours_studied"]]`.

**P11. (Short answer)** Name one score used for regression and one used for classification. Say what each one tells you.

??? success "Model Answer"

    For regression, R-squared tells how much of the pattern in the label the model explains (1 is perfect, near 0 is no better than guessing the average). Mean absolute error tells the average size of the mistakes, in the unit of the label. For classification, accuracy is the share of predictions that are correct. The confusion matrix shows how many right and wrong answers there are for each class. Both kinds of score should be computed on the test data.

**P12. (Write a program)** Using `study_marks.csv`, build a model that predicts `result` (Pass or Fail) from `hours_studied` and `attendance`. Use an 80/20 split with `random_state=42` and print the accuracy on the test data.

??? success "Model Answer"

    ```python
    import pandas as pd
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split

    students = pd.read_csv("study_marks.csv")
    X = students[["hours_studied", "attendance"]]
    y = students["result"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)

    print("Accuracy:", round(accuracy_score(y_test, predicted), 2))
    ```

    ```{ .text .output title="Output" }
    Accuracy: 0.83
    ```

**P13. (Write a program)** Using `shop_customers.csv`, group the customers into 3 clusters with K-means (`random_state=42`) and print how many customers are in each cluster.

??? success "Model Answer"

    ```python
    import pandas as pd
    from sklearn.cluster import KMeans

    customers = pd.read_csv("shop_customers.csv")
    X = customers[["monthly_visits", "monthly_spend"]]

    model = KMeans(n_clusters=3, n_init=10, random_state=42)
    model.fit(X)

    customers["cluster"] = model.labels_
    print(customers["cluster"].value_counts().sort_index())
    ```

    ```{ .text .output title="Output" }
    cluster
    0    30
    1    30
    2    30
    Name: count, dtype: int64
    ```

**P14. (Long answer)** Describe the steps of building a machine learning model with scikit-learn. Use the example of predicting marks from hours studied.

??? success "Model Answer"

    1. State the task. Predicting marks (a number) is a regression task.
    2. Load the data with `pd.read_csv("study_marks.csv")` and look at it.
    3. Choose the features and the label: `X = students[["hours_studied"]]` (a table) and `y = students["marks"]`.
    4. Split the data with `train_test_split(X, y, test_size=0.2, random_state=42)`, so that 20% of the rows are kept for testing.
    5. Choose a model, `model = LinearRegression()`, and train it on the training rows only: `model.fit(X_train, y_train)`.
    6. Predict the test rows with `model.predict(X_test)`.
    7. Evaluate on the test data with R-squared (`r2_score`) and mean absolute error (`mean_absolute_error`).
    8. Use the model on new students with `model.predict(new_students)`. The new data must have the same columns as the training data.

## Unit X: Data Visualization and Reporting

[Back to the Unit X notes](unit-10-visualization.md)

### Past Paper Questions

No past-paper question for this unit was found.

### Practice Questions (Not from Past Papers)

**P1. (Short answer)** What does a heatmap show? How do you read the colours in a correlation heatmap drawn with `cmap="coolwarm"`, and why do we set `vmin=-1` and `vmax=1`?

??? success "Model Answer"

    A heatmap is a grid in which the colour of each cell shows a number, so you can spot big and small values at a glance. In a correlation heatmap, red cells are positive correlations (the deeper, the stronger), blue cells are negative correlations, and the middle colour means almost no link. The diagonal is always 1 because a column matches itself. `vmin=-1` and `vmax=1` fix the colour scale to the full range of a correlation, so the middle colour always means zero and the same colour always means the same number.

**P2. (Predict the output)** A heatmap needs a grid, which a pivot table gives. What does this program print?

<!-- answer -->
```python
import pandas as pd

sales = pd.DataFrame({
    "category": ["Grocery", "Grocery", "Stationery", "Stationery", "Grocery"],
    "weekday": ["Mon", "Tue", "Mon", "Tue", "Mon"],
    "amount": [500, 300, 120, 80, 200],
})
print(sales.pivot_table(index="category", columns="weekday", values="amount", aggfunc="sum"))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    weekday     Mon  Tue
    category            
    Grocery     700  300
    Stationery  120   80
    ```

    The rows are the categories and the columns are the weekdays. Each cell is the sum of the amounts for that pair. Grocery on Monday has two sales, 500 and 200, so the cell shows 700.

**P3. (Short answer)** What is a pair plot? The iris dataset has four number columns and three species. How many panels does `sns.pairplot(flowers, hue="species")` draw, and what do the panels on the diagonal show?

??? success "Model Answer"

    A pair plot is a grid that draws a scatter plot for every pair of number columns. With four columns the grid is 4 by 4, so it has 16 panels. Twelve are scatter plots (each pair appears twice, with the axes swapped). The four panels on the diagonal cannot be scatter plots, so they show how each single column is spread out. `hue="species"` colours the points by species, so you can see which measurements separate the three species.

**P4. (Short answer)** What does it mean for a plot to be interactive? Name three things the reader can do. How does `fig.show()` behave in a Jupyter notebook and in a Python script?

??? success "Model Answer"

    An interactive plot reacts to the mouse. The reader can hover over a point to see its values, zoom into a region by dragging a box, pan to move the view, or click a legend item to hide and show a group. In a Jupyter notebook or Colab, `fig.show()` shows the plot under the cell. In a Python script, it opens the plot as a web page in the default browser.

**P5. (Write a program)** Using `tips.csv` and Plotly Express, write a program that builds a bar chart of the average `total_bill` for each `day`. Give it a title. Print the averages, rounded to 1 decimal place, before showing the chart.

??? success "Model Answer"

    ```python
    import pandas as pd
    import plotly.express as px

    tips = pd.read_csv("tips.csv")
    average = tips.groupby("day", as_index=False)["total_bill"].mean().round(1)
    print(average)

    fig = px.bar(average, x="day", y="total_bill", title="Average Bill by Day")
    fig.show()
    ```

    ```{ .text .output title="Output" }
        day  total_bill
    0   Fri        17.2
    1   Sat        20.4
    2   Sun        21.4
    3  Thur        17.7
    ```

    `px.bar()` needs a table and the names of the columns for `x` and `y`. `as_index=False` keeps `day` as an ordinary column, so Plotly can use it.

**P6. (Short answer)** A Dash app has two parts. Name them and say what each does. In `@callback(Output("graph", "figure"), Input("menu", "value"))`, which is the input and which is the output?

??? success "Model Answer"

    The **layout** is what the user sees: the heading, the menu and the graph. The **callback** is a Python function that runs when the user changes something, and it updates part of the page. Here the input is the `value` of the component with id `menu` (the user's choice), and the output is the `figure` of the component with id `graph`, which gets whatever the function returns.

**P7. (Write a program)** Write a complete Dash app (`app.py`) that shows a histogram of `total_bill` from `tips.csv` and a dropdown that lets the user choose a day (`Thur`, `Fri`, `Sat`, `Sun`). The histogram must show only the chosen day. Use port 8064.

??? success "Model Answer"

    <!-- serve: 8; script: app.py -->
    ```python
    import pandas as pd
    import plotly.express as px
    from dash import Dash, dcc, html, Input, Output, callback

    tips = pd.read_csv("tips.csv")

    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Bills by Day"),
        dcc.Dropdown(
            id="day-menu",
            options=["Thur", "Fri", "Sat", "Sun"],
            value="Sat",
            clearable=False,
        ),
        dcc.Graph(id="bill-histogram"),
    ])


    @callback(
        Output("bill-histogram", "figure"),
        Input("day-menu", "value"),
    )
    def update_histogram(day):
        one_day = tips[tips["day"] == day]
        return px.histogram(one_day, x="total_bill", title=f"Bills on {day}")


    if __name__ == "__main__":
        app.run(port=8064, debug=True)
    ```

    ```{ .text .output title="Output" }
    Dash is running on http://127.0.0.1:8064/

     * Serving Flask app 'app'
     * Debug mode: on
    ```

    The ids `day-menu` and `bill-histogram` are written exactly the same in the layout and in the callback. The function's argument receives the chosen day.

**P8. (Short answer)** A student's Dash page opens, but the graph stays empty and an error panel says "ID not found in layout". What is the most likely cause, and how do you fix it?

??? success "Model Answer"

    The `id` used in the callback (in `Input(...)` or `Output(...)`) does not match any `id` in the layout. It is usually a spelling mistake, for example `day-dropdwon` instead of `day-dropdown`. Compare every id in the callback with the layout and correct the spelling so that they match exactly.

**P9. (Short answer)** How do you start a Dash app saved as `app.py` that uses `port=8061`, which address do you open in the browser, and how do you stop the app?

??? success "Model Answer"

    Open a terminal in the folder with `app.py` and the data file and run `python app.py`. Then open `http://127.0.0.1:8061/` in a web browser. (`127.0.0.1` means "this computer".) To stop the app, go back to the terminal and press `Ctrl+C`.

**P10. (Long answer)** A chart has the title "Sales", no axis labels, nine bars in nine different colours, and the months in alphabetical order. List the five rules for presenting data effectively and use them to say how you would improve this chart.

??? success "Model Answer"

    The five rules are: (1) one message per chart, (2) a title that states the finding, (3) labelled axes with units, (4) the right chart for the question, (5) meaningful colours.

    Improvements: put the months in calendar order (a line plot over time may suit the question better than bars). Change the title from "Sales" to a finding, such as "Sales Doubled Between June and September". Label the axes ("Month", "Sales (Rs.)"). Use one colour for all bars, and use a different colour only to mark something meaningful, such as the best month. Show only the one message the reader should remember.

**P11. (Long answer)** A school wants a small dashboard for the class marks table. Describe its layout and its callback: which controls and graphs would you place, what is the input and what is the output?

??? success "Model Answer"

    **Layout:** a heading ("Class Marks Dashboard"), a dropdown with the three subjects (Maths, Science, English), and a graph.

    **Callback:** the input is the `value` of the dropdown (the chosen subject). The callback function takes the chosen subject, builds a histogram or a bar chart of that subject's marks with a title and axis labels, and returns the figure. The output is the `figure` of the graph. Whenever the teacher picks another subject, Dash runs the callback again and the graph updates.

## Unit XI: Practical Lab Work

[Back to the Unit XI notes](unit-11-lab.md)

### Past Paper Questions

No past-paper question for this unit was found.

### Practice Questions (Not from Past Papers)

**P1. (Short answer)** You load a new CSV file into pandas. What three checks do you make before any analysis, and why?

??? success "Model Answer"

    Look at the size with `df.shape`, look at the first rows with `df.head()`, and count the missing values and duplicate rows with `df.isna().sum()` and `df.duplicated().sum()`. The size and first rows show what the table looks like. The counts show how much cleaning is needed. Skipping this step means wrong results later.

**P2. (Short answer)** In the file `students_raw.csv`, one student has `math` equal to 880. How do you find such an outlier with the IQR rule, and why is the median a better fill value than the mean?

??? success "Model Answer"

    Work out `Q1` and `Q3` (the 25% and 75% points) and `IQR = Q3 - Q1`. A value above `Q3 + 1.5 x IQR` is an outlier. The mean is pulled towards the outlier, so it gives a wrong "typical" mark. The median is the middle value and does not move when one value is huge.

**P3. (Short answer)** Why do we score a model on the test set and not on the training set?

??? success "Model Answer"

    The model has already seen the training rows, so a good score on them only shows that it remembered them. The test rows are new. The score on them shows how the model will work on data it has never seen.

**P4. (Short answer)** In the shop customers project, why did the clustering model not need a target column? How did you decide what to call each group?

??? success "Model Answer"

    Clustering is unsupervised. It finds groups by itself from the input columns, so there is no correct answer to learn from. The group numbers are only labels. You name a group by reading its average visits and average spend, for example "occasional shoppers" for low visits and low spend.

**P5. (Short answer)** In a Dash app, what do the layout and the callback do? Where does the result appear when you run `python app.py`?

??? success "Model Answer"

    The layout says what the page contains, such as a heading, a dropdown and graphs. The callback is a function that runs when the viewer changes an input, such as the dropdown. It builds new figures that replace the old ones. The terminal only prints a start-up message and keeps running. The dashboard itself appears in the browser at the address shown, for example `http://127.0.0.1:8050/`.

**P6. (Predict the output)** What does this program print?

<!-- answer -->
```python
data = [4, 0, 7, -1, 5, 9]
total = 0
for x in data:
    if x == 0:
        continue
    if x < 0:
        break
    total = total + x
print(total)
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    11
    ```

    `4` is added. `0` is skipped by `continue`. `7` is added. `-1` makes the loop stop with `break`, so `5` and `9` are never added. The total is `4 + 7 = 11`.

**P7. (Predict the output)** What does this program print?

<!-- answer -->
```python
sold = ["Pen", "Tea", "Pen", "Pen", "Tea"]
counts = {}
for item in sold:
    counts[item] = counts.get(item, 0) + 1
print(counts)
print(max(counts, key=counts.get))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    {'Pen': 3, 'Tea': 2}
    Pen
    ```

    `counts.get(item, 0)` gives the count so far, or 0 for a new item. The loop adds 1 each time. `max(counts, key=counts.get)` returns the key with the biggest value.

**P8. (Write a program)** Read `students.csv` with the `csv` module and print the name and attendance of every student whose attendance is below 75. Print a message instead of crashing if the file is missing.

??? success "Model Answer"

    ```python
    import csv

    try:
        with open("students.csv", newline="") as f:
            rows = list(csv.DictReader(f))
    except FileNotFoundError:
        print("students.csv was not found")
        rows = []

    for row in rows:
        if int(row["attendance"]) < 75:
            print(row["name"], row["attendance"])
    ```

    ```{ .text .output title="Output" }
    Dipesh 70
    Jiwan 65
    ```

    The `int()` is needed because the `csv` module gives every value as text.

**P9. (Write a program)** Using `shop_sales.csv`, add a `total` column (`quantity` times `price`), then print the total sales of each category and the category with the highest total.

??? success "Model Answer"

    ```python
    import pandas as pd

    sales = pd.read_csv("shop_sales.csv")
    sales["total"] = sales["quantity"] * sales["price"]

    by_category = sales.groupby("category")["total"].sum()
    print(by_category)
    print("Highest:", by_category.idxmax())
    ```

    ```{ .text .output title="Output" }
    category
    Grocery       15060
    Household      2085
    Stationery     2775
    Name: total, dtype: int64
    Highest: Grocery
    ```

**P10. (Long answer)** You are given `tips.csv` and asked to take it from the raw file to three findings. Describe the stages you follow, and say what makes a good finding.

??? success "Model Answer"

    1. **Load.** Read the file with `pd.read_csv()` and look at its shape and first rows.
    2. **Clean.** Count missing values and duplicates. Drop the duplicates, fill or remove missing values, handle outliers, and fix wrong types.
    3. **Explore.** Work out statistics such as the mean and group averages with `groupby`. Check a correlation.
    4. **Model or chart.** Draw one clear chart with a title and labelled axes, or fit one model and print its score.
    5. **Present.** Write three findings.

    A good finding is one plain sentence with a number from the data, for example "The average tip is between 15 and 17 percent of the bill on every day of the week." It should be checked against the output, not guessed.
