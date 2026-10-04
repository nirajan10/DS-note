# Unit XI Exam Questions: Practical Lab Work

[Back to the Unit XI notes](../unit-11-lab.md)

## Past Paper Questions

No past-paper question for this unit was found.

## Practice Questions (Not from Past Papers)

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
