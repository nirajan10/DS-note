# Unit X Exam Questions: Data Visualization and Reporting

[Back to the Unit X notes](../unit-10-visualization.md)

## Past Paper Questions

No past-paper question for this unit was found.

## Practice Questions (Not from Past Papers)

**P1. (Short answer)** What does a heatmap show? How do you read the colours in a correlation heatmap drawn with `cmap="coolwarm"`, and why do we set `vmin=-1` and `vmax=1`?

??? success "Model Answer"

    A heatmap is a grid in which the colour of each cell shows a number, so you can spot big and small values at a glance. In a correlation heatmap, red cells are positive correlations (the deeper, the stronger), blue cells are negative correlations, and the middle colour means almost no link. The diagonal is always 1 because a column matches itself. `vmin=-1` and `vmax=1` fix the colour scale to the full range of a correlation, so the middle colour always means zero and the same colour always means the same number.

**P2. (Predict the output)** A heatmap needs a grid, which a pivot table gives. What does this program print?

<!-- answer -->
```python
import pandas as pd

sales = pd.DataFrame({
    "category": ["Grocery", "Grocery", "Stationery", "Stationery", "Grocery"],
    "weekday": ["Mon", "Tue", "Mon", "Tue", "Mon"],
    "amount": [500, 300, 120, 80, 200],
})
print(sales.pivot_table(index="category", columns="weekday", values="amount", aggfunc="sum"))
```

??? success "Model Answer"

    ```{ .text .output title="Output" }
    weekday     Mon  Tue
    category            
    Grocery     700  300
    Stationery  120   80
    ```

    The rows are the categories and the columns are the weekdays. Each cell is the sum of the amounts for that pair. Grocery on Monday has two sales, 500 and 200, so the cell shows 700.

**P3. (Short answer)** What is a pair plot? The iris dataset has four number columns and three species. How many panels does `sns.pairplot(flowers, hue="species")` draw, and what do the panels on the diagonal show?

??? success "Model Answer"

    A pair plot is a grid that draws a scatter plot for every pair of number columns. With four columns the grid is 4 by 4, so it has 16 panels. Twelve are scatter plots (each pair appears twice, with the axes swapped). The four panels on the diagonal cannot be scatter plots, so they show how each single column is spread out. `hue="species"` colours the points by species, so you can see which measurements separate the three species.

**P4. (Short answer)** What does it mean for a plot to be interactive? Name three things the reader can do. How does `fig.show()` behave in a Jupyter notebook and in a Python script?

??? success "Model Answer"

    An interactive plot reacts to the mouse. The reader can hover over a point to see its values, zoom into a region by dragging a box, pan to move the view, or click a legend item to hide and show a group. In a Jupyter notebook or Colab, `fig.show()` shows the plot under the cell. In a Python script, it opens the plot as a web page in the default browser.

**P5. (Write a program)** Using `tips.csv` and Plotly Express, write a program that builds a bar chart of the average `total_bill` for each `day`. Give it a title. Print the averages, rounded to 1 decimal place, before showing the chart.

??? success "Model Answer"

    ```python
    import pandas as pd
    import plotly.express as px

    tips = pd.read_csv("tips.csv")
    average = tips.groupby("day", as_index=False)["total_bill"].mean().round(1)
    print(average)

    fig = px.bar(average, x="day", y="total_bill", title="Average Bill by Day")
    fig.show()
    ```

    ```{ .text .output title="Output" }
        day  total_bill
    0   Fri        17.2
    1   Sat        20.4
    2   Sun        21.4
    3  Thur        17.7
    ```

    `px.bar()` needs a table and the names of the columns for `x` and `y`. `as_index=False` keeps `day` as an ordinary column, so Plotly can use it.

**P6. (Short answer)** A Dash app has two parts. Name them and say what each does. In `@callback(Output("graph", "figure"), Input("menu", "value"))`, which is the input and which is the output?

