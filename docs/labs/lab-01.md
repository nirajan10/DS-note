# Lab 1: Set Up Python and Run a First Script

## Objective

Get a working Python in a **virtual environment**, and run your first **script**. A script is a text file of Python lines that Python runs from top to bottom. A virtual environment is a private folder with its own Python and its own libraries. Your script will also print your name and your folder, so the work is clearly yours.

## What You Need

- A computer with internet for the first setup. [Setting Up Python](../setup.md) shows the ways: **Anaconda** (a free bundle of Python, data tools and Jupyter), **Miniconda** (a much smaller start, where you add the libraries yourself), **plain Python** with `venv` and `pip` (no conda), or **Google Colab** (Jupyter in the browser, with nothing to install). **Jupyter Notebook** is a page where you run code in small cells.
- Background: [Unit I](../unit-01-intro.md).

## Steps

1. Set up one tool. On your computer, follow [Option 1: Anaconda](../setup.md#option-1-anaconda-on-your-computer), [Option 1B: Miniconda](../setup.md#option-1b-miniconda-the-light-alternative) if disk space is small, or [Option 1C: Plain Python](../setup.md#option-1c-plain-python-with-venv-and-pip) if you do not want conda. Then [Opening Jupyter Notebook](../setup.md#opening-jupyter-notebook), or work in [Visual Studio Code](../setup.md#option-3-visual-studio-code). In a browser, follow [Option 2: Google Colab](../setup.md#option-2-google-colab).
2. Make a folder called `lab1` and a virtual environment (next section). Colab needs no environment.
3. Install `pandas` and `numpy` inside the environment.
4. Create a file named `hello.py` inside `lab1`, as shown in [Running a Script from the Terminal](../setup.md#running-a-script-from-the-terminal). In Jupyter or Colab, open a new notebook instead.
5. Type the starter code below. Change `student_name` to your own name.
6. Run it from inside the `lab1` folder, with the environment active. In a terminal, type `python hello.py`. In Jupyter or Colab, press `Shift+Enter` on the cell.
7. Compare what you see with the Output block. Your name, user, folder and Python path will be different. Your version numbers may be different. That is fine.
8. Run the full library check in [Checking Your Setup](../setup.md#checking-your-setup) once, so you know every library is ready for the later labs.

## Make a Virtual Environment

Every project gets its own environment, so the libraries of one project never clash with another. You make it once, then **activate** it each time you open a new terminal.

=== "Windows"

    ```bash
    mkdir lab1
    cd lab1
    python -m venv .venv
    .venv\Scripts\activate.bat
    pip install pandas numpy
    ```

    In PowerShell, use `.venv\Scripts\Activate.ps1` for the fourth line.

=== "macOS and Linux"

    ```bash
    mkdir lab1
    cd lab1
    python3 -m venv .venv
    source .venv/bin/activate
    pip install pandas numpy
    ```

=== "Anaconda or Miniconda"

    ```bash
    mkdir lab1
    cd lab1
    conda create -n lab1 python=3.12 -y
    conda activate lab1
    pip install pandas numpy
    ```

=== "Colab"

    There is nothing to make. Each Colab session starts clean. If a library is missing, run `!pip install pandas numpy` in a cell.

After activation you see `(.venv)` (or `(lab1)` for conda) at the start of the line. That is how you know the environment is active. If you already made the `dsc481` environment on the setup page, you may use it instead.

## Starter Code

Run it. Your first line must read exactly the same as the Output block.

```python
import getpass
import os
import platform
import sys

import pandas as pd

student_name = "Asha Gurung"   # type your own name here

print("Hello, Data Science!")
print("Name:", student_name)
print("User:", getpass.getuser())
print("Folder:", os.getcwd())
print("Python:", sys.executable)
print("Python version:", platform.python_version())
print("pandas version:", pd.__version__)
```

```{ .text .output title="Output" }
Hello, Data Science!
Name: Asha Gurung
User: asha
Folder: /home/student/project
Python: /home/student/project/.venv/bin/python
Python version: 3.12.3
pandas version: 3.0.6
```

Read the four middle lines. **Name** is the name you typed. **User** is the login name of your computer. **Folder** is where Python is running. **Python** is the Python that ran your code, and it should be inside your `.venv`. Yours will show your own values, for example a folder like `C:\Users\Asha\lab1` on Windows.

## Common Mistakes

!!! warning "Common Mistake: Missing Library"

    A `ModuleNotFoundError` means Python cannot find a library. Here the name is mistyped: `panda` instead of `pandas`.

    <!-- error -->
    ```python
    import panda as pd
    ```

    ```{ .text .output title="Output" }
    Traceback (most recent call last):
      File "example.py", line 1, in <module>
        import panda as pd
    ModuleNotFoundError: No module named 'panda'
    ```

    The same error appears when the spelling is right, but the library is not in the Python that you are running. There are three usual causes:

    1. The library is not installed. Run `pip install pandas`.
    2. The environment is not active. There is no `(.venv)` at the start of the line. Activate it, then install again.
    3. You installed it in one Python, but run your code in another. In a notebook, the **kernel** may be a different Python from your terminal. Look at the **Python** line of your output to see which one runs.

!!! warning "Common Mistake: A File Named Like a Library"

    A file in your folder with the same name as a library hides the real library. Here is a file called `pandas.py`.

    <!-- file: pandas.py -->
    ```python title="pandas.py"
    print("This is my own file, not the library")
    ```

    <!-- error -->
    ```python
    import pandas as pd
    print(pd.__version__)
    ```

    ```{ .text .output title="Output" }
    This is my own file, not the library
    Traceback (most recent call last):
      File "example.py", line 2, in <module>
        print(pd.__version__)
              ^^^^^^^^^^^^^^
    AttributeError: module 'pandas' has no attribute '__version__'
    ```

    Python found your `pandas.py` first. Never name your own files `pandas.py`, `numpy.py`, `random.py`, `math.py` or `csv.py`. Rename the file and delete the folder `__pycache__` if one was created.

!!! warning "Common Mistake: Smart Quotes"

    Code copied from a slide, a PDF or a Word file may have curly quotes. Python only accepts straight quotes.

    <!-- error -->
    ```python
    print(“Hello, Data Science!”)
    ```

    ```{ .text .output title="Output" }
      File "example.py", line 1
        print(“Hello, Data Science!”)
              ^
    SyntaxError: invalid character '“' (U+201C)
    ```

    Retype the quotes in your editor.

More mistakes that happen in this lab:

| What you see | Why | What to do |
|---|---|---|
| `'python' is not recognized` (Windows) or `command not found: python` | Python is not installed, or it is not on your `PATH` | Install from [python.org](https://www.python.org/downloads/), tick the `PATH` option, open a **new** terminal. On macOS and Linux try `python3`. Check with `python --version`. |
| `can't open file ... [Errno 2] No such file or directory` | The terminal is in a different folder from `hello.py` | Use `cd` to go into `lab1`. Check the **Folder** line of your output. |
| The same message, but the file is there | Windows saved it as `hello.py.txt` | In File Explorer, turn on **File name extensions** (the **View** menu) and rename the file. |
| No `(.venv)` at the start of the line | The environment is not active | Activate it again. Do this in every new terminal. |
| PowerShell says running scripts is disabled | Windows blocks the activate script | Use Command Prompt with `activate.bat`, or run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once. |
| `error: externally-managed-environment` when you run `pip install` | You are installing into the system Python, which is protected | Make and activate a virtual environment first. This is the reason we use one. |
| The library works in the terminal but not in VS Code | VS Code uses another Python | Press `Ctrl+Shift+P`, run `Python: Select Interpreter` and pick the one in `.venv`. |

## Your Turn

1. Add a line that prints your roll number, and another that prints your college.
2. Add one more version check, for `numpy`, the number library. Import it as `np` and print `np.__version__`.

??? success "Solution"

    ```python
    import numpy as np

    print("Roll number: 24")
    print("College: Pokhara University")
    print("numpy version:", np.__version__)
    ```

    ```{ .text .output title="Output" }
    Roll number: 24
    College: Pokhara University
    numpy version: 2.5.3
    ```

## How to Submit

Your teacher needs to know that the output is from your own computer.

1. Put your own name in `student_name` and run the starter code.
2. Take a screenshot of the **whole screen**, not a cropped part. Keep the clock visible.
3. Check that the **Name**, **User**, **Folder** and **Python** lines show your own values.

Every student's **User**, **Folder** and **Python** lines are different. Your teacher uses them to tell your work from a copy. A screenshot that shows someone else's name or folder is not accepted.

## Check Yourself

- [ ] I have one working tool: Anaconda, Miniconda, plain Python, Jupyter or Colab.
- [ ] I made a virtual environment, and I can see `(.venv)` or `(lab1)` when it is active.
- [ ] I ran a script or a cell and saw my own name, user and folder in the output.
- [ ] I can say what a script is, and what a virtual environment is.
- [ ] I know how to read the version of a library.
