from flask import Flask, jsonify, request
import sqlite3
from datetime import datetime

# ================================================
#         RITHAM DAIRY FARM - WEB API
# ================================================

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("ritham_farm.db")
    conn.row_factory = sqlite3.Row
    return conn

# ================================================
#                   ROUTES
# ================================================

# Home route
@app.route("/")
def home():
    return jsonify({
        "farm": "Ritham Dairy Farm",
        "owner": "Sunny",
        "location": "Nashville, Tennessee",
        "api_version": "1.0",
        "endpoints": [
            "/cows",
            "/cows/healthy",
            "/cows/sick",
            "/cows/stars",
            "/cows/<name>",
            "/barns",
            "/revenue",
            "/alerts",
            "/products"
        ]
    })

# Get all cows
@app.route("/cows")
def get_cows():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cows ORDER BY daily_milk DESC")
    cows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify({
        "total": len(cows),
        "cows": cows
    })

# Get healthy cows
@app.route("/cows/healthy")
def get_healthy():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cows WHERE is_healthy = 1 ORDER BY daily_milk DESC")
    cows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify({
        "total_healthy": len(cows),
        "cows": cows
    })

# Get sick cows
@app.route("/cows/sick")
def get_sick():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cows WHERE is_healthy = 0")
    cows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify({
        "total_sick": len(cows),
        "cows": cows,
        "alert": "Call the vet immediately!" if cows else "All cows are healthy!"
    })

# Get star cows
@app.route("/cows/stars")
def get_stars():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cows WHERE daily_milk >= 30 ORDER BY daily_milk DESC")
    cows = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify({
        "total_stars": len(cows),
        "cows": cows
    })

# Get single cow by name
@app.route("/cows/<name>")
def get_cow(name):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cows WHERE name = ?", (name,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return jsonify({"error": f"Cow '{name}' not found!"}), 404

    cow = dict(row)
    cow["daily_revenue"] = cow["daily_milk"] * 1.50
    cow["monthly_revenue"] = cow["daily_revenue"] * 30
    cow["grade"] = (
        "A" if cow["daily_milk"] >= 30 else
        "B" if cow["daily_milk"] >= 25 else
        "C" if cow["daily_milk"] >= 20 else "D"
    )
    return jsonify(cow)

# Get barn summary
@app.route("/barns")
def get_barns():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT barn,
               COUNT(*) as num_cows,
               SUM(daily_milk) as total_milk,
               AVG(daily_milk) as avg_milk
        FROM cows
        GROUP BY barn
        ORDER BY total_milk DESC
    """)
    barns = []
    for row in cursor.fetchall():
        barns.append({
            "barn": row[0],
            "num_cows": row[1],
            "total_milk": row[2],
            "avg_milk": round(row[3], 1),
            "daily_revenue": round(row[2] * 1.50, 2)
        })
    conn.close()
    return jsonify({"barns": barns})

# Get revenue summary
@app.route("/revenue")
def get_revenue():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(daily_milk), AVG(daily_milk) FROM cows")
    row = cursor.fetchone()
    conn.close()

    total_milk = row[0] or 0
    daily_rev = total_milk * 1.50
    monthly_expenses = 10450

    return jsonify({
        "total_milk_per_day": total_milk,
        "daily_revenue": round(daily_rev, 2),
        "monthly_revenue": round(daily_rev * 30, 2),
        "yearly_revenue": round(daily_rev * 365, 2),
        "monthly_expenses": monthly_expenses,
        "monthly_profit": round((daily_rev * 30) - monthly_expenses, 2),
        "yearly_profit": round(((daily_rev * 30) - monthly_expenses) * 12, 2),
    })

# Get all alerts
@app.route("/alerts")
def get_alerts():
    conn = get_db()
    cursor = conn.cursor()

    # Sick cows
    cursor.execute("SELECT name FROM cows WHERE is_healthy = 0")
    sick = [row[0] for row in cursor.fetchall()]

    # Low producers
    cursor.execute("SELECT name, daily_milk FROM cows WHERE daily_milk < 20")
    low = [{"name": r[0], "milk": r[1]} for r in cursor.fetchall()]

    # Retirement candidates
    cursor.execute("SELECT name, age FROM cows WHERE age > 7 AND daily_milk < 20")
    retire = [{"name": r[0], "age": r[1]} for r in cursor.fetchall()]

    # Star performers
    cursor.execute("SELECT name, daily_milk FROM cows WHERE daily_milk >= 30")
    stars = [{"name": r[0], "milk": r[1]} for r in cursor.fetchall()]

    conn.close()

    return jsonify({
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "sick_cows": sick,
        "low_producers": low,
        "retirement_candidates": retire,
        "star_performers": stars,
        "total_alerts": len(sick) + len(low) + len(retire)
    })

# Get products
@app.route("/products")
def get_products():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify({
        "total_products": len(products),
        "products": products
    })

# Add new cow (POST)
@app.route("/cows/add", methods=["POST"])
def add_cow():
    data = request.get_json()
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cows (name, breed, age, daily_milk, barn, is_healthy, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["name"], data["breed"], data["age"],
        data["daily_milk"], data["barn"],
        data.get("is_healthy", 1),
        datetime.now().strftime("%Y-%m-%d")
    ))
    conn.commit()
    conn.close()
    return jsonify({
        "message": f"✅ {data['name']} added to Ritham Dairy Farm!",
        "cow": data
    }), 201

# ================================================
#                 RUN THE API
# ================================================
if __name__ == "__main__":
    print("🌐 Ritham Dairy Farm API Starting...")
    print("📡 Open your browser and go to:")
    print("   http://localhost:5000")
    print("   http://localhost:5000/cows")
    print("   http://localhost:5000/alerts")
    print("   http://localhost:5000/revenue")
    print("   http://localhost:5000/barns")
    print("\nPress CTRL+C to stop the server")
    app.run(debug=True, port=5000)