# Lab Sheets

These are the ten practical activities of the course. Each lab sheet is one sitting at the computer, about 30 to 45 minutes. The order follows the units: Lab 1 goes with Unit I, Lab 2 with Unit II, and so on up to Lab 10 with Unit X. Unit XI, [Practical Lab Work](unit-11-lab.md), then uses all ten skills together in bigger tasks.

!!! abstract "How to Use a Lab Sheet"

    1. Read the **Objective**. It tells you what you will be able to do at the end.
    2. Check **What You Need**. Open the data file or the earlier unit if the sheet asks for it.
    3. Follow the **Steps** in order, at the computer.
    4. Type the **Starter Code** yourself. Do not only copy it. Run it and compare your result with the **Output** block under it. They should match.
    5. Do **Your Turn** on your own first. Open the solution only after you have tried.
    6. Tick every box in **Check Yourself**. If you cannot tick one, repeat that part.

The data files used by the labs (`students.csv`, `tips.csv` and the others) are listed, with a download link, in [Practice Data Files](setup.md#practice-data-files). Save them in the same folder as your script or notebook. Then `pd.read_csv("students.csv")` works without a folder path. In Google Colab, upload the file first, as shown in [Using the Practice Data Files in Colab](setup.md#using-the-practice-data-files-in-colab).

| Lab | Syllabus activity | Unit |
|---|---|---|
| [Lab 1](#lab-1-set-up-python-and-run-a-first-script) | Set up Python environment (Anaconda, Jupyter, Colab) and run first script. | [Unit I](unit-01-intro.md) |
| [Lab 2](#lab-2-variables-data-types-and-operators) | Work with variables, data types, and operators in small programs. | [Unit II](unit-02-basics.md) |
| [Lab 3](#lab-3-conditions-loops-break-and-continue) | Use if, for, while statements; apply break and continue. | [Unit III](unit-03-control.md) |
| [Lab 4](#lab-4-functions-and-modules) | Write functions, use parameters/return values, and import modules. | [Unit IV](unit-04-functions.md) |
| [Lab 5](#lab-5-lists-tuples-sets-and-dictionaries) | Manipulate lists, tuples, sets, and dictionaries with operations and methods. | [Unit V](unit-05-structures.md) |
| [Lab 6](#lab-6-files-csv-json-and-exceptions) | Read/write files (CSV, JSON) and handle exceptions using try-except. | [Unit VI](unit-06-files.md) |
| [Lab 7](#lab-7-import-and-clean-a-dataset) | Import datasets, handle missing values, duplicates, outliers; transform data. | [Unit VII](unit-07-cleaning.md) |
| [Lab 8](#lab-8-descriptive-statistics-and-visualization) | Perform descriptive statistics and visualize data with Matplotlib/Seaborn. | [Unit VIII](unit-08-eda.md) |
| [Lab 9](#lab-9-build-machine-learning-models-with-scikit-learn) | Build ML models (regression, classification, clustering) using Scikit-learn. | [Unit IX](unit-09-ml.md) |
| [Lab 10](#lab-10-dashboards-and-interactive-plots-with-plotly-dash) | Create dashboards and interactive plots with Plotly Dash or Streamlit. | [Unit X](unit-10-visualization.md) |

## Lab 1: Set Up Python and Run a First Script

### Objective

Get a working Python on your computer, or in the browser, and run your first **script**. A script is a text file of Python lines that Python runs from top to bottom.

### What You Need

- A computer with internet for the first setup. [Setting Up Python](setup.md) shows two ways: **Anaconda** (a free bundle of Python, data tools and Jupyter) or **Google Colab** (Jupyter in the browser, with nothing to install). **Jupyter Notebook** is a page where you run code in small cells.
- Background: [Unit I](unit-01-intro.md).

### Steps

1. Set up one tool. On your computer, follow [Option 1: Anaconda](setup.md#option-1-anaconda-on-your-computer) and then [Opening Jupyter Notebook](setup.md#opening-jupyter-notebook). In a browser, follow [Option 2: Google Colab](setup.md#option-2-google-colab).
2. Make a new folder called `lab1`. Create a file named `hello.py` inside it, as shown in [Running a Script From the Terminal](setup.md#running-a-script-from-the-terminal). In Jupyter or Colab, open a new notebook instead.
3. Type the starter code below.
4. Run it. In a terminal, type `python hello.py`. In Jupyter or Colab, press `Shift+Enter` on the cell.
5. Compare what you see with the Output block. Your version numbers may be different. That is fine.
6. Run the full library check in [Checking Your Setup](setup.md#checking-your-setup) once, so you know every library is ready for the later labs.

### Starter Code

Run it. Your first line must read exactly the same as the Output block.

```python
import platform
import pandas as pd

print("Hello, Data Science!")
print("Python version:", platform.python_version())
print("pandas version:", pd.__version__)
```

```{ .text .output title="Output" }
Hello, Data Science!
Python version: 3.12.3
pandas version: 3.0.6
```

If the third line fails with `ModuleNotFoundError: No module named 'pandas'`, your Python does not have pandas yet. Anaconda and Colab already have it. See [Installing Extra Libraries](setup.md#installing-extra-libraries).

### Your Turn

1. Print your own name and your college on two separate lines.
2. Add one more version check, for `numpy`, the number library. Import it as `np` and print `np.__version__`.

??? success "Solution"

    ```python
    import numpy as np

    print("Name: Asha Gurung")
    print("College: Pokhara University")
    print("numpy version:", np.__version__)
    ```

    ```{ .text .output title="Output" }
    Name: Asha Gurung
    College: Pokhara University
    numpy version: 2.5.3
    ```

### Check Yourself

- [ ] I have one working tool: Anaconda, Jupyter or Colab.
- [ ] I ran a script or a cell and saw the output.
- [ ] I can say what a script is.
- [ ] I know how to read the version of a library.

## Lab 2: Variables, Data Types and Operators

### Objective

Store values in variables, see their data types, and use operators in a small calculator program. You also use `input()` to ask the user for a value.

### What You Need

- Python from Lab 1. No data file.
- Background: [Unit II](unit-02-basics.md).

### Steps

1. Open a new file called `percentage.py` or a new notebook.
2. Type the starter code. It asks for a name, the marks obtained and the full marks.
3. Run it and type the values shown in the Output block. When you run it yourself, type your own values.
4. Look at the output line that shows `type(...)`. Notice that `int()` turned the typed text into a number.
5. Do the two tasks in Your Turn.

### Starter Code

The values after each prompt in the Output block (`Asha`, `342`, `400`) are what was typed in.

<!-- stdin: Asha | 342 | 400 -->
```python
name = input("Student name: ")
obtained = int(input("Marks obtained: "))
full = int(input("Full marks: "))

percentage = obtained / full * 100

print(name, "scored", round(percentage, 1), "percent")
print("Type of obtained:", type(obtained))
print("Passed:", percentage >= 45)
```

```{ .text .output title="Output" }
Student name: Asha
Marks obtained: 342
Full marks: 400
Asha scored 85.5 percent
Type of obtained: <class 'int'>
Passed: True
```

### Your Turn

1. Write a **bill calculator**. Ask for an item name, its price in Rs. and the quantity. Print the subtotal, a 13 percent tax and the final total.
2. A trip took 135 minutes. Use `//` and `%` to print it as hours and minutes.

??? success "Solution"

    <!-- stdin: Notebook | 60 | 5 -->
    ```python
    item = input("Item: ")
    price = float(input("Price in Rs.: "))
    quantity = int(input("Quantity: "))

    subtotal = price * quantity
    tax = subtotal * 0.13
    total = subtotal + tax

    print("Subtotal: Rs.", subtotal)
    print("Tax: Rs.", round(tax, 2))
    print("Total for", quantity, item, "= Rs.", round(total, 2))
    ```

    ```{ .text .output title="Output" }
    Item: Notebook
    Price in Rs.: 60
    Quantity: 5
    Subtotal: Rs. 300.0
    Tax: Rs. 39.0
    Total for 5 Notebook = Rs. 339.0
    ```

    `//` gives the whole part of a division. `%` gives what is left over.

    ```python
    minutes = 135
    hours = minutes // 60
    left = minutes % 60
    print(hours, "hours", left, "minutes")
    ```

    ```{ .text .output title="Output" }
    2 hours 15 minutes
    ```

### Check Yourself

- [ ] I can name the data type of a value using `type()`.
- [ ] I know why `input()` needs `int()` or `float()` around it for numbers.
- [ ] I can use `/`, `//`, `%` and `*` and say what each one gives.
- [ ] I can write a comparison like `percentage >= 45` and see `True` or `False`.

## Lab 3: Conditions, Loops, Break and Continue

### Objective

Write a grade report with `if`, `elif` and `else` inside a `for` loop. Then use `continue` to skip a value and `break` to stop a `while` loop early.

### What You Need

- The maths marks of the ten students in `students.csv`, typed into the program as a list. No file is read in this lab.
- Background: [Unit III](unit-03-control.md).

### Steps

1. Open a new file `grades.py`.
2. Type the list of ten marks. These are the `math` column of `students.csv`.
3. Write the `for` loop. Inside it, use `if`, `elif` and `else` to set the grade.
4. Count how many students passed (45 or more). Print the count after the loop.
5. Run it and compare. Then do Your Turn, which adds `continue` and `break`.

### Starter Code

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

### Your Turn

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

### Check Yourself

- [ ] My grade report prints one line for each of the ten students.
- [ ] I can explain why the order of `if`, `elif` and `else` matters.
- [ ] I can say the difference between `break` and `continue`.
- [ ] I changed the variable inside my `while` loop so that it ends.

## Lab 4: Functions and Modules

### Objective

Write your own functions with parameters and return values, put them in a small **module** of your own, and **import** them. A module is a Python file whose functions other programs can reuse. You also use the built-in `math` and `statistics` modules.

### What You Need

- Two files in one folder: `helpers.py` (your module) and `lab4.py` (the program that imports it).
- Background: [Unit IV](unit-04-functions.md).

### Steps

1. Create `helpers.py` and type the two functions below. Save it.
2. Create `lab4.py` in the same folder. The file names must match the `import` line.
3. In `lab4.py`, import `math`, `statistics` and `helpers`.
4. Call `helpers.grade()` for each mark. Notice that it **returns** the grade instead of printing it.
5. Run `lab4.py` and compare the output.

### Starter Code

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

### Your Turn

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

### Check Yourself

- [ ] My function uses `return`, and I used its result in a `print()`.
- [ ] I can say what a default parameter is, and I used one.
- [ ] My own module `helpers.py` imports without an error.
- [ ] I used at least one function from `math` and one from `statistics`.

## Lab 5: Lists, Tuples, Sets and Dictionaries

### Objective

Build a mini student register. You use a **list** (an ordered collection you can change), a **tuple** (an ordered collection you cannot change), a **set** (a collection of unique items) and a **dictionary** (pairs of a key and a value).

### What You Need

- No data file. All data is typed in.
- Background: [Unit V](unit-05-structures.md).

### Steps

1. Open a new file `register.py`.
2. Make the list of names, then use `append()` and `sort()` on it.
3. Make the tuple of subjects. Read its first item.
4. Make the dictionary of marks. Change one value and loop over it with `.items()`.
5. Make the two sets of club members. Use `&` and `|` on them.
6. Run it and compare with the Output block.

### Starter Code

```python
names = ["Asha", "Bikash", "Chandra"]          # list
names.append("Dipesh")
names.sort(reverse=True)
print("Names:", names)

subjects = ("Maths", "Science", "English")      # tuple
print("First subject:", subjects[0], "| count:", len(subjects))

marks = {"Asha": 78, "Bikash": 64, "Chandra": 92, "Dipesh": 45}   # dictionary
marks["Bikash"] = 66
for name, m in marks.items():
    print(name, m)
print("Class average:", sum(marks.values()) / len(marks))

sports = {"Asha", "Chandra", "Dipesh"}          # sets
music = {"Bikash", "Chandra"}
print("In both clubs:", sorted(sports & music))
print("In any club:", sorted(sports | music))
```

```{ .text .output title="Output" }
Names: ['Dipesh', 'Chandra', 'Bikash', 'Asha']
First subject: Maths | count: 3
Asha 78
Bikash 66
Chandra 92
Dipesh 45
Class average: 70.25
In both clubs: ['Chandra']
In any club: ['Asha', 'Bikash', 'Chandra', 'Dipesh']
```

Sets have no fixed order. That is why the program prints `sorted(...)` of each set, so you see the same order every time.

### Your Turn

1. Add a student `"Elina"` with 88 marks. Remove `"Dipesh"` with `pop()`. Print the name of the top scorer with `max(marks, key=marks.get)`.
2. Print the students who are in `sports` but not in `music`.

??? success "Solution"

    ```python
    marks = {"Asha": 78, "Bikash": 66, "Chandra": 92, "Dipesh": 45}

    marks["Elina"] = 88
    removed = marks.pop("Dipesh")
    print("Removed marks:", removed)
    print("Register:", marks)
    print("Top scorer:", max(marks, key=marks.get))
    ```

    ```{ .text .output title="Output" }
    Removed marks: 45
    Register: {'Asha': 78, 'Bikash': 66, 'Chandra': 92, 'Elina': 88}
    Top scorer: Chandra
    ```

    ```python
    sports = {"Asha", "Chandra", "Dipesh"}
    music = {"Bikash", "Chandra"}

    print("Sports only:", sorted(sports - music))
    ```

    ```{ .text .output title="Output" }
    Sports only: ['Asha', 'Dipesh']
    ```

### Check Yourself

- [ ] I can say which of the four structures can be changed and which cannot.
- [ ] I read and changed a dictionary value by its key.
- [ ] I used `.items()` to loop over a dictionary.
- [ ] I can say what `&` and `|` do on sets.

## Lab 6: Files, CSV, JSON and Exceptions

### Objective

Read a **CSV file** (a plain-text table, with commas between the values), save data as a **JSON file** (a plain-text format of keys and values, like a dictionary), and use `try` and `except` so that a missing file does not crash the program.

### What You Need

- `students.csv` in your folder ([Practice Data Files](setup.md#practice-data-files)).
- Libraries: `csv` and `json`. Both come with Python.
- Background: [Unit VI](unit-06-files.md).

### Steps

1. Open a new file `files.py`. Check that `students.csv` is in the same folder.
2. Read the file with `csv.DictReader` inside a `try` block. Handle `FileNotFoundError`.
3. Build a dictionary of name and maths marks. The CSV gives text, so convert each mark with `int()`.
4. Save the dictionary to `math_marks.json` with `json.dump()`. Read it back with `json.load()`.
5. Try to open a file that does not exist, and see the `except` message instead of a crash.

### Starter Code

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

### Your Turn

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

### Check Yourself

- [ ] I used `with open(...)`, so my files close by themselves.
- [ ] I know why `int()` was needed after reading from a CSV.
- [ ] I wrote a JSON file and read it back.
- [ ] My program printed a friendly message instead of a crash when a file was missing.

## Lab 7: Import and Clean a Dataset

### Objective

Load a messy dataset with **pandas** and clean it: find and fill missing values, drop duplicate rows, fix an impossible value (an **outlier**), and change text columns into proper numbers and dates.

### What You Need

- `students_raw.csv` ([Practice Data Files](setup.md#practice-data-files)). It has real-world mess on purpose: two missing values, one duplicate row, one mark of 880, `attendance` stored as text like `92%`, and `gender` in mixed case.
- Library: `pandas`.
- Background: [Unit VII](unit-07-cleaning.md).

### Steps

1. Open a new file or notebook. Load `students_raw.csv`.
2. Count the missing values and the duplicate rows before you change anything.
3. Drop the duplicate rows.
4. Fill the missing marks with the **median** (the middle value) of their column.
5. Treat any maths mark above 100 as wrong: make it missing, then fill it with the median too.
6. Make `gender` upper case, turn `attendance` into a number and `joined` into a date.
7. Print the cleaned table and compare.

### Starter Code

```python
import pandas as pd

df = pd.read_csv("students_raw.csv")
print("Rows at start:", len(df))
print("Missing values:", df.isna().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()
# Keep a maths mark only if it is 100 or less. Otherwise it becomes missing.
df["math"] = df["math"].where(df["math"] <= 100)
for col in ["math", "science", "english"]:
    df[col] = df[col].fillna(df[col].median())

df["gender"] = df["gender"].str.upper()
df["attendance"] = df["attendance"].str.replace("%", "").astype(int)
df["joined"] = pd.to_datetime(df["joined"])

print("Rows at end:", len(df))
print(df[["name", "gender", "math", "science", "english", "attendance"]])
```

```{ .text .output title="Output" }
Rows at start: 11
Missing values: 2
Duplicate rows: 1
Rows at end: 10
       name gender  math  science  english  attendance
0      Asha      F  78.0     85.0     72.0          92
1    Bikash      M  64.0     72.0     70.0          85
2   Chandra      M  92.0     88.0     81.0          97
3    Dipesh      M  45.0     52.0     48.0          70
5     Elina      F  67.0     91.0     95.0          98
6      Gita      F  56.0     61.0     72.0          80
7      Hari      M  73.0     69.0     77.0          88
8      Isha      F  81.0     79.0     84.0          94
9     Jiwan      M  39.0     44.0     50.0          65
10    Kiran      M  67.0     72.0     63.0          83
```

### Your Turn

1. Add a column `average` with the mean of the three subjects, rounded to 1 place. Print the name and average of the top three students.
2. **Normalise** `attendance` to a 0 to 1 scale. This means subtract the smallest value and divide by the range. Print the first three rows of `name` and the new column.

??? success "Solution"

    ```python
    import pandas as pd

    df = pd.read_csv("students_raw.csv").drop_duplicates()
    df["math"] = df["math"].where(df["math"] <= 100)
    for col in ["math", "science", "english"]:
        df[col] = df[col].fillna(df[col].median())

    df["average"] = df[["math", "science", "english"]].mean(axis=1).round(1)
    top3 = df.sort_values("average", ascending=False).head(3)
    print(top3[["name", "average"]])
    ```

    ```{ .text .output title="Output" }
          name  average
    2  Chandra     87.0
    5    Elina     84.3
    8     Isha     81.3
    ```

    ```python
    import pandas as pd

    df = pd.read_csv("students_raw.csv").drop_duplicates()
    df["attendance"] = df["attendance"].str.replace("%", "").astype(int)

    low, high = df["attendance"].min(), df["attendance"].max()
    df["attendance_01"] = ((df["attendance"] - low) / (high - low)).round(2)
    print(df[["name", "attendance_01"]].head(3))
    ```

    ```{ .text .output title="Output" }
          name  attendance_01
    0     Asha           0.82
    1   Bikash           0.61
    2  Chandra           0.97
    ```

### Check Yourself

- [ ] I counted missing values and duplicates before I cleaned them.
- [ ] I can explain why the median is a safer fill value than the mean when there is an outlier.
- [ ] After cleaning, `attendance` is a number and `joined` is a date.
- [ ] I can say what normalising does to a column.

## Lab 8: Descriptive Statistics and Visualization

### Objective

Summarise a table with **descriptive statistics** (numbers such as the mean and the spread that describe the data) and draw a **scatter plot** with Matplotlib and Seaborn to see how two columns are related.

### What You Need

- `tips.csv` ([Practice Data Files](setup.md#practice-data-files)): 244 restaurant bills with the tip left for each.
- Libraries: `pandas`, `matplotlib`, `seaborn`.
- Background: [Unit VIII](unit-08-eda.md).

### Steps

1. Load `tips.csv` and look at the `total_bill` and `tip` columns.
2. Use `.describe()` to get the count, mean, spread and quartiles in one table.
3. Find the **correlation** (a number from -1 to 1 that tells how strongly two columns move together) between `total_bill` and `tip`.
4. Draw a scatter plot of `total_bill` against `tip`. Always add a title.
5. Compare your plot and your numbers with the ones below.

### Starter Code

<!-- figure: u11-lab8-tips-scatter -->
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips = pd.read_csv("tips.csv")
print(tips[["total_bill", "tip"]].describe().round(2))
print("Correlation:", round(tips["total_bill"].corr(tips["tip"]), 2))

sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Bigger Bills Get Bigger Tips")
plt.xlabel("Total bill")
plt.ylabel("Tip")
plt.show()
```

```{ .text .output title="Output" }
       total_bill     tip
count      244.00  244.00
mean        19.79    3.00
std          8.90    1.38
min          3.07    1.00
25%         13.35    2.00
50%         17.80    2.90
75%         24.13    3.56
max         50.81   10.00
Correlation: 0.68
```

![Scatter plot of tip against total bill for 244 meals: the dots rise from the lower left to the upper right.](assets/img/u11-lab8-tips-scatter.png#only-light)
![Scatter plot of tip against total bill for 244 meals: the dots rise from the lower left to the upper right.](assets/img/u11-lab8-tips-scatter-dark.png#only-dark)

### Your Turn

1. Print the average tip for each `day`, rounded to 2 places, with `groupby`.
2. Change the plot so that the dots are coloured by `time` (lunch or dinner) with `hue="time"`. Print the average tip for each `time` too.

??? success "Solution"

    ```python
    import pandas as pd

    tips = pd.read_csv("tips.csv")
    print(tips.groupby("day")["tip"].mean().round(2))
    ```

    ```{ .text .output title="Output" }
    day
    Fri     2.73
    Sat     2.99
    Sun     3.26
    Thur    2.77
    Name: tip, dtype: float64
    ```

    This version draws the coloured plot on your screen and also prints the averages. The notes show only the printed numbers.

    ```python
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    tips = pd.read_csv("tips.csv")
    print(tips.groupby("time")["tip"].mean().round(2))

    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
    plt.title("Tips at Lunch and Dinner")
    plt.show()
    ```

    ```{ .text .output title="Output" }
    time
    Dinner    3.10
    Lunch     2.73
    Name: tip, dtype: float64
    ```

### Check Yourself

- [ ] I can read the mean, the minimum and the maximum from `.describe()`.
- [ ] My plot has a title and both axes are named.
- [ ] I can say in one sentence what the plot shows about bills and tips.
- [ ] I know what a correlation close to 1 means.

## Lab 9: Build Machine Learning Models with Scikit-learn

### Objective

Build three tiny models with **Scikit-learn**: a **regression** model that predicts a number, a **classification** model that predicts a label, and a **clustering** model that finds groups without labels. Print one **score** for each.

### What You Need

- `study_marks.csv` (60 students, hours studied and marks) and `shop_customers.csv` (90 shoppers, visits and spend). See [Practice Data Files](setup.md#practice-data-files).
- Libraries: `pandas`, `scikit-learn`.
- Background: [Unit IX](unit-09-ml.md).

### Steps

1. Load `study_marks.csv`. Choose `hours_studied` as the input and `marks` as the target.
2. Split the rows into a **training set** (the model learns from it) and a **test set** (the model is scored on it). Use `random_state=42` so that everyone gets the same split.
3. Fit a `LinearRegression` and print its score on the test set.
4. Fit a `LogisticRegression` on `hours_studied` and `attendance` to predict `result`. Print its accuracy.
5. Load `shop_customers.csv` and fit `KMeans` with 3 groups. Print how many customers are in each group.

### Starter Code

```python
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

students = pd.read_csv("study_marks.csv")

# 1. Regression: predict marks from hours studied
X = students[["hours_studied"]]
y = students["marks"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
reg = LinearRegression().fit(X_train, y_train)
print("Regression R2 score:", round(reg.score(X_test, y_test), 2))

# 2. Classification: predict Pass or Fail
X = students[["hours_studied", "attendance"]]
y = students["result"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
clf = LogisticRegression().fit(X_train, y_train)
print("Classification accuracy:", round(clf.score(X_test, y_test), 2))

# 3. Clustering: group the shoppers
customers = pd.read_csv("shop_customers.csv")
km = KMeans(n_clusters=3, n_init=10, random_state=42)
km.fit(customers[["monthly_visits", "monthly_spend"]])
sizes = pd.Series(km.labels_).value_counts().tolist()
print("Customers in each group:", sorted(sizes))
```

```{ .text .output title="Output" }
Regression R2 score: 0.8
Classification accuracy: 0.87
Customers in each group: [30, 30, 30]
```

### Your Turn

1. Use the regression model to predict the marks of a student who studies 6 hours. Print the prediction as a whole number.
2. Refit the clustering with 2 groups instead of 3. Print how many customers are in each group.

??? success "Solution"

    ```python
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    students = pd.read_csv("study_marks.csv")
    X = students[["hours_studied"]]
    reg = LinearRegression().fit(X, students["marks"])

    new_student = pd.DataFrame({"hours_studied": [6]})
    guess = reg.predict(new_student)[0]
    print("Predicted marks for 6 hours:", round(guess))
    ```

    ```{ .text .output title="Output" }
    Predicted marks for 6 hours: 58
    ```

    ```python
    import pandas as pd
    from sklearn.cluster import KMeans

    customers = pd.read_csv("shop_customers.csv")
    km = KMeans(n_clusters=2, n_init=10, random_state=42)
    km.fit(customers[["monthly_visits", "monthly_spend"]])
    sizes = pd.Series(km.labels_).value_counts().tolist()
    print("Customers in each group:", sorted(sizes))
    ```

    ```{ .text .output title="Output" }
    Customers in each group: [31, 59]
    ```

### Check Yourself

- [ ] I can say which of my three models is regression, which is classification and which is clustering.
- [ ] I can say why I score the model on the test set and not on the training set.
- [ ] I know why the clustering model has no target column.
- [ ] My `random_state=42` gave the same numbers as the Output block.

## Lab 10: Dashboards and Interactive Plots with Plotly Dash

### Objective

Build a small **dashboard** with **Plotly Dash**. A dashboard is a web page that shows charts and lets the viewer change them. Yours has a dropdown that filters the tips table by day, and a scatter plot that updates when you choose.

### What You Need

- `tips.csv` in the same folder as your script ([Practice Data Files](setup.md#practice-data-files)).
- Libraries: `dash`, `plotly`, `pandas`. If Python says `No module named 'dash'`, install it once, as shown in [Installing Extra Libraries](setup.md#installing-extra-libraries).
- Background: [Unit X](unit-10-visualization.md).

### Steps

1. Create a file named `app.py` in the folder with `tips.csv`. A Dash app is a normal script.
2. Type the starter code. Read the three parts: the data, the **layout** (what the page shows) and the **callback** (the function that runs when the dropdown changes).
3. Run it in a terminal with `python app.py`. The terminal prints a start-up message and then waits. It does not finish. That is normal, because the app is a server.
4. Open `http://127.0.0.1:8071/` in your browser. Choose a day in the dropdown and watch the plot change. Hover over a dot to see its values.
5. Stop the app by pressing `Ctrl+C` in the terminal.

### Starter Code

The notes run this app for a few seconds and stop it. The Output block is the real start-up message. The dashboard itself appears in your browser page at `http://127.0.0.1:8071/`, not in the terminal.

<!-- serve: 8; script: app.py -->
```python
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

tips = pd.read_csv("tips.csv")

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Restaurant Tips"),
    dcc.Dropdown(["Thur", "Fri", "Sat", "Sun"], "Sun", id="day"),
    dcc.Graph(id="chart"),
])


@app.callback(Output("chart", "figure"), Input("day", "value"))
def update(day):
    data = tips[tips["day"] == day]
    return px.scatter(data, x="total_bill", y="tip", title="Tips on " + day)


if __name__ == "__main__":
    app.run(port=8071)
```

```{ .text .output title="Output" }
Dash is running on http://127.0.0.1:8071/

 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8071
Press CTRL+C to quit
```

The line that starts with `WARNING` is normal. It only says that this built-in server is for learning and testing, not for a real website. The address in the output is where the dashboard lives.

Streamlit is another tool that can build dashboards in Python, and the syllabus allows it too. These labs use Dash only.

### Your Turn

1. Change the dropdown so that the viewer chooses `time` (`Lunch` or `Dinner`) instead of `day`.
2. Change the chart to a histogram of `total_bill` with `px.histogram`. Use the port `8073` so it does not clash with the first app if both are open.

??? success "Solution"

    Only three lines change: the dropdown values, the filter column and the chart type. The start-up message is the same kind as before. Open `http://127.0.0.1:8073/` to see the histogram.

    <!-- serve: 8; script: app.py -->
    ```python
    import pandas as pd
    import plotly.express as px
    from dash import Dash, dcc, html, Input, Output

    tips = pd.read_csv("tips.csv")

    app = Dash(__name__)
    app.layout = html.Div([
        html.H1("Restaurant Tips"),
        dcc.Dropdown(["Lunch", "Dinner"], "Dinner", id="time"),
        dcc.Graph(id="chart"),
    ])


    @app.callback(Output("chart", "figure"), Input("time", "value"))
    def update(time):
        data = tips[tips["time"] == time]
        return px.histogram(data, x="total_bill", title="Bills at " + time)


    if __name__ == "__main__":
        app.run(port=8073)
    ```

    ```{ .text .output title="Output" }
    Dash is running on http://127.0.0.1:8073/

     * Serving Flask app 'app'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:8073
    Press CTRL+C to quit
    ```

### Check Yourself

- [ ] I ran `python app.py` and saw the start-up message with the address.
- [ ] I opened the address in a browser and the page showed my dropdown and plot.
- [ ] I can say what the layout and the callback do.
- [ ] I stopped the app with `Ctrl+C`.
