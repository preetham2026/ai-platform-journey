# ---- DAIRY FARM BUSINESS TRACKER ----

# Farm info
farm_name = "Ritham Dairy Farm"
owner = "Sunny"
location = "Nashville, Tennessee"
established_year = 2020

# Farm stats
total_cows = 150
daily_milk_per_cow = 25    # liters per cow per day
milk_price_per_liter = 0.80  # dollars

# ---- PRODUCTION MATH ----
daily_milk_total = total_cows * daily_milk_per_cow
monthly_milk_total = daily_milk_total * 30

# ---- REVENUE MATH ----
daily_revenue = daily_milk_total * milk_price_per_liter
monthly_revenue = daily_revenue * 30
yearly_revenue = monthly_revenue * 12

# ---- EXPENSES ----
monthly_feed_cost = total_cows * 45     # $45 per cow per month
monthly_labor_cost = 8000
monthly_maintenance = 2000
total_monthly_expenses = monthly_feed_cost + monthly_labor_cost + monthly_maintenance

# ---- PROFIT ----
monthly_profit = monthly_revenue - total_monthly_expenses
yearly_profit = monthly_profit * 12

# ---- PRINT REPORT ----
print("========================================")
print("   DAIRY FARM BUSINESS REPORT")
print("========================================")
print("Farm Name  :", farm_name)
print("Owner      :", owner)
print("Location   :", location)
print("Established:", established_year)

print("\n-------- PRODUCTION --------")
print("Total Cows            :", total_cows)
print("Milk Per Cow/Day      :", daily_milk_per_cow, "liters")
print("Total Milk/Day        :", daily_milk_total, "liters")
print("Total Milk/Month      :", monthly_milk_total, "liters")

print("\n-------- REVENUE --------")
print("Milk Price            : $", milk_price_per_liter, "per liter")
print("Daily Revenue         : $", daily_revenue)
print("Monthly Revenue       : $", monthly_revenue)
print("Yearly Revenue        : $", yearly_revenue)

print("\n-------- EXPENSES --------")
print("Feed Cost/Month       : $", monthly_feed_cost)
print("Labor Cost/Month      : $", monthly_labor_cost)
print("Maintenance/Month     : $", monthly_maintenance)
print("Total Expenses/Month  : $", total_monthly_expenses)

print("\n-------- PROFIT --------")
print("Monthly Profit        : $", monthly_profit)
print("Yearly Profit         : $", yearly_profit)
print("========================================")