import sqlite3
import json
from datetime import datetime

# ================================================
#         RITHAM DAIRY FARM - DATABASE
# ================================================

# Connect to database (creates file if not exists)
conn = sqlite3.connect("ritham_farm.db")
cursor = conn.cursor()

print("✅ Connected to Ritham Farm Database!")

# ================================================
#              CREATE TABLES
# ================================================

# Create cows table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cows (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        name        TEXT NOT NULL,
        breed       TEXT,
        age         INTEGER,
        daily_milk  REAL,
        is_healthy  INTEGER DEFAULT 1,
        barn        TEXT,
        created_at  TEXT
    )
""")

# Create milk_logs table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS milk_logs (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        cow_name    TEXT,
        milk_amount REAL,
        revenue     REAL,
        log_date    TEXT
    )
""")

# Create products table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT NOT NULL,
        price   REAL,
        stock   INTEGER
    )
""")

conn.commit()
print("✅ Tables created!")

# ================================================
#              ADD COWS TO DATABASE
# ================================================

def add_cow(name, breed, age, daily_milk, barn, is_healthy=1):
    cursor.execute("""
        INSERT INTO cows (name, breed, age, daily_milk, is_healthy, barn, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, breed, age, daily_milk, is_healthy, barn, 
          datetime.now().strftime("%Y-%m-%d")))
    conn.commit()
    print(f"✅ {name} added to database!")

def add_product(name, price, stock):
    cursor.execute("""
        INSERT INTO products (name, price, stock)
        VALUES (?, ?, ?)
    """, (name, price, stock))
    conn.commit()

# Clear existing data and add fresh
cursor.execute("DELETE FROM cows")
cursor.execute("DELETE FROM products")
cursor.execute("DELETE FROM milk_logs")
conn.commit()

print("\n--- Adding cows to database ---")
add_cow("Bessie", "Holstein",  3, 28, "A")
add_cow("Daisy",  "Jersey",    5, 15, "A", is_healthy=0)
add_cow("Rosie",  "Guernsey",  4, 30, "B")
add_cow("Luna",   "Holstein",  8, 18, "B")
add_cow("Bella",  "Jersey",    2, 35, "C")
add_cow("Molly",  "Guernsey",  6, 24, "C", is_healthy=0)
add_cow("Ruby",   "Holstein",  1, 32, "A")
add_cow("Pearl",  "Jersey",    5, 26, "B")
add_cow("Clara",  "Jersey",    2, 33, "B")
add_cow("Maggie", "Holstein",  9, 14, "A", is_healthy=0)

print("\n--- Adding products ---")
add_product("Whole Milk", 1.20, 500)
add_product("Butter",     4.50, 80)
add_product("Cheese",     6.00, 45)
add_product("Yogurt",     2.50, 200)
add_product("Ice Cream",  5.00, 30)

# ================================================
#              QUERY THE DATABASE
# ================================================

print("\n" + "=" * 55)
print("   QUERYING THE DATABASE")
print("=" * 55)

# Get all cows
print("\n--- ALL COWS ---")
cursor.execute("SELECT name, breed, age, daily_milk, barn FROM cows ORDER BY daily_milk DESC")
rows = cursor.fetchall()
for row in rows:
    print(f"🐄 {row[0]:<10} | {row[1]:<10} | Age: {row[2]} | Milk: {row[3]}L | Barn: {row[4]}")

# Get healthy cows only
print("\n--- HEALTHY COWS ---")
cursor.execute("SELECT name, daily_milk FROM cows WHERE is_healthy = 1 ORDER BY daily_milk DESC")
rows = cursor.fetchall()
for row in rows:
    print(f"✅ {row[0]:<10} | {row[1]} liters/day")

# Get sick cows
print("\n--- SICK COWS ---")
cursor.execute("SELECT name, age, daily_milk FROM cows WHERE is_healthy = 0")
rows = cursor.fetchall()
for row in rows:
    print(f"🚨 {row[0]:<10} | Age: {row[1]} | Milk: {row[2]}L")

# Get top 3 producers
print("\n--- TOP 3 PRODUCERS ---")
cursor.execute("SELECT name, daily_milk FROM cows ORDER BY daily_milk DESC LIMIT 3")
rows = cursor.fetchall()
for i, row in enumerate(rows, 1):
    print(f"#{i} {row[0]:<10} | {row[1]} liters/day")

# ================================================
#              AGGREGATE QUERIES
# ================================================

print("\n" + "=" * 55)
print("   DATABASE ANALYTICS")
print("=" * 55)

# Total and average milk
cursor.execute("SELECT SUM(daily_milk), AVG(daily_milk), MAX(daily_milk), MIN(daily_milk) FROM cows")
row = cursor.fetchone()
print(f"\n📊 MILK STATS:")
print(f"  Total   : {row[0]} liters/day")
print(f"  Average : {row[1]:.1f} liters/day")
print(f"  Highest : {row[2]} liters/day")
print(f"  Lowest  : {row[3]} liters/day")

# Group by barn
print(f"\n🏚️  MILK BY BARN:")
cursor.execute("""
    SELECT barn, COUNT(*) as num_cows, SUM(daily_milk) as total_milk, 
           AVG(daily_milk) as avg_milk
    FROM cows 
    GROUP BY barn 
    ORDER BY total_milk DESC
""")
rows = cursor.fetchall()
for row in rows:
    print(f"  Barn {row[0]}: {row[1]} cows | {row[2]} liters | avg: {row[3]:.1f}L")

# Group by breed
print(f"\n🐄 MILK BY BREED:")
cursor.execute("""
    SELECT breed, COUNT(*) as num_cows, SUM(daily_milk) as total_milk,
           AVG(daily_milk) as avg_milk
    FROM cows
    GROUP BY breed
    ORDER BY avg_milk DESC
""")
rows = cursor.fetchall()
for row in rows:
    print(f"  {row[0]:<12}: {row[1]} cows | {row[2]}L total | {row[3]:.1f}L avg")

# ================================================
#              UPDATE & DELETE
# ================================================

print("\n" + "=" * 55)
print("   UPDATING DATABASE")
print("=" * 55)

# Heal Daisy
cursor.execute("UPDATE cows SET is_healthy = 1 WHERE name = 'Daisy'")
conn.commit()
print("\n✅ Daisy healed in database!")

# Boost Maggie's milk
cursor.execute("UPDATE cows SET daily_milk = daily_milk + 8 WHERE name = 'Maggie'")
conn.commit()
print("📈 Maggie's milk boosted in database!")

# Remove Luna (retired)
cursor.execute("DELETE FROM cows WHERE name = 'Luna'")
conn.commit()
print("👋 Luna retired from database!")

# Add milk log for today
today = datetime.now().strftime("%Y-%m-%d")
cursor.execute("SELECT name, daily_milk FROM cows")
all_cows = cursor.fetchall()
for cow in all_cows:
    revenue = cow[1] * 1.50
    cursor.execute("""
        INSERT INTO milk_logs (cow_name, milk_amount, revenue, log_date)
        VALUES (?, ?, ?, ?)
    """, (cow[0], cow[1], revenue, today))
conn.commit()
print(f"📝 Milk log saved for {today}!")

# ================================================
#              FINAL REPORT FROM DB
# ================================================

print("\n" + "=" * 55)
print("   FINAL FARM REPORT FROM DATABASE")
print("=" * 55)

cursor.execute("""
    SELECT name, breed, age, daily_milk, barn, is_healthy
    FROM cows ORDER BY daily_milk DESC
""")
rows = cursor.fetchall()

total_milk = 0
for row in rows:
    status = "✅" if row[5] else "🚨"
    rev = row[3] * 1.50
    print(f"{status} {row[0]:<10} | {row[1]:<10} | "
          f"Milk: {row[3]}L | ${rev:.2f}/day | Barn {row[4]}")
    total_milk += row[3]

daily_rev = total_milk * 1.50
print(f"\n💰 Total Milk    : {total_milk} liters/day")
print(f"💰 Daily Revenue : ${daily_rev:.2f}")
print(f"💰 Monthly Rev   : ${daily_rev * 30:.2f}")
print(f"💰 Yearly Rev    : ${daily_rev * 365:.2f}")

# Close connection
conn.close()
print("\n✅ Database connection closed!")
print("💾 Data saved permanently in ritham_farm.db!")