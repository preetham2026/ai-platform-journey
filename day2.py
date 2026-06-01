# ---- LISTS ----
# A list stores multiple values in one variable

cows = ["Bessie", "Daisy", "Molly", "Rosie", "Luna"]
products = ["Whole Milk", "Butter", "Cheese", "Yogurt", "Ice Cream"]
daily_milk = [28, 25, 30, 22, 27]   # liters per cow

# Access single items (starts from 0!)
print("===== ACCESSING LIST ITEMS =====")
print("First cow:", cows[0])
print("Second cow:", cows[1])
print("Last cow:", cows[-1])       # -1 always means last item

# Check how many items
print("Total cows:", len(cows))
print("Total products:", len(products))

# Add and remove
print("\n===== ADDING & REMOVING =====")
cows.append("Bella")              # add to end
print("After adding Bella:", cows)

cows.remove("Molly")              # remove by name
print("After removing Molly:", cows)

# ---- LOOPS ----
print("\n===== ALL OUR COWS =====")
for cow in cows:
    print("🐄 Cow:", cow)

print("\n===== ALL OUR PRODUCTS =====")
for product in products:
    print("🥛 Product:", product)

# Loop with index number
print("\n===== MILK PRODUCTION =====")
for i in range(len(daily_milk)):
    print("Cow", i+1, "produces", daily_milk[i], "liters/day")

# ---- MATH IN LOOPS ----
print("\n===== TOTAL MILK =====")
total = 0
for liters in daily_milk:
    total = total + liters
print("Total milk from all cows:", total, "liters/day")
print("Monthly total:", total * 30, "liters")