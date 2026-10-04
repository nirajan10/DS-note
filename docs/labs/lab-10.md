# Lab 10: Dashboards and Interactive Plots with Plotly Dash

## Objective

Build a small **dashboard** with **Plotly Dash**. A dashboard is a web page that shows charts and lets the viewer change them. Yours has a dropdown that filters the tips table by day, and a scatter plot that updates when you choose.

## What You Need

- `tips.csv` in the same folder as your script ([Practice Data Files](../setup.md#practice-data-files)).
- Libraries: `dash`, `plotly`, `pandas`. If Python says `No module named 'dash'`, install it once, as shown in [Installing Extra Libraries](../setup.md#installing-extra-libraries).
- Background: [Unit X](../unit-10-visualization.md).

## Steps

1. Create a file named `app.py` in the folder with `tips.csv`. A Dash app is a normal script.
2. Type the starter code. Read the three parts: the data, the **layout** (what the page shows) and the **callback** (the function that runs when the dropdown changes).
3. Run it in a terminal with `python app.py`. The terminal prints a start-up message and then waits. It does not finish. That is normal, because the app is a server.
4. Open `http://127.0.0.1:8071/` in your browser. Choose a day in the dropdown and watch the plot change. Hover over a dot to see its values.
5. Stop the app by pressing `Ctrl+C` in the terminal.

## Starter Code

The notes run this app for a few seconds and stop it. The Output block is the real start-up message. The dashboard itself appears in your browser page at `http://127.0.0.1:8071/`, not in the terminal.

<!-- serve: 8; script: app.py -->
```python
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

tips = pd.read_csv("tips.csv")

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Restaurant Tips"),
    dcc.Dropdown(["Thur", "Fri", "Sat", "Sun"], "Sun", id="day"),
    dcc.Graph(id="chart"),
])


@app.callback(Output("chart", "figure"), Input("day", "value"))
def update(day):
    data = tips[tips["day"] == day]
    return px.scatter(data, x="total_bill", y="tip", title="Tips on " + day)


if __name__ == "__main__":
    app.run(port=8071)
```

```{ .text .output title="Output" }
Dash is running on http://127.0.0.1:8071/

 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8071
Press CTRL+C to quit
```

The line that starts with `WARNING` is normal. It only says that this built-in server is for learning and testing, not for a real website. The address in the output is where the dashboard lives.

Streamlit is another tool that can build dashboards in Python, and the syllabus allows it too. These labs use Dash only.

## Your Turn

1. Change the dropdown so that the viewer chooses `time` (`Lunch` or `Dinner`) instead of `day`.
2. Change the chart to a histogram of `total_bill` with `px.histogram`. Use the port `8073` so it does not clash with the first app if both are open.

??? success "Solution"

    Only three lines change: the dropdown values, the filter column and the chart type. The start-up message is the same kind as before. Open `http://127.0.0.1:8073/` to see the histogram.

    <!-- serve: 8; script: app.py -->
    ```python
    import pandas as pd
    import plotly.express as px
    from dash import Dash, dcc, html, Input, Output

    tips = pd.read_csv("tips.csv")

    app = Dash(__name__)
    app.layout = html.Div([
        html.H1("Restaurant Tips"),
        dcc.Dropdown(["Lunch", "Dinner"], "Dinner", id="time"),
        dcc.Graph(id="chart"),
    ])


    @app.callback(Output("chart", "figure"), Input("time", "value"))
    def update(time):
        data = tips[tips["time"] == time]
        return px.histogram(data, x="total_bill", title="Bills at " + time)


    if __name__ == "__main__":
        app.run(port=8073)
    ```

    ```{ .text .output title="Output" }
    Dash is running on http://127.0.0.1:8073/

     * Serving Flask app 'app'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:8073
    Press CTRL+C to quit
    ```

## Check Yourself

- [ ] I ran `python app.py` and saw the start-up message with the address.
- [ ] I opened the address in a browser and the page showed my dropdown and plot.
- [ ] I can say what the layout and the callback do.
- [ ] I stopped the app with `Ctrl+C`.
