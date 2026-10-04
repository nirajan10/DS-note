"""Build the small practice datasets in docs/assets/data/.

Every file is tiny so students can open it and read all of it.
Random data uses a fixed seed, so running this script again gives the same files.

tips.csv is the one exception: it is the classic restaurant-tips table from the
seaborn-data project, downloaded once and kept as is.

Run:  python scripts/make_data.py
"""
import json
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "docs" / "assets" / "data"
DATA.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(481)


def save_csv(name, df):
    df.to_csv(DATA / name, index=False)
    print(f"wrote {name:<22} {len(df):>4} rows")


# 1. students.csv: ten students, three subjects --------------------------------
students = pd.DataFrame(
    {
        "roll": range(1, 11),
        "name": ["Asha", "Bikash", "Chandra", "Dipesh", "Elina",
                 "Gita", "Hari", "Isha", "Jiwan", "Kiran"],
        "math": [78, 64, 92, 45, 88, 56, 73, 81, 39, 67],
        "science": [85, 58, 88, 52, 91, 61, 69, 79, 44, 72],
        "english": [72, 70, 81, 48, 95, 66, 77, 84, 50, 63],
        "attendance": [92, 85, 97, 70, 98, 80, 88, 94, 65, 83],
    }
)
save_csv("students.csv", students)

# JSON version of the same table (list of records)
(DATA / "students.json").write_text(
    json.dumps(students.to_dict(orient="records"), indent=2) + "\n"
)
print("wrote students.json")

# 2. students_raw.csv: the same class with typical real-world mess ---------------
raw_rows = [
    (1, "Asha", "F", 78, 85, 72, "92%", "2024-01-15"),
    (2, "Bikash", "M", 64, None, 70, "85%", "2024-01-15"),
    (3, "Chandra", "m", 92, 88, 81, "97%", "2024-01-16"),
    (4, "Dipesh", "M", 45, 52, 48, "70%", "2024-01-16"),
    (4, "Dipesh", "M", 45, 52, 48, "70%", "2024-01-16"),  # duplicate row
    (5, "Elina", "F", 880, 91, 95, "98%", "2024-01-17"),  # typo: 880, not 88
    (6, "Gita", "F", 56, 61, None, "80%", "2024-01-17"),
    (7, "Hari", "M", 73, 69, 77, "88%", "2024-01-18"),
    (8, "Isha", "F", 81, 79, 84, "94%", "2024-01-18"),
    (9, "Jiwan", "M", 39, 44, 50, "65%", "2024-01-19"),
    (10, "Kiran", "M", 67, 72, 63, "83%", "2024-01-19"),
]
raw = pd.DataFrame(
    raw_rows,
    columns=["roll", "name", "gender", "math", "science", "english",
             "attendance", "joined"],
)
save_csv("students_raw.csv", raw)

# 3. shop_sales.csv: one small shop, three weeks ---------------------------------
items = {
    "Rice": ("Grocery", 130), "Lentils": ("Grocery", 190), "Cooking Oil": ("Grocery", 260),
    "Tea": ("Grocery", 150), "Soap": ("Household", 45), "Detergent": ("Household", 120),
    "Notebook": ("Stationery", 60), "Pen": ("Stationery", 15),
}
dates = pd.date_range("2024-03-01", periods=21, freq="D")
rows = []
for d in dates:
    for item in rng.choice(list(items), size=2, replace=False):
        category, price = items[item]
        rows.append(
            (d.strftime("%Y-%m-%d"), item, category, int(rng.integers(1, 9)),
             price, str(rng.choice(["Pokhara", "Kathmandu", "Butwal"], p=[0.5, 0.3, 0.2])))
        )
sales = pd.DataFrame(rows, columns=["date", "item", "category", "quantity", "price", "city"])
save_csv("shop_sales.csv", sales)
sales.to_excel(DATA / "shop_sales.xlsx", index=False, sheet_name="sales")
print("wrote shop_sales.xlsx")

