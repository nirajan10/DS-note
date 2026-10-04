# Lab 1: Set Up Python and Run a First Script

## Objective

Get a working Python on your computer, or in the browser, and run your first **script**. A script is a text file of Python lines that Python runs from top to bottom.

## What You Need

- A computer with internet for the first setup. [Setting Up Python](../setup.md) shows two ways: **Anaconda** (a free bundle of Python, data tools and Jupyter) or **Google Colab** (Jupyter in the browser, with nothing to install). **Jupyter Notebook** is a page where you run code in small cells.
- Background: [Unit I](../unit-01-intro.md).

## Steps

1. Set up one tool. On your computer, follow [Option 1: Anaconda](../setup.md#option-1-anaconda-on-your-computer) and then [Opening Jupyter Notebook](../setup.md#opening-jupyter-notebook). In a browser, follow [Option 2: Google Colab](../setup.md#option-2-google-colab).
2. Make a new folder called `lab1`. Create a file named `hello.py` inside it, as shown in [Running a Script From the Terminal](../setup.md#running-a-script-from-the-terminal). In Jupyter or Colab, open a new notebook instead.
3. Type the starter code below.
4. Run it. In a terminal, type `python hello.py`. In Jupyter or Colab, press `Shift+Enter` on the cell.
5. Compare what you see with the Output block. Your version numbers may be different. That is fine.
6. Run the full library check in [Checking Your Setup](../setup.md#checking-your-setup) once, so you know every library is ready for the later labs.

## Starter Code

Run it. Your first line must read exactly the same as the Output block.

```python
import platform
import pandas as pd

print("Hello, Data Science!")
print("Python version:", platform.python_version())
print("pandas version:", pd.__version__)
```

```{ .text .output title="Output" }
Hello, Data Science!
Python version: 3.12.3
pandas version: 3.0.6
```

If the third line fails with `ModuleNotFoundError: No module named 'pandas'`, your Python does not have pandas yet. Anaconda and Colab already have it. See [Installing Extra Libraries](../setup.md#installing-extra-libraries).

## Your Turn

1. Print your own name and your college on two separate lines.
2. Add one more version check, for `numpy`, the number library. Import it as `np` and print `np.__version__`.

??? success "Solution"

    ```python
    import numpy as np

    print("Name: Asha Gurung")
    print("College: Pokhara University")
    print("numpy version:", np.__version__)
    ```

    ```{ .text .output title="Output" }
    Name: Asha Gurung
    College: Pokhara University
    numpy version: 2.5.3
    ```

## Check Yourself

- [ ] I have one working tool: Anaconda, Jupyter or Colab.
- [ ] I ran a script or a cell and saw the output.
- [ ] I can say what a script is.
- [ ] I know how to read the version of a library.
