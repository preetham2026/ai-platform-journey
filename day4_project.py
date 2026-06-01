# ---- RITHAM DAIRY FARM - SMART ALERT SYSTEM ----

farm = {
    "name": "Ritham Dairy Farm",
    "owner": "Sunny",
    "milk_price": 0.80,
    "low_stock_alert": 100,    # alert if stock below this
    "low_milk_alert": 20,      # alert if cow below this
}

cows = [
    {"name": "Bessie", "age": 3, "breed": "Holstein", "daily_milk": 28, "is_healthy": True,  "barn": "A"},
    {"name": "Daisy",  "age": 5, "breed": "Jersey",   "daily_milk": 15, "is_healthy": False, "barn": "A"},
    {"name": "Rosie",  "age": 4, "breed": "Guernsey", "daily_milk": 30, "is_healthy": True,  "barn": "B"},
    {"name": "Luna",   "age": 8, "breed": "Holstein", "daily_milk": 18, "is_healthy": True,  "barn": "B"},
    {"name": "Bella",  "age": 2, "breed": "Jersey",   "daily_milk": 35, "is_healthy": True,  "barn": "C"},
    {"name": "Molly",  "age": 6, "breed": "Guernsey", "daily_milk": 24, "is_healthy": False, "barn": "C"},
    {"name": "Ruby",   "age": 1, "breed": "Holstein", "daily_milk": 32, "is_healthy": True,  "barn": "A"},
    {"name": "Pearl",  "age": 5, "breed": "Jersey",   "daily_milk": 26, "is_healthy": True,  "barn": "B"},
    {"name": "Clara",  "age": 2, "breed": "Jersey",   "daily_milk": 33, "is_healthy": True,  "barn": "B"},
    {"name": "Maggie", "age": 9, "breed": "Holstein", "daily_milk": 14, "is_healthy": False, "barn": "A"},
]

products = [
    {"name": "Whole Milk", "price": 1.20, "stock": 500},
    {"name": "Butter",     "price": 4.50, "stock": 80},
    {"name": "Cheese",     "price": 6.00, "stock": 45},
    {"name": "Yogurt",     "price": 2.50, "stock": 200},
    {"name": "Ice Cream",  "price": 5.00, "stock": 30},
]

# ---- FUNCTIONS ----
def print_header(title):
    print("\n" + "=" * 50)
    print(f"   {title}")
    print("=" * 50)

def check_cow_status(cow):
    # Returns a status emoji based on cow data
    if not cow["is_healthy"]:
        return "🚨 SICK"
    elif cow["age"] > 7 and cow["daily_milk"] < 20:
        return "⚠️ RETIRE"
    elif cow["daily_milk"] >= 30:
        return "⭐ STAR"
    elif cow["daily_milk"] >= 20:
        return "✅ GOOD"
    else:
        return "⚠️ LOW"

def get_production_grade(milk):
    if milk >= 30:
        return "A"
    elif milk >= 25:
        return "B"
    elif milk >= 20:
        return "C"
    else:
        return "D"

def check_stock_alert(product, min_stock):
    if product["stock"] < min_stock:
        return f"🚨 LOW STOCK"
    elif product["stock"] < min_stock * 1.5:
        return f"⚠️  ORDER SOON"
    else:
        return f"✅ OK"

def calculate_revenue(milk, price):
    return milk * price

# ---- COW REPORT WITH ALERTS ----
print_header("RITHAM DAIRY FARM - SMART REPORT")
print(f"Owner: {farm['owner']}")

print_header("COW STATUS REPORT")
sick_cows = []
retire_cows = []
star_cows = []

for cow in cows:
    status = check_cow_status(cow)
    grade = get_production_grade(cow["daily_milk"])
    rev = calculate_revenue(cow["daily_milk"], farm["milk_price"])
    print(f"🐄 {cow['name']:<8} | Grade {grade} | {cow['daily_milk']} liters | ${rev:.2f}/day | {status}")

    # Collect alerts
    if "SICK" in status:
        sick_cows.append(cow["name"])
    elif "RETIRE" in status:
        retire_cows.append(cow["name"])
    elif "STAR" in status:
        star_cows.append(cow["name"])

# ---- ALERTS ----
print_header("🚨 FARM ALERTS")

if sick_cows:
    print(f"🚨 SICK COWS - Call the vet immediately!")
    for name in sick_cows:
        print(f"   → {name} needs medical attention")

if retire_cows:
    print(f"\n⚠️  RETIREMENT CANDIDATES")
    for name in retire_cows:
        print(f"   → {name} is old with low production")

if star_cows:
    print(f"\n⭐ STAR PERFORMERS - Keep these healthy!")
    for name in star_cows:
        print(f"   → {name} is performing excellently")

# ---- PRODUCT ALERTS ----
print_header("📦 INVENTORY ALERTS")
for product in products:
    status = check_stock_alert(product, farm["low_stock_alert"])
    print(f"🥛 {product['name']:<15} | Stock: {product['stock']:<5} | {status}")

# ---- OVERALL SUMMARY ----
print_header("📊 FARM SUMMARY")
total_milk = sum(cow["daily_milk"] for cow in cows)
healthy_cows = sum(1 for cow in cows if cow["is_healthy"])
daily_rev = calculate_revenue(total_milk, farm["milk_price"])

print(f"Total Cows      : {len(cows)}")
print(f"Healthy Cows    : {healthy_cows}")
print(f"Sick Cows       : {len(sick_cows)}")
print(f"Total Milk/Day  : {total_milk} liters")
print(f"Daily Revenue   : ${daily_rev:.2f}")
print(f"Monthly Revenue : ${daily_rev * 30:.2f}")
print(f"Yearly Revenue  : ${daily_rev * 365:.2f}")
print("=" * 50)