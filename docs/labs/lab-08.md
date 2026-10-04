# Lab 8: Descriptive Statistics and Visualization

## Objective

Summarise a table with **descriptive statistics** (numbers such as the mean and the spread that describe the data) and draw a **scatter plot** with Matplotlib and Seaborn to see how two columns are related.

## What You Need

- `tips.csv` ([Practice Data Files](../setup.md#practice-data-files)): 244 restaurant bills with the tip left for each.
- Libraries: `pandas`, `matplotlib`, `seaborn`.
- Background: [Unit VIII](../unit-08-eda.md).

## Steps

1. Load `tips.csv` and look at the `total_bill` and `tip` columns.
2. Use `.describe()` to get the count, mean, spread and quartiles in one table.
3. Find the **correlation** (a number from -1 to 1 that tells how strongly two columns move together) between `total_bill` and `tip`.
4. Draw a scatter plot of `total_bill` against `tip`. Always add a title.
5. Compare your plot and your numbers with the ones below.

## Starter Code

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

![Scatter plot of tip against total bill for 244 meals: the dots rise from the lower left to the upper right.](../assets/img/u11-lab8-tips-scatter.png#only-light)
![Scatter plot of tip against total bill for 244 meals: the dots rise from the lower left to the upper right.](../assets/img/u11-lab8-tips-scatter-dark.png#only-dark)

## Your Turn

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

## Check Yourself

- [ ] I can read the mean, the minimum and the maximum from `.describe()`.
- [ ] My plot has a title and both axes are named.
- [ ] I can say in one sentence what the plot shows about bills and tips.
- [ ] I know what a correlation close to 1 means.
