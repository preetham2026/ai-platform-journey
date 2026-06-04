import boto3
import json
import sqlite3
from datetime import datetime

# ================================================
#      RITHAM DAIRY FARM - AI CHAT ASSISTANT
# ================================================

client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

# ================================================
#         GET LIVE FARM DATA FROM DATABASE
# ================================================

def get_farm_data():
    conn = sqlite3.connect("ritham_farm.db")
    cursor = conn.cursor()

    # Get all cows
    cursor.execute("SELECT name, breed, age, daily_milk, is_healthy, barn FROM cows")
    cows = cursor.fetchall()

    # Get stats
    cursor.execute("SELECT SUM(daily_milk), AVG(daily_milk), COUNT(*) FROM cows")
    stats = cursor.fetchone()

    # Get sick cows
    cursor.execute("SELECT name FROM cows WHERE is_healthy = 0")
    sick = [row[0] for row in cursor.fetchall()]

    # Get stars
    cursor.execute("SELECT name, daily_milk FROM cows WHERE daily_milk >= 30")
    stars = cursor.fetchall()

    # Get products
    cursor.execute("SELECT name, stock FROM products")
    products = cursor.fetchall()

    conn.close()

    return {
        "cows": cows,
        "total_milk": stats[0],
        "avg_milk": round(stats[1], 1),
        "total_cows": stats[2],
        "sick_cows": sick,
        "star_cows": stars,
        "products": products
    }

def build_farm_context(farm_data):
    # Build a text summary of farm data for AI
    cows_text = "\n".join([
        f"- {c[0]}: {c[1]}, age {c[2]}, {c[3]}L/day, "
        f"{'healthy' if c[4] else 'SICK'}, Barn {c[5]}"
        for c in farm_data["cows"]
    ])

    sick_text = ", ".join(farm_data["sick_cows"]) if farm_data["sick_cows"] else "None"

    stars_text = ", ".join([
        f"{c[0]} ({c[1]}L)" for c in farm_data["star_cows"]
    ])

    products_text = "\n".join([
        f"- {p[0]}: {p[1]} units in stock"
        for p in farm_data["products"]
    ])

    context = f"""
You are an expert AI assistant for Ritham Dairy Farm owned by Sunny in Nashville, Tennessee.
Here is the current farm data:

COWS ({farm_data['total_cows']} total):
{cows_text}

FARM STATISTICS:
- Total milk production: {farm_data['total_milk']} liters/day
- Average milk per cow: {farm_data['avg_milk']} liters/day
- Daily revenue (at $1.50/liter): ${farm_data['total_milk'] * 1.50:.2f}
- Monthly revenue: ${farm_data['total_milk'] * 1.50 * 30:.2f}

ALERTS:
- Sick cows: {sick_text}
- Star performers: {stars_text}

PRODUCTS IN STOCK:
{products_text}

Answer questions about this farm based on the data above.
Be helpful, specific, and reference actual cow names and numbers.
Keep answers concise and practical.
"""
    return context

# ================================================
#              ASK AI WITH FARM CONTEXT
# ================================================

def ask_farm_ai(question, context):
    prompt = f"{context}\n\nFarmer Sunny asks: {question}\n\nExpert AI Answer:"

    body = json.dumps({
        "prompt": prompt,
        "max_gen_len": 400,
        "temperature": 0.7,
    })

    response = client.invoke_model(
        modelId="meta.llama3-8b-instruct-v1:0",
        body=body,
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())
    return result["generation"].strip()

# ================================================
#              CHAT INTERFACE
# ================================================

def print_header():
    print("\n" + "=" * 60)
    print("   🐄 RITHAM DAIRY FARM - AI ASSISTANT 🤖")
    print("   Powered by AWS Bedrock + Llama 3")
    print("=" * 60)
    print("Ask me anything about your farm!")
    print("Type 'quit' to exit\n")

def chat():
    print_header()

    # Load farm data once
    print("📊 Loading farm data from database...")
    farm_data = get_farm_data()
    context = build_farm_context(farm_data)
    print(f"✅ Loaded {farm_data['total_cows']} cows, ready to chat!\n")

    # Predefined questions to start
    starter_questions = [
        "Which cows need immediate attention today?",
        "How is the farm performing financially?",
        "Which cow should I focus on improving first?",
    ]

    print("💡 Example questions you can ask:")
    for i, q in enumerate(starter_questions, 1):
        print(f"   {i}. {q}")
    print()

    # Chat loop
    while True:
        question = input("👨‍🌾 Sunny: ").strip()

        if question.lower() in ["quit", "exit", "q"]:
            print("\n👋 Goodbye! Keep taking care of those cows! 🐄")
            break

        if not question:
            continue

        print("🤖 AI thinking...")
        answer = ask_farm_ai(question, context)
        print(f"\n🤖 Farm AI: {answer}\n")
        print("-" * 60)

# ================================================
#                    RUN
# ================================================

if __name__ == "__main__":
    chat()