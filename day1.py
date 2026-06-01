# ---- MY PROFILE ----
name = "Preetham"
current_role = "DevOps Engineer"
target_role = "AI Platform Engineer"
years_experience = 8
target_salary = 180000

# ---- PRINT MY PROFILE ----
print("===== MY PROFILE =====")
print("Name:", name)
print("Current Role:", current_role)
print("Target Role:", target_role)
print("Years of Experience:", years_experience)
print("Target Salary: $", target_salary)

# ---- MATH WITH VARIABLES ----
print("\n===== SALARY MATH =====")
tax = target_salary * 0.25
take_home = target_salary - tax
print("Gross Salary: $", target_salary)
print("Tax (25%): $", tax)
print("Take Home: $", take_home)

# ---- STRING TRICKS ----
print("\n===== STRING TRICKS =====")
print(target_role.upper())
print(target_role.lower())
print("Total characters in my target role:", len(target_role))
print("My goal: I am", name, "and I will become a", target_role)