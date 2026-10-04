# Lab 7: Import and Clean a Dataset

## Objective

Load a messy dataset with **pandas** and clean it: find and fill missing values, drop duplicate rows, fix an impossible value (an **outlier**), and change text columns into proper numbers and dates.

## What You Need

- `students_raw.csv` ([Practice Data Files](../setup.md#practice-data-files)). It has real-world mess on purpose: two missing values, one duplicate row, one mark of 880, `attendance` stored as text like `92%`, and `gender` in mixed case.
- Library: `pandas`.
- Background: [Unit VII](../unit-07-cleaning.md).

## Steps

1. Open a new file or notebook. Load `students_raw.csv`.
2. Count the missing values and the duplicate rows before you change anything.
3. Drop the duplicate rows.
4. Fill the missing marks with the **median** (the middle value) of their column.
5. Treat any maths mark above 100 as wrong: make it missing, then fill it with the median too.
6. Make `gender` upper case, turn `attendance` into a number and `joined` into a date.
7. Print the cleaned table and compare.

## Starter Code

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

## Your Turn

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

## Check Yourself

- [ ] I counted missing values and duplicates before I cleaned them.
- [ ] I can explain why the median is a safer fill value than the mean when there is an outlier.
- [ ] After cleaning, `attendance` is a number and `joined` is a date.
- [ ] I can say what normalising does to a column.
