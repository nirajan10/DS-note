# Unit V Exam Questions: Data Structures in Python

[Back to the Unit V notes](../unit-05-structures.md)

## Past Paper Questions

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

## Practice Questions (Not from Past Papers)

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
