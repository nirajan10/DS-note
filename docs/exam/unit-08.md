# Unit VIII Exam Questions: Exploratory Data Analysis

[Back to the Unit VIII notes](../unit-08-eda.md)

## Past Paper Questions

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

    ![Box plot of the twelve exam scores. The box runs from about 28 to 61 with the median line at 51; the whiskers reach 17 and 80. There are no outliers.](../assets/img/ex-box-scores.png#only-light)
    ![Box plot of the twelve exam scores. The box runs from about 28 to 61 with the median line at 51; the whiskers reach 17 and 80. There are no outliers.](../assets/img/ex-box-scores-dark.png#only-dark)

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

## Practice Questions (Not from Past Papers)

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