??? success "Model Answer"

    The **layout** is what the user sees: the heading, the menu and the graph. The **callback** is a Python function that runs when the user changes something, and it updates part of the page. Here the input is the `value` of the component with id `menu` (the user's choice), and the output is the `figure` of the component with id `graph`, which gets whatever the function returns.

**P7. (Write a program)** Write a complete Dash app (`app.py`) that shows a histogram of `total_bill` from `tips.csv` and a dropdown that lets the user choose a day (`Thur`, `Fri`, `Sat`, `Sun`). The histogram must show only the chosen day. Use port 8064.

??? success "Model Answer"

    <!-- serve: 8; script: app.py -->
    ```python
    import pandas as pd
    import plotly.express as px
    from dash import Dash, dcc, html, Input, Output, callback

    tips = pd.read_csv("tips.csv")

    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("Bills by Day"),
        dcc.Dropdown(
            id="day-menu",
            options=["Thur", "Fri", "Sat", "Sun"],
            value="Sat",
            clearable=False,
        ),
        dcc.Graph(id="bill-histogram"),
    ])


    @callback(
        Output("bill-histogram", "figure"),
        Input("day-menu", "value"),
    )
    def update_histogram(day):
        one_day = tips[tips["day"] == day]
        return px.histogram(one_day, x="total_bill", title=f"Bills on {day}")


    if __name__ == "__main__":
        app.run(port=8064, debug=True)
    ```

    ```{ .text .output title="Output" }
    Dash is running on http://127.0.0.1:8064/

     * Serving Flask app 'app'
     * Debug mode: on
    ```

    The ids `day-menu` and `bill-histogram` are written exactly the same in the layout and in the callback. The function's argument receives the chosen day.

**P8. (Short answer)** A student's Dash page opens, but the graph stays empty and an error panel says "ID not found in layout". What is the most likely cause, and how do you fix it?

??? success "Model Answer"

    The `id` used in the callback (in `Input(...)` or `Output(...)`) does not match any `id` in the layout. It is usually a spelling mistake, for example `day-dropdwon` instead of `day-dropdown`. Compare every id in the callback with the layout and correct the spelling so that they match exactly.

**P9. (Short answer)** How do you start a Dash app saved as `app.py` that uses `port=8061`, which address do you open in the browser, and how do you stop the app?

??? success "Model Answer"

    Open a terminal in the folder with `app.py` and the data file and run `python app.py`. Then open `http://127.0.0.1:8061/` in a web browser. (`127.0.0.1` means "this computer".) To stop the app, go back to the terminal and press `Ctrl+C`.

**P10. (Long answer)** A chart has the title "Sales", no axis labels, nine bars in nine different colours, and the months in alphabetical order. List the five rules for presenting data effectively and use them to say how you would improve this chart.

??? success "Model Answer"

    The five rules are: (1) one message per chart, (2) a title that states the finding, (3) labelled axes with units, (4) the right chart for the question, (5) meaningful colours.

    Improvements: put the months in calendar order (a line plot over time may suit the question better than bars). Change the title from "Sales" to a finding, such as "Sales Doubled Between June and September". Label the axes ("Month", "Sales (Rs.)"). Use one colour for all bars, and use a different colour only to mark something meaningful, such as the best month. Show only the one message the reader should remember.

**P11. (Long answer)** A school wants a small dashboard for the class marks table. Describe its layout and its callback: which controls and graphs would you place, what is the input and what is the output?

??? success "Model Answer"

    **Layout:** a heading ("Class Marks Dashboard"), a dropdown with the three subjects (Maths, Science, English), and a graph.

    **Callback:** the input is the `value` of the dropdown (the chosen subject). The callback function takes the chosen subject, builds a histogram or a bar chart of that subject's marks with a title and axis labels, and returns the figure. The output is the `figure` of the graph. Whenever the teacher picks another subject, Dash runs the callback again and the graph updates.
