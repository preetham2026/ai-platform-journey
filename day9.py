import pandas as pd
import matplotlib.pyplot as plt

# ---- FARM DATA ----
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
milk_price = 1.50
df["daily_revenue"] = df["daily_milk"] * milk_price
df["grade"] = df["daily_milk"].apply(
    lambda x: "A" if x >= 30 else "B" if x >= 25 else "C" if x >= 20 else "D"
)

# ---- COLORS ----
colors = {
    "A": "#2ecc71",   # green
    "B": "#3498db",   # blue
    "C": "#f39c12",   # orange
    "D": "#e74c3c",   # red
}
bar_colors = [colors[g] for g in df["grade"]]

# ================================================
# CHART 1 — Milk Production by Cow (Bar Chart)
# ================================================
plt.figure(figsize=(12, 6))
bars = plt.bar(df["name"], df["daily_milk"], color=bar_colors, edgecolor="black")

# Add value labels on top of bars
for bar, milk in zip(bars, df["daily_milk"]):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             str(milk), ha="center", va="bottom", fontweight="bold")

plt.title("🐄 Ritham Dairy Farm - Daily Milk Production by Cow", 
          fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Cow Name", fontsize=12)
plt.ylabel("Milk (liters/day)", fontsize=12)
plt.axhline(y=df["daily_milk"].mean(), color="purple", 
            linestyle="--", label=f"Average: {df['daily_milk'].mean():.1f} liters")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart1_milk_production.png")
plt.show()
print("✅ Chart 1 saved!")

# ================================================
# CHART 2 — Milk by Breed (Pie Chart)
# ================================================
breed_milk = df.groupby("breed")["daily_milk"].sum()

plt.figure(figsize=(8, 8))
plt.pie(breed_milk.values,
        labels=breed_milk.index,
        autopct="%1.1f%%",
        colors=["#e74c3c", "#3498db", "#2ecc71"],
        explode=[0.05, 0.05, 0.05],
        shadow=True,
        startangle=90)

plt.title("🥛 Milk Production by Breed", 
          fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("chart2_breed_pie.png")
plt.show()
print("✅ Chart 2 saved!")

# ================================================
# CHART 3 — Revenue by Cow (Horizontal Bar)
# ================================================
df_sorted = df.sort_values("daily_revenue", ascending=True)

plt.figure(figsize=(10, 7))
bars = plt.barh(df_sorted["name"], df_sorted["daily_revenue"],
                color=[colors[g] for g in df_sorted["grade"]],
                edgecolor="black")

for bar, rev in zip(bars, df_sorted["daily_revenue"]):
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
             f"${rev:.2f}", va="center", fontweight="bold")

plt.title("💰 Daily Revenue by Cow", fontsize=14, fontweight="bold")
plt.xlabel("Daily Revenue ($)", fontsize=12)
plt.ylabel("Cow Name", fontsize=12)
plt.tight_layout()
plt.savefig("chart3_revenue.png")
plt.show()
print("✅ Chart 3 saved!")

# ================================================
# CHART 4 — Barn Performance (Grouped Bar)
# ================================================
barn_stats = df.groupby("barn").agg(
    total_milk=("daily_milk", "sum"),
    avg_milk=("daily_milk", "mean"),
    num_cows=("name", "count")
).reset_index()

x = range(len(barn_stats))
width = 0.35

plt.figure(figsize=(10, 6))
plt.bar([i - width/2 for i in x], barn_stats["total_milk"],
        width, label="Total Milk", color="#3498db", edgecolor="black")
plt.bar([i + width/2 for i in x], barn_stats["avg_milk"],
        width, label="Avg Milk", color="#2ecc71", edgecolor="black")

plt.title("🏚️  Barn Performance Comparison", fontsize=14, fontweight="bold")
plt.xlabel("Barn", fontsize=12)
plt.ylabel("Milk (liters)", fontsize=12)
plt.xticks(x, [f"Barn {b}" for b in barn_stats["barn"]])
plt.legend()
plt.tight_layout()
plt.savefig("chart4_barn_performance.png")
plt.show()
print("✅ Chart 4 saved!")

# ================================================
# CHART 5 — Age vs Milk Scatter Plot
# ================================================
plt.figure(figsize=(10, 6))

for _, row in df.iterrows():
    color = "#2ecc71" if row["is_healthy"] else "#e74c3c"
    plt.scatter(row["age"], row["daily_milk"], 
                color=color, s=200, edgecolor="black", zorder=5)
    plt.annotate(row["name"],
                 (row["age"], row["daily_milk"]),
                 textcoords="offset points",
                 xytext=(8, 4), fontsize=9)

plt.title("📊 Age vs Milk Production\n(Green=Healthy, Red=Sick)",
          fontsize=14, fontweight="bold")
plt.xlabel("Age (years)", fontsize=12)
plt.ylabel("Daily Milk (liters)", fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("chart5_age_vs_milk.png")
plt.show()
print("✅ Chart 5 saved!")

print("\n🎉 All 5 charts saved to your folder!")
print("Check your ai-platform-journey folder for PNG files!")