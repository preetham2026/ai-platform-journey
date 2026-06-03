# ================================================
#         RITHAM DAIRY FARM - OOP VERSION
# ================================================

class Cow:
    # This runs when you create a new cow
    def __init__(self, name, age, breed, daily_milk, barn, is_healthy=True):
        self.name       = name
        self.age        = age
        self.breed      = breed
        self.daily_milk = daily_milk
        self.barn       = barn
        self.is_healthy = is_healthy
        self.milk_price = 1.50

    # Calculate revenue
    def get_daily_revenue(self):
        return self.daily_milk * self.milk_price

    def get_monthly_revenue(self):
        return self.get_daily_revenue() * 30

    # Get grade
    def get_grade(self):
        if self.daily_milk >= 30:   return "A"
        elif self.daily_milk >= 25: return "B"
        elif self.daily_milk >= 20: return "C"
        else:                       return "D"

    # Get status
    def get_status(self):
        if not self.is_healthy:
            return "🚨 SICK"
        elif self.age > 7 and self.daily_milk < 20:
            return "⚠️  RETIRE"
        elif self.daily_milk >= 30:
            return "⭐ STAR"
        elif self.daily_milk >= 20:
            return "✅ GOOD"
        else:
            return "⚠️  LOW"

    # Actions
    def heal(self):
        self.is_healthy = True
        print(f"✅ {self.name} has been healed!")

    def increase_milk(self, amount):
        self.daily_milk += amount
        print(f"📈 {self.name} now produces {self.daily_milk} liters/day!")

    # Print cow info
    def __str__(self):
        return (f"🐄 {self.name:<10} | {self.breed:<10} | "
                f"Age: {self.age} | Milk: {self.daily_milk}L | "
                f"Grade: {self.get_grade()} | {self.get_status()}")


class Farm:
    def __init__(self, name, owner, location):
        self.name     = name
        self.owner    = owner
        self.location = location
        self.cows     = []
        self.products = []

    # Add a cow
    def add_cow(self, cow):
        self.cows.append(cow)
        print(f"✅ {cow.name} added to {self.name}!")

    # Remove a cow
    def remove_cow(self, name):
        for cow in self.cows:
            if cow.name == name:
                self.cows.remove(cow)
                print(f"❌ {name} removed from farm")
                return
        print(f"⚠️  {name} not found!")

    # Get all sick cows
    def get_sick_cows(self):
        return [cow for cow in self.cows if not cow.is_healthy]

    # Get star cows
    def get_star_cows(self):
        return [cow for cow in self.cows if cow.daily_milk >= 30]

    # Get cows by barn
    def get_barn_cows(self, barn):
        return [cow for cow in self.cows if cow.barn == barn]

    # Get best cow
    def get_best_cow(self):
        return max(self.cows, key=lambda c: c.daily_milk)

    # Total milk
    def get_total_milk(self):
        return sum(cow.daily_milk for cow in self.cows)

    # Total revenue
    def get_daily_revenue(self):
        return sum(cow.get_daily_revenue() for cow in self.cows)

    # Print full report
    def print_report(self):
        print("\n" + "=" * 60)
        print(f"   {self.name} - FARM REPORT")
        print(f"   Owner: {self.owner} | {self.location}")
        print("=" * 60)

        print("\n🐄 ALL COWS:")
        for cow in self.cows:
            print(f"  {cow}")

        print(f"\n📊 SUMMARY:")
        print(f"  Total Cows     : {len(self.cows)}")
        print(f"  Total Milk/Day : {self.get_total_milk()} liters")
        print(f"  Daily Revenue  : ${self.get_daily_revenue():.2f}")
        print(f"  Monthly Revenue: ${self.get_daily_revenue() * 30:.2f}")
        print(f"  Best Cow       : {self.get_best_cow().name}")

        sick = self.get_sick_cows()
        if sick:
            print(f"\n🚨 SICK COWS: {', '.join(c.name for c in sick)}")

        stars = self.get_star_cows()
        if stars:
            print(f"⭐ STAR COWS : {', '.join(c.name for c in stars)}")


# ================================================
#              CREATE THE FARM
# ================================================

# Create farm
farm = Farm("Ritham Dairy Farm", "Sunny", "Nashville, Tennessee")

# Create cows
farm.add_cow(Cow("Bessie", 3, "Holstein",  28, "A"))
farm.add_cow(Cow("Daisy",  5, "Jersey",    15, "A", is_healthy=False))
farm.add_cow(Cow("Rosie",  4, "Guernsey",  30, "B"))
farm.add_cow(Cow("Luna",   8, "Holstein",  18, "B"))
farm.add_cow(Cow("Bella",  2, "Jersey",    35, "C"))
farm.add_cow(Cow("Molly",  6, "Guernsey",  24, "C", is_healthy=False))
farm.add_cow(Cow("Ruby",   1, "Holstein",  32, "A"))
farm.add_cow(Cow("Pearl",  5, "Jersey",    26, "B"))
farm.add_cow(Cow("Clara",  2, "Jersey",    33, "B"))
farm.add_cow(Cow("Maggie", 9, "Holstein",  14, "A", is_healthy=False))

# ---- PRINT INITIAL REPORT ----
farm.print_report()

# ================================================
#              FARM ACTIONS
# ================================================
print("\n" + "=" * 60)
print("   TAKING FARM ACTIONS")
print("=" * 60)

# Heal sick cows
print("\n🏥 HEALING SICK COWS:")
for cow in farm.get_sick_cows():
    cow.heal()

# Boost low producers
print("\n📈 BOOSTING LOW PRODUCERS:")
for cow in farm.cows:
    if cow.daily_milk < 20:
        cow.increase_milk(8)

# Add a brand new cow
print("\n🐄 ADDING NEW COW:")
farm.add_cow(Cow("Sophie", 1, "Jersey", 34, "C"))

# Remove retired cow
print("\n👋 RETIRING LUNA:")
farm.remove_cow("Luna")

# ---- PRINT UPDATED REPORT ----
print("\n📊 UPDATED FARM REPORT AFTER ACTIONS:")
farm.print_report()

# ---- BARN REPORTS ----
print("\n" + "=" * 60)
print("   BARN BY BARN REPORT")
print("=" * 60)
for barn in ["A", "B", "C"]:
    barn_cows = farm.get_barn_cows(barn)
    barn_milk = sum(c.daily_milk for c in barn_cows)
    print(f"\nBarn {barn} ({len(barn_cows)} cows | {barn_milk} liters/day):")
    for cow in barn_cows:
        print(f"  {cow}")