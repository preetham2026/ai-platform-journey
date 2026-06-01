# ---- RITHAM DAIRY FARM - FULL TRACKER ----

farm_name = "Ritham Dairy Farm"
owner = "Sunny"

# Farm data
cow_names = ["Bessie", "Daisy", "Rosie", "Luna", "Bella", 
             "Molly", "Ruby", "Pearl", "Lola", "Maggie","clara"]

daily_milk_liters = [28, 25, 30, 22, 27, 
                     24, 29, 26, 23, 31,33]

milk_price = 0.80

# Products we sell
products = ["Whole Milk", "Butter", "Cheese", "Yogurt", "Ice Cream"]
product_prices = [1.20, 4.50, 6.00, 2.50, 5.00]

# ---- PRINT FARM HEADER ----
print("==========================================")
print("       RITHAM DAIRY FARM REPORT")
print("       Owner:", owner)
print("==========================================")

# ---- PRINT ALL COWS AND THEIR MILK ----
print("\n-------- COW PRODUCTION REPORT --------")
total_milk = 0
best_cow = cow_names[0]
best_milk = daily_milk_liters[0]

for i in range(len(cow_names)):
    milk = daily_milk_liters[i]
    revenue = milk * milk_price
    print(f"🐄 {cow_names[i]:<10} | {milk} liters/day | ${revenue:.2f}/day")
    total_milk = total_milk + milk

    # Find best cow
    if milk > best_milk:
        best_milk = milk
        best_cow = cow_names[i]

# ---- PRODUCTION SUMMARY ----
print("\n-------- PRODUCTION SUMMARY --------")
print("Total Cows          :", len(cow_names))
print("Total Milk/Day      :", total_milk, "liters")
print("Total Milk/Month    :", total_milk * 30, "liters")
print("Best Cow            :", best_cow, "with", best_milk, "liters/day")

# ---- REVENUE ----
daily_revenue = total_milk * milk_price
monthly_revenue = daily_revenue * 30
yearly_revenue = monthly_revenue * 12

print("\n-------- REVENUE --------")
print(f"Daily Revenue       : ${daily_revenue:.2f}")
print(f"Monthly Revenue     : ${monthly_revenue:.2f}")
print(f"Yearly Revenue      : ${yearly_revenue:.2f}")

# ---- PRODUCTS WE SELL ----
print("\n-------- PRODUCTS & PRICES --------")
for i in range(len(products)):
    print(f"🥛 {products[i]:<15} : ${product_prices[i]:.2f}")

# ---- FIND MOST EXPENSIVE PRODUCT ----
most_expensive = products[0]
highest_price = product_prices[0]

for i in range(len(products)):
    if product_prices[i] > highest_price:
        highest_price = product_prices[i]
        most_expensive = products[i]

print("\n🏆 Most Expensive Product:", most_expensive, "at $", highest_price)
print("==========================================")