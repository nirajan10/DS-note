# Lab 9: Build Machine Learning Models with Scikit-learn

## Objective

Build three tiny models with **Scikit-learn**: a **regression** model that predicts a number, a **classification** model that predicts a label, and a **clustering** model that finds groups without labels. Print one **score** for each.

## What You Need

- `study_marks.csv` (60 students, hours studied and marks) and `shop_customers.csv` (90 shoppers, visits and spend). See [Practice Data Files](../setup.md#practice-data-files).
- Libraries: `pandas`, `scikit-learn`.
- Background: [Unit IX](../unit-09-ml.md).

## Steps

1. Load `study_marks.csv`. Choose `hours_studied` as the input and `marks` as the target.
2. Split the rows into a **training set** (the model learns from it) and a **test set** (the model is scored on it). Use `random_state=42` so that everyone gets the same split.
3. Fit a `LinearRegression` and print its score on the test set.
4. Fit a `LogisticRegression` on `hours_studied` and `attendance` to predict `result`. Print its accuracy.
5. Load `shop_customers.csv` and fit `KMeans` with 3 groups. Print how many customers are in each group.

## Starter Code

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

## Your Turn

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

## Check Yourself

- [ ] I can say which of my three models is regression, which is classification and which is clustering.
- [ ] I can say why I score the model on the test set and not on the training set.
- [ ] I know why the clustering model has no target column.
- [ ] My `random_state=42` gave the same numbers as the Output block.
