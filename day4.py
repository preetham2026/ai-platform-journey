# ---- IF/ELSE — Making Decisions ----

daily_milk = 28
age = 7
is_healthy = True

# Basic if/else
print("===== COW HEALTH CHECK =====")
if daily_milk >= 30:
    print("✅ Excellent production!")
elif daily_milk >= 25:
    print("👍 Good production")
elif daily_milk >= 20:
    print("⚠️ Below average production")
else:
    print("🚨 Poor production - needs attention!")

# Multiple conditions
print("\n===== AGE & HEALTH CHECK =====")
if age > 6 and daily_milk < 25:
    print("🚨 Old cow with low production - consider retiring")
elif age > 6 and daily_milk >= 25:
    print("⭐ Experienced cow still performing well!")
elif age <= 2 and daily_milk >= 28:
    print("🌟 Young high performer - great investment!")
else:
    print("✅ Cow is in normal range")

# Check health status
print("\n===== HEALTH STATUS =====")
if is_healthy:
    print("✅ Cow is healthy")
else:
    print("🚨 Cow needs veterinary attention!")

# ---- ERROR HANDLING ----
print("\n===== ERROR HANDLING =====")

# Without error handling — this would CRASH
# result = 100 / 0  # ZeroDivisionError!

# With error handling — safe!
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("❌ Cannot divide by zero!")
        return 0

def get_cow_age(age_input):
    try:
        age = int(age_input)
        if age < 0 or age > 25:
            print("❌ Invalid age! Must be between 0 and 25")
            return None
        return age
    except ValueError:
        print("❌ Age must be a number, not:", age_input)
        return None

# Test safe divide
print("100 / 4 =", safe_divide(100, 4))
print("100 / 0 =", safe_divide(100, 0))

# Test age validation
print("\nTesting ages:")
print("Age 5:", get_cow_age(5))
print("Age -1:", get_cow_age(-1))
print("Age 'abc':", get_cow_age("abc"))
print("Age 30:", get_cow_age(30))