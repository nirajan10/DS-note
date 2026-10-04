# Unit I Exam Questions: Introduction to Data Science and Python

[Back to the Unit I notes](../unit-01-intro.md)

## Past Paper Questions

No past-paper question for this unit was found.

## Practice Questions (Not from Past Papers)

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
