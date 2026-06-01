import json
import os
import requests
from datetime import datetime

# ---- FARM DATA ----
farm = {
    "name": "Ritham Dairy Farm",
    "owner": "Sunny",
    "location": "Nashville, Tennessee",
    "milk_price": 0.80,
    "lat": 36.1627,
    "lon": -86.7816
}

cows = [
    {"name": "Bessie", "age": 3, "daily_milk": 28, "is_healthy": True},
    {"name": "Daisy",  "age": 5, "daily_milk": 15, "is_healthy": False},
    {"name": "Rosie",  "age": 4, "daily_milk": 30, "is_healthy": True},
    {"name": "Luna",   "age": 8, "daily_milk": 18, "is_healthy": True},
    {"name": "Bella",  "age": 2, "daily_milk": 35, "is_healthy": True},
    {"name": "Molly",  "age": 6, "daily_milk": 24, "is_healthy": False},
    {"name": "Ruby",   "age": 1, "daily_milk": 32, "is_healthy": True},
    {"name": "Pearl",  "age": 5, "daily_milk": 26, "is_healthy": True},
    {"name": "Clara",  "age": 2, "daily_milk": 33, "is_healthy": True},
    {"name": "Maggie", "age": 9, "daily_milk": 14, "is_healthy": False},
]

# ---- FUNCTIONS ----
def print_header(title):
    print("\n" + "=" * 50)
    print(f"   {title}")
    print("=" * 50)

def get_weather(lat, lon):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&temperature_unit=fahrenheit"
        response = requests.get(url, timeout=5)
        data = response.json()
        current = data["current"]
        return {
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind_speed": current["wind_speed_10m"],
            "success": True
        }
    except Exception as e:
        print(f"❌ Weather API error: {e}")
        return {"success": False}

def get_weather_alert(temp, humidity):
    alerts = []
    if temp > 90:
        alerts.append("🌡️  HEAT ALERT - Move cows to shade, increase water!")
    elif temp > 80:
        alerts.append("☀️  Warm day - Monitor cow hydration")
    elif temp < 32:
        alerts.append("🥶 FREEZE ALERT - Check barn heating!")
    elif temp < 45:
        alerts.append("❄️  Cold day - Ensure barn is warm")
    else:
        alerts.append("✅ Temperature is comfortable for cows")

    if humidity > 80:
        alerts.append("💧 High humidity - Watch for heat stress")
    elif humidity < 30:
        alerts.append("🌵 Low humidity - Ensure water access")

    return alerts

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

def save_report(report_data):
    filename = "daily_report.json"
    with open(filename, "w") as f:
        json.dump(report_data, f, indent=2)
    print(f"\n✅ Report saved to {filename}")

# ---- GET WEATHER ----
print_header("🌤️  NASHVILLE WEATHER CHECK")
weather = get_weather(farm["lat"], farm["lon"])

if weather["success"]:
    print(f"🌡️  Temperature : {weather['temperature']}°F")
    print(f"💧 Humidity    : {weather['humidity']}%")
    print(f"💨 Wind Speed  : {weather['wind_speed']} km/h")

    print("\n--- Weather Alerts ---")
    alerts = get_weather_alert(
        weather["temperature"],
        weather["humidity"]
    )
    for alert in alerts:
        print(alert)
else:
    print("⚠️  Could not fetch weather - using offline mode")

# ---- COW REPORT ----
print_header("🐄 COW STATUS REPORT")
total_milk = 0
sick_cows = []
star_cows = []

for cow in cows:
    status = check_cow_status(cow)
    total_milk += cow["daily_milk"]
    print(f"🐄 {cow['name']:<8} | {cow['daily_milk']} liters | {status}")

    if "SICK" in status:
        sick_cows.append(cow["name"])
    if "STAR" in status:
        star_cows.append(cow["name"])

# ---- SUMMARY ----
print_header("📊 DAILY SUMMARY")
daily_rev = total_milk * farm["milk_price"]
today = datetime.now().strftime("%Y-%m-%d %H:%M")

print(f"Date & Time     : {today}")
print(f"Total Milk/Day  : {total_milk} liters")
print(f"Daily Revenue   : ${daily_rev:.2f}")
print(f"Monthly Revenue : ${daily_rev * 30:.2f}")
print(f"Yearly Revenue  : ${daily_rev * 365:.2f}")
print(f"Sick Cows       : {len(sick_cows)}")
print(f"Star Cows       : {len(star_cows)}")

# ---- SAVE REPORT TO FILE ----
report = {
    "date": today,
    "farm": farm["name"],
    "owner": farm["owner"],
    "weather": weather,
    "total_milk": total_milk,
    "daily_revenue": daily_rev,
    "sick_cows": sick_cows,
    "star_cows": star_cows,
}

save_report(report)
print_header("✅ DAY 5 COMPLETE!")
print("Your farm report is saved and weather is live!")
print("=" * 50)