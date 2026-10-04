# Lab 2: Variables, Data Types and Operators

## Objective

Store values in variables, see their data types, and use operators in a small calculator program. You also use `input()` to ask the user for a value.

## What You Need

- Python from Lab 1. No data file.
- Background: [Unit II](../unit-02-basics.md).

## Steps

1. Open a new file called `percentage.py` or a new notebook.
2. Type the starter code. It asks for a name, the marks obtained and the full marks.
3. Run it and type the values shown in the Output block. When you run it yourself, type your own values.
4. Look at the output line that shows `type(...)`. Notice that `int()` turned the typed text into a number.
5. Do the two tasks in Your Turn.

## Starter Code

The values after each prompt in the Output block (`Asha`, `342`, `400`) are what was typed in.

<!-- stdin: Asha | 342 | 400 -->
```python
name = input("Student name: ")
obtained = int(input("Marks obtained: "))
full = int(input("Full marks: "))

percentage = obtained / full * 100

print(name, "scored", round(percentage, 1), "percent")
print("Type of obtained:", type(obtained))
print("Passed:", percentage >= 45)
```

```{ .text .output title="Output" }
Student name: Asha
Marks obtained: 342
Full marks: 400
Asha scored 85.5 percent
Type of obtained: <class 'int'>
Passed: True
```

## Your Turn

1. Write a **bill calculator**. Ask for an item name, its price in Rs. and the quantity. Print the subtotal, a 13 percent tax and the final total.
2. A trip took 135 minutes. Use `//` and `%` to print it as hours and minutes.

??? success "Solution"

    <!-- stdin: Notebook | 60 | 5 -->
    ```python
    item = input("Item: ")
    price = float(input("Price in Rs.: "))
    quantity = int(input("Quantity: "))

    subtotal = price * quantity
    tax = subtotal * 0.13
    total = subtotal + tax

    print("Subtotal: Rs.", subtotal)
    print("Tax: Rs.", round(tax, 2))
    print("Total for", quantity, item, "= Rs.", round(total, 2))
    ```

    ```{ .text .output title="Output" }
    Item: Notebook
    Price in Rs.: 60
    Quantity: 5
    Subtotal: Rs. 300.0
    Tax: Rs. 39.0
    Total for 5 Notebook = Rs. 339.0
    ```

    `//` gives the whole part of a division. `%` gives what is left over.

    ```python
    minutes = 135
    hours = minutes // 60
    left = minutes % 60
    print(hours, "hours", left, "minutes")
    ```

    ```{ .text .output title="Output" }
    2 hours 15 minutes
    ```

## Check Yourself

- [ ] I can name the data type of a value using `type()`.
- [ ] I know why `input()` needs `int()` or `float()` around it for numbers.
- [ ] I can use `/`, `//`, `%` and `*` and say what each one gives.
- [ ] I can write a comparison like `percentage >= 45` and see `True` or `False`.
