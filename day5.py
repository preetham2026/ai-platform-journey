import json
import os

# ---- WRITING TO FILES ----
print("===== WRITING FILES =====")

# Write a simple text file
with open("farm_log.txt", "w") as f:
    f.write("Ritham Dairy Farm - Daily Log\n")
    f.write("Date: June 2026\n")
    f.write("Total Cows: 10\n")
    f.write("Total Milk: 255 liters\n")
    f.write("Daily Revenue: $204.00\n")

print("✅ farm_log.txt created!")

# Read it back
print("\n===== READING FILES =====")
with open("farm_log.txt", "r") as f:
    content = f.read()
    print(content)

# ---- JSON FILES ----
print("===== SAVING JSON =====")

# Save farm data as JSON
farm_data = {
    "farm_name": "Ritham Dairy Farm",
    "owner": "Sunny",
    "milk_price": 0.80,
    "cows": [
        {"name": "Bessie", "daily_milk": 28},
        {"name": "Clara",  "daily_milk": 33},
        {"name": "Bella",  "daily_milk": 35},
    ]
}

with open("farm_data.json", "w") as f:
    json.dump(farm_data, f, indent=2)

print("✅ farm_data.json saved!")

# Load it back
print("\n===== LOADING JSON =====")
with open("farm_data.json", "r") as f:
    loaded = json.load(f)

print("Farm:", loaded["farm_name"])
print("Owner:", loaded["owner"])
print("Cows:")
for cow in loaded["cows"]:
    print(f"  🐄 {cow['name']} - {cow['daily_milk']} liters/day")

# ---- CHECK IF FILE EXISTS ----
print("\n===== FILE CHECKS =====")
files = ["farm_log.txt", "farm_data.json", "missing_file.txt"]
for file in files:
    if os.path.exists(file):
        print(f"✅ {file} exists")
    else:
        print(f"❌ {file} not found")