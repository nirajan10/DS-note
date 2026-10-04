# Lab 5: Lists, Tuples, Sets and Dictionaries

## Objective

Build a mini student register. You use a **list** (an ordered collection you can change), a **tuple** (an ordered collection you cannot change), a **set** (a collection of unique items) and a **dictionary** (pairs of a key and a value).

## What You Need

- No data file. All data is typed in.
- Background: [Unit V](../unit-05-structures.md).

## Steps

1. Open a new file `register.py`.
2. Make the list of names, then use `append()` and `sort()` on it.
3. Make the tuple of subjects. Read its first item.
4. Make the dictionary of marks. Change one value and loop over it with `.items()`.
5. Make the two sets of club members. Use `&` and `|` on them.
6. Run it and compare with the Output block.

## Starter Code

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

## Your Turn

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

## Check Yourself

- [ ] I can say which of the four structures can be changed and which cannot.
- [ ] I read and changed a dictionary value by its key.
- [ ] I used `.items()` to loop over a dictionary.
- [ ] I can say what `&` and `|` do on sets.
