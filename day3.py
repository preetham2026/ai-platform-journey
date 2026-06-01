# ---- DICTIONARIES ----
# Instead of 2 separate lists, store everything together!

# A dictionary holds key:value pairs
cow = {
    "name": "Maggie",
    "age": 4,
    "breed": "Holstein",
    "daily_milk": 31,
    "is_healthy": True
}

# Access values by key
print("===== COW DETAILS =====")
print("Name:", cow["name"])
print("Age:", cow["age"])
print("Breed:", cow["breed"])
print("Daily Milk:", cow["daily_milk"], "liters")
print("Healthy:", cow["is_healthy"])

# Update a value
cow["daily_milk"] = 35
print("\nAfter update:")
print("New milk production:", cow["daily_milk"], "liters")

# Add a new key
cow["location"] = "Barn A"
print("Location:", cow["location"])

# ---- DICTIONARY INSIDE A LIST ----
# This is how real apps store data!
print("\n===== ALL COWS =====")
cows = [
    {"name": "Bessie", "age": 3, "daily_milk": 28},
    {"name": "Daisy",  "age": 5, "daily_milk": 25},
    {"name": "Clara",  "age": 2, "daily_milk": 33},
    {"name": "Maggie", "age": 4, "daily_milk": 31},
]

for cow in cows:
    print(f"🐄 {cow['name']:<10} | Age: {cow['age']} | Milk: {cow['daily_milk']} liters")

# ---- FUNCTIONS ----
print("\n===== FUNCTIONS =====")

# A function is reusable code
def calculate_daily_revenue(milk_liters, price_per_liter):
    revenue = milk_liters * price_per_liter
    return revenue

def get_best_cow(cow_list):
    best = cow_list[0]
    for cow in cow_list:
        if cow["daily_milk"] > best["daily_milk"]:
            best = cow
    return best

def print_cow_report(cow, price):
    revenue = calculate_daily_revenue(cow["daily_milk"], price)
    print(f"🐄 {cow['name']:<10} | {cow['daily_milk']} liters | ${revenue:.2f}/day")

# Call the functions
price = 0.80
print("Daily revenues:")
for cow in cows:
    print_cow_report(cow, price)

best = get_best_cow(cows)
print(f"\n🏆 Best cow is {best['name']} with {best['daily_milk']} liters/day!")