import json
import os
import requests
from datetime import datetime

# ================================================
#        RITHAM DAIRY FARM - FULL DASHBOARD
#        Built by: Sunny
#        Version: 1.0
# ================================================

# ---- ALL FARM DATA ----
farm = {
    "name": "Ritham Dairy Farm",
    "owner": "Sunny",
    "location": "Nashville, Tennessee",
    "established": 2020,
    "milk_price": 1.80,
    "lat": 36.1627,
    "lon": -86.7816,
    "low_stock_alert": 100,
}

cows = [
    {"name": "Bessie", "age": 3, "breed": "Holstein",  "daily_milk": 28, "is_healthy": True,  "barn": "A"},
    {"name": "Daisy",  "age": 5, "breed": "Jersey",    "daily_milk": 15, "is_healthy": False, "barn": "A"},
    {"name": "Rosie",  "age": 4, "breed": "Guernsey",  "daily_milk": 30, "is_healthy": True,  "barn": "B"},
    {"name": "Luna",   "age": 8, "breed": "Holstein",  "daily_milk": 18, "is_healthy": True,  "barn": "B"},
    {"name": "Bella",  "age": 2, "breed": "Jersey",    "daily_milk": 35, "is_healthy": True,  "barn": "C"},
    {"name": "Molly",  "age": 6, "breed": "Guernsey",  "daily_milk": 24, "is_healthy": False, "barn": "C"},
    {"name": "Ruby",   "age": 1, "breed": "Holstein",  "daily_milk": 32, "is_healthy": True,  "barn": "A"},
    {"name": "Pearl",  "age": 5, "breed": "Jersey",    "daily_milk": 26, "is_healthy": True,  "barn": "B"},
    {"name": "Clara",  "age": 2, "breed": "Jersey",    "daily_milk": 33, "is_healthy": True,  "barn": "B"},
    {"name": "Maggie", "age": 9, "breed": "Holstein",  "daily_milk": 14, "is_healthy": False, "barn": "A"},
]

products = [
    {"name": "Whole Milk", "price": 1.20, "stock": 500},
    {"name": "Butter",     "price": 4.50, "stock": 80},
    {"name": "Cheese",     "price": 6.00, "stock": 45},
    {"name": "Yogurt",     "price": 2.50, "stock": 200},
    {"name": "Ice Cream",  "price": 5.00, "stock": 30},
]

# ================================================
#                   FUNCTIONS
# ================================================

def print_header(title):
    print("\n" + "=" * 55)
    print(f"   {title}")
    print("=" * 55)

def print_section(title):
    print(f"\n--- {title} ---")

def get_weather():
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={farm['lat']}&longitude={farm['lon']}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation&temperature_unit=fahrenheit"
        response = requests.get(url, timeout=5)
        data = response.json()
        current = data["current"]
        return {
            "temperature": current["temperature_2m"],
            "humidity":    current["relative_humidity_2m"],
            "wind_speed":  current["wind_speed_10m"],
            "rain":        current["precipitation"],
            "success": True
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

def get_weather_advice(temp, humidity, rain):
    advice = []
    if temp > 90:
        advice.append("🌡️  HEAT ALERT - Move cows to shade immediately!")
    elif temp > 80:
        advice.append("☀️  Warm day - Increase water supply for cows")
    elif temp < 32:
        advice.append("🥶 FREEZE ALERT - Check all barn heating systems!")
    elif temp < 45:
        advice.append("❄️  Cold day - Make sure barns are insulated")
    else:
        advice.append("✅ Great weather for the cows today!")

    if humidity > 80:
        advice.append("💧 High humidity - Watch for heat stress signs")
    if rain > 0:
        advice.append("🌧️  Raining - Keep cows in barns")
    return advice

def check_cow_status(cow):
    if not cow["is_healthy"]:
        return "🚨 SICK"
    elif cow["age"] > 7 and cow["daily_milk"] < 20:
        return "⚠️  RETIRE"
    elif cow["daily_milk"] >= 30:
        return "⭐ STAR"
    elif cow["daily_milk"] >= 20:
        return "✅ GOOD"
    else:
        return "⚠️  LOW"

def get_grade(milk):
    if milk >= 30:   return "A"
    elif milk >= 25: return "B"
    elif milk >= 20: return "C"
    else:            return "D"

def get_barn_summary(cow_list):
    barns = {}
    for cow in cow_list:
        barn = cow["barn"]
        if barn not in barns:
            barns[barn] = {"cows": [], "total_milk": 0}
        barns[barn]["cows"].append(cow["name"])
        barns[barn]["total_milk"] += cow["daily_milk"]
    return barns

def check_stock(product):
    if product["stock"] < farm["low_stock_alert"] * 0.5:
        return "🚨 CRITICAL"
    elif product["stock"] < farm["low_stock_alert"]:
        return "⚠️  LOW"
    else:
        return "✅ OK"

def save_daily_report(data):
    # Save todays report
    filename = f"report_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    # Also save as latest report
    with open("latest_report.json", "w") as f:
        json.dump(data, f, indent=2)
    return filename

# ================================================
#                 MAIN DASHBOARD
# ================================================

now = datetime.now().strftime("%Y-%m-%d %H:%M")

print_header(f"RITHAM DAIRY FARM - DAILY DASHBOARD")
print(f"   Owner    : {farm['owner']}")
print(f"   Location : {farm['location']}")
print(f"   Date     : {now}")
print("=" * 55)

# ---- SECTION 1: WEATHER ----
print_header("🌤️  LIVE WEATHER - NASHVILLE")
weather = get_weather()

if weather["success"]:
    print(f"🌡️  Temperature : {weather['temperature']}°F")
    print(f"💧 Humidity    : {weather['humidity']}%")
    print(f"💨 Wind Speed  : {weather['wind_speed']} km/h")
    print(f"🌧️  Rain        : {weather['rain']} mm")

    print_section("Weather Advice")
    for advice in get_weather_advice(
        weather["temperature"],
        weather["humidity"],
        weather["rain"]
    ):
        print(f"  {advice}")
else:
    print("⚠️  Weather unavailable - running offline")

# ---- SECTION 2: COW REPORT ----
print_header("🐄 COW PRODUCTION REPORT")
print(f"{'Name':<10} {'Breed':<12} {'Age':<5} {'Milk':<8} {'Grade':<7} {'Barn':<6} Status")
print("-" * 55)

total_milk = 0
sick_cows = []
retire_cows = []
star_cows = []

for cow in cows:
    status = check_cow_status(cow)
    grade  = get_grade(cow["daily_milk"])
    total_milk += cow["daily_milk"]

    print(f"{cow['name']:<10} {cow['breed']:<12} {cow['age']:<5} {cow['daily_milk']:<8} {grade:<7} {cow['barn']:<6} {status}")

    if "SICK"   in status: sick_cows.append(cow["name"])
    if "RETIRE" in status: retire_cows.append(cow["name"])
    if "STAR"   in status: star_cows.append(cow["name"])

# ---- SECTION 3: BARN SUMMARY ----
print_header("🏚️  BARN SUMMARY")
barns = get_barn_summary(cows)
for barn_name, barn_data in barns.items():
    barn_rev = barn_data["total_milk"] * farm["milk_price"]
    print(f"Barn {barn_name}: {', '.join(barn_data['cows'])}")
    print(f"       Milk: {barn_data['total_milk']} liters | Revenue: ${barn_rev:.2f}/day")

# ---- SECTION 4: ALERTS ----
print_header("🚨 FARM ALERTS")

if sick_cows:
    print("🚨 SICK COWS - Call vet immediately!")
    for name in sick_cows:
        print(f"   → {name}")

if retire_cows:
    print("\n⚠️  RETIREMENT CANDIDATES")
    for name in retire_cows:
        print(f"   → {name}")

if star_cows:
    print("\n⭐ STAR PERFORMERS")
    for name in star_cows:
        print(f"   → {name}")

# ---- SECTION 5: INVENTORY ----
print_header("📦 PRODUCT INVENTORY")
print(f"{'Product':<15} {'Price':<8} {'Stock':<8} {'Value':<12} Status")
print("-" * 55)

total_inventory_value = 0
for product in products:
    status = check_stock(product)
    value  = product["price"] * product["stock"]
    total_inventory_value += value
    print(f"{product['name']:<15} ${product['price']:<7.2f} {product['stock']:<8} ${value:<11.2f} {status}")

print(f"\nTotal Inventory Value: ${total_inventory_value:.2f}")

# ---- SECTION 6: FINANCIAL SUMMARY ----
print_header("💰 FINANCIAL SUMMARY")
daily_rev   = total_milk * farm["milk_price"]
monthly_rev = daily_rev * 30
yearly_rev  = daily_rev * 365

# Expenses
monthly_feed    = len(cows) * 45
monthly_labor   = 8000
monthly_maint   = 2000
total_expenses  = monthly_feed + monthly_labor + monthly_maint
monthly_profit  = monthly_rev - total_expenses

print(f"{'REVENUE':}")
print(f"  Daily Revenue      : ${daily_rev:.2f}")
print(f"  Monthly Revenue    : ${monthly_rev:.2f}")
print(f"  Yearly Revenue     : ${yearly_rev:.2f}")
print(f"\n{'EXPENSES (Monthly)':}")
print(f"  Feed Cost          : ${monthly_feed:.2f}")
print(f"  Labor Cost         : ${monthly_labor:.2f}")
print(f"  Maintenance        : ${monthly_maint:.2f}")
print(f"  Total Expenses     : ${total_expenses:.2f}")
print(f"\n{'PROFIT':}")
print(f"  Monthly Profit     : ${monthly_profit:.2f}")
print(f"  Yearly Profit      : ${monthly_profit * 12:.2f}")

# ---- SECTION 7: SAVE REPORT ----
print_header("💾 SAVING REPORT")

report = {
    "date": now,
    "farm": farm["name"],
    "owner": farm["owner"],
    "weather": weather,
    "total_cows": len(cows),
    "total_milk": total_milk,
    "daily_revenue": daily_rev,
    "monthly_revenue": monthly_rev,
    "yearly_revenue": yearly_rev,
    "monthly_profit": monthly_profit,
    "sick_cows": sick_cows,
    "retire_cows": retire_cows,
    "star_cows": star_cows,
    "inventory_value": total_inventory_value,
}

filename = save_daily_report(report)
print(f"✅ Report saved to: {filename}")
print(f"✅ Latest report  : latest_report.json")

print_header("✅ DASHBOARD COMPLETE")
print(f"   Ritham Dairy Farm is being monitored!")
print(f"   Total Milk Today  : {total_milk} liters")
print(f"   Daily Revenue     : ${daily_rev:.2f}")
print(f"   Cows Need Vet     : {len(sick_cows)}")
print(f"   Star Performers   : {len(star_cows)}")
print("=" * 55)