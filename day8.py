import pandas as pd

# ---- CREATE A DATAFRAME ----
print("===== CREATING OUR FARM DATAFRAME =====")

data = {
    "name":       ["Bessie", "Daisy", "Rosie", "Luna", "Bella",
                   "Molly", "Ruby", "Pearl", "Clara", "Maggie"],
    "breed":      ["Holstein", "Jersey", "Guernsey", "Holstein", "Jersey",
                   "Guernsey", "Holstein", "Jersey", "Jersey", "Holstein"],
    "age":        [3, 5, 4, 8, 2, 6, 1, 5, 2, 9],
    "daily_milk": [28, 15, 30, 18, 35, 24, 32, 26, 33, 14],
    "is_healthy": [True, False, True, True, True, False, True, True, True, False],
    "barn":       ["A", "A", "B", "B", "C", "C", "A", "B", "B", "A"],
}

df = pd.DataFrame(data)
print(df)

# ---- BASIC INFO ----
print("\n===== DATAFRAME INFO =====")
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("Total cows:", len(df))

# ---- BASIC STATS ----
print("\n===== MILK STATISTICS =====")
print("Average milk:", df["daily_milk"].mean())
print("Highest milk:", df["daily_milk"].max())
print("Lowest milk :", df["daily_milk"].min())
print("Total milk  :", df["daily_milk"].sum())

# ---- FILTERING ----
print("\n===== HEALTHY COWS ONLY =====")
healthy = df[df["is_healthy"] == True]
print(healthy[["name", "daily_milk", "barn"]])

print("\n===== HIGH PRODUCERS (30+ liters) =====")
stars = df[df["daily_milk"] >= 30]
print(stars[["name", "breed", "daily_milk"]])

print("\n===== SICK COWS =====")
sick = df[df["is_healthy"] == False]
print(sick[["name", "age", "daily_milk"]])

# ---- ADDING NEW COLUMNS ----
print("\n===== ADDING CALCULATED COLUMNS =====")

milk_price = 1.50

df["daily_revenue"] = df["daily_milk"] * milk_price
df["monthly_revenue"] = df["daily_revenue"] * 30
df["grade"] = df["daily_milk"].apply(
    lambda x: "A" if x >= 30 else "B" if x >= 25 else "C" if x >= 20 else "D"
)

print(df[["name", "daily_milk", "grade", "daily_revenue", "monthly_revenue"]])

# ---- GROUP BY BARN ----
print("\n===== MILK BY BARN =====")
barn_stats = df.groupby("barn")["daily_milk"].agg(["sum", "mean", "count"])
barn_stats.columns = ["total_milk", "avg_milk", "num_cows"]
print(barn_stats)

# ---- GROUP BY BREED ----
print("\n===== MILK BY BREED =====")
breed_stats = df.groupby("breed")["daily_milk"].agg(["sum", "mean", "max"])
breed_stats.columns = ["total_milk", "avg_milk", "best_cow"]
print(breed_stats)

# ---- SORT DATA ----
print("\n===== TOP PRODUCERS (sorted) =====")
top = df.sort_values("daily_milk", ascending=False)
print(top[["name", "breed", "daily_milk", "grade"]].head(5))

print("\n===== BOTTOM PRODUCERS (sorted) =====")
bottom = df.sort_values("daily_milk", ascending=True)
print(bottom[["name", "breed", "daily_milk", "grade"]].head(3))

# ---- SAVE TO CSV ----
print("\n===== SAVING TO CSV =====")
df.to_csv("farm_data.csv", index=False)
print("✅ farm_data.csv saved!")

df_loaded = pd.read_csv("farm_data.csv")
print(f"✅ Loaded back {len(df_loaded)} cows from CSV")

# ---- SUMMARY STATS ----
print("\n===== FULL FARM STATISTICS =====")
print(df[["age", "daily_milk", "daily_revenue"]].describe())