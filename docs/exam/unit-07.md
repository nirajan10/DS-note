# Unit VII Exam Questions: Data Collection and Cleaning with Python

[Back to the Unit VII notes](../unit-07-cleaning.md)

## Past Paper Questions

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

    This course covers cleaning and transformation in [Unit VII](../unit-07-cleaning.md).

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

## Practice Questions (Not from Past Papers)

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