# 4. mobile_data.csv: one phone, 30 days of data use (in MB) ----------------------
days = np.arange(1, 31)
base = rng.normal(1000, 140, size=30)
base[days % 7 == 0] += 450  # Saturdays are heavier
base = base.round().astype(int)
base[17] = 6200  # day 18: a big movie download (the outlier)
save_csv("mobile_data.csv", pd.DataFrame({"day": days, "mb_used": base}))

# 5. cricket.csv: twelve (made-up) batters ---------------------------------------
names = ["Anil", "Bibek", "Chiran", "Deepak", "Esan", "Faisal",
         "Gagan", "Hemant", "Ishan", "Jitu", "Kamal", "Lokesh"]
roles = ["Opener", "Opener", "Top order", "Top order", "Middle", "Middle",
         "Middle", "All-rounder", "All-rounder", "Finisher", "Finisher", "Bowler"]
matches = rng.integers(8, 26, size=12)
balls = (matches * rng.integers(18, 38, size=12)).astype(int)
strike = rng.normal(112, 14, size=12)
runs = (balls * strike / 100).round().astype(int)
fours = (runs * rng.uniform(0.07, 0.11, size=12)).round().astype(int)
sixes = (runs * rng.uniform(0.01, 0.045, size=12)).round().astype(int)
save_csv(
    "cricket.csv",
    pd.DataFrame({"player": names, "role": roles, "matches": matches, "runs": runs,
                  "balls_faced": balls, "fours": fours, "sixes": sixes}),
)

# 6. study_marks.csv: 60 students, hours studied vs marks ---------------------------
n = 60
hours = rng.uniform(0.5, 9.0, size=n).round(1)
attendance = np.clip(rng.normal(82, 9, size=n), 55, 100).round().astype(int)
marks = 4 + 6.4 * hours + 0.18 * attendance + rng.normal(0, 6, size=n)
marks = np.clip(marks, 5, 100).round().astype(int)
save_csv(
    "study_marks.csv",
    pd.DataFrame(
        {"student_id": range(1, n + 1), "hours_studied": hours, "attendance": attendance,
         "marks": marks, "result": np.where(marks >= 45, "Pass", "Fail")}
    ),
)

# 7. shop_customers.csv: 90 shoppers in three natural groups ------------------------
centres = [(3, 1.0), (12, 2.5), (7, 5.5)]  # (visits per month, spend in Rs. '000)
parts = []
for visits, spend in centres:
    parts.append(
        pd.DataFrame(
            {"monthly_visits": np.clip(rng.normal(visits, 1.3, 30), 1, None).round(1),
             "monthly_spend": np.clip(rng.normal(spend, 0.5, 30), 0.2, None).round(2)}
        )
    )
customers = pd.concat(parts, ignore_index=True).sample(frac=1, random_state=3).reset_index(drop=True)
customers.insert(0, "customer_id", range(1, len(customers) + 1))
save_csv("shop_customers.csv", customers)

# 8. api_response.json: what a small weather web API sends back ---------------------
api = {
    "city": "Pokhara",
    "country": "Nepal",
    "unit": "celsius",
    "forecast": [
        {"day": "Sun", "temp_max": 27, "temp_min": 17, "rain_mm": 0.0},
        {"day": "Mon", "temp_max": 26, "temp_min": 18, "rain_mm": 4.2},
        {"day": "Tue", "temp_max": 24, "temp_min": 17, "rain_mm": 12.5},
        {"day": "Wed", "temp_max": 23, "temp_min": 16, "rain_mm": 20.1},
        {"day": "Thu", "temp_max": 25, "temp_min": 17, "rain_mm": 6.8},
        {"day": "Fri", "temp_max": 28, "temp_min": 18, "rain_mm": 0.0},
        {"day": "Sat", "temp_max": 29, "temp_min": 19, "rain_mm": 0.5},
    ],
}
(DATA / "api_response.json").write_text(json.dumps(api, indent=2) + "\n")
print("wrote api_response.json")

# 9. One zip with everything, so students download once -----------------------------
zip_path = DATA / "course-data.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(DATA.iterdir()):
        if f.name != zip_path.name:
            z.write(f, f.name)
print(f"wrote {zip_path.name}")
