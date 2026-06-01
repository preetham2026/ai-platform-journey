# ---- RITHAM DAIRY FARM - UPGRADED WITH DICTIONARIES ----

farm = {
    "name": "Ritham Dairy Farm",
    "owner": "Sunny",
    "location": "Nashville, Tennessee",
    "established": 2020,
    "milk_price": 0.80
}

cows = [
    {"name": "Bessie", "age": 3, "breed": "Holstein",  "daily_milk": 28, "barn": "A"},
    {"name": "Daisy",  "age": 5, "breed": "Jersey",    "daily_milk": 25, "barn": "A"},
    {"name": "Rosie",  "age": 4, "breed": "Guernsey",  "daily_milk": 30, "barn": "B"},
    {"name": "Luna",   "age": 2, "breed": "Holstein",  "daily_milk": 22, "barn": "B"},
    {"name": "Bella",  "age": 6, "breed": "Jersey",    "daily_milk": 27, "barn": "C"},
    {"name": "Molly",  "age": 3, "breed": "Guernsey",  "daily_milk": 24, "barn": "C"},
    {"name": "Ruby",   "age": 4, "breed": "Holstein",  "daily_milk": 29, "barn": "A"},
    {"name": "Pearl",  "age": 5, "breed": "Jersey",    "daily_milk": 26, "barn": "B"},
    {"name": "Lola",   "age": 2, "breed": "Guernsey",  "daily_milk": 23, "barn": "C"},
    {"name": "Maggie", "age": 4, "breed": "Holstein",  "daily_milk": 31, "barn": "A"},
    {"name": "Clara",  "age": 2, "breed": "Jersey",    "daily_milk": 33, "barn": "B"},
]

products = [
    {"name": "Whole Milk",  "price": 1.20, "stock": 500},
    {"name": "Butter",      "price": 4.50, "stock": 120},
    {"name": "Cheese",      "price": 6.00, "stock": 80},
    {"name": "Yogurt",      "price": 2.50, "stock": 200},
    {"name": "Ice Cream",   "price": 5.00, "stock": 150},
]

# ---- FUNCTIONS ----
def print_header(title):
    print("\n" + "=" * 45)
    print(f"   {title}")
    print("=" * 45)

def calculate_revenue(milk, price):
    return milk * price

def get_best_cow(cow_list):
    best = cow_list[0]
    for cow in cow_list:
        if cow["daily_milk"] > best["daily_milk"]:
            best = cow
    return best

def get_cows_by_barn(cow_list, barn):
    result = []
    for cow in cow_list:
        if cow["barn"] == barn:
            result.append(cow["name"])
    return result

def get_total_milk(cow_list):
    total = 0
    for cow in cow_list:
        total = total + cow["daily_milk"]
    return total

# ---- FARM HEADER ----
print_header("RITHAM DAIRY FARM REPORT")
print(f"Owner    : {farm['owner']}")
print(f"Location : {farm['location']}")
print(f"Est.     : {farm['established']}")

# ---- COW REPORT ----
print_header("COW PRODUCTION REPORT")
for cow in cows:
    rev = calculate_revenue(cow["daily_milk"], farm["milk_price"])
    print(f"🐄 {cow['name']:<8} | {cow['breed']:<10} | Barn {cow['barn']} | {cow['daily_milk']} liters | ${rev:.2f}/day")

# ---- BARN REPORT ----
print_header("COWS BY BARN")
for barn in ["A", "B", "C"]:
    barn_cows = get_cows_by_barn(cows, barn)
    print(f"Barn {barn}: {', '.join(barn_cows)}")

# ---- SUMMARY ----
print_header("PRODUCTION SUMMARY")
total_milk = get_total_milk(cows)
daily_rev = calculate_revenue(total_milk, farm["milk_price"])
best = get_best_cow(cows)

print(f"Total Cows       : {len(cows)}")
print(f"Total Milk/Day   : {total_milk} liters")
print(f"Total Milk/Month : {total_milk * 30} liters")
print(f"Daily Revenue    : ${daily_rev:.2f}")
print(f"Monthly Revenue  : ${daily_rev * 30:.2f}")
print(f"Yearly Revenue   : ${daily_rev * 365:.2f}")
print(f"🏆 Best Cow      : {best['name']} ({best['daily_milk']} liters/day)")

# ---- PRODUCTS ----
print_header("PRODUCTS & STOCK")
for product in products:
    value = product["price"] * product["stock"]
    print(f"🥛 {product['name']:<15} | ${product['price']:.2f} | Stock: {product['stock']} | Value: ${value:.2f}")

print("\n" + "=" * 45)