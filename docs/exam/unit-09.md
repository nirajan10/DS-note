# Unit IX Exam Questions: Introduction to Machine Learning with Python

[Back to the Unit IX notes](../unit-09-ml.md)

## Past Paper Questions

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

## Practice Questions (Not from Past Papers)

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
