import boto3
import json

# ================================================
#         RITHAM DAIRY FARM - AI ASSISTANT
# ================================================

# Connect to Bedrock
client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

print("✅ Connected to AWS Bedrock!")

# ================================================
#           FUNCTION TO CALL AI
# ================================================

def ask_ai(question):
    print(f"\n🤔 Question: {question}")
    print("⏳ Thinking...")

    body = json.dumps({
        "prompt": f"Human: {question}\nAssistant:",
        "max_gen_len": 512,
        "temperature": 0.7,
    })

    response = client.invoke_model(
        modelId="meta.llama3-8b-instruct-v1:0",
        body=body,
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())
    answer = result["generation"]
    print(f"🤖 AI Answer: {answer}")
    return answer

# ================================================
#         ASK AI ABOUT THE DAIRY FARM
# ================================================

print("\n" + "=" * 55)
print("   RITHAM DAIRY FARM - AI CONSULTANT")
print("=" * 55)

# Question 1
ask_ai("What are the top 3 ways to increase milk production in dairy cows?")

# Question 2
ask_ai("A Holstein cow aged 9 years is producing only 14 liters per day. Should I retire her?")

# Question 3
ask_ai("What should I feed dairy cows to maximize milk production?")

# Question 4
ask_ai("How do I know if a dairy cow is sick and needs a vet?")

print("\n" + "=" * 55)
print("✅ AI Farm Consultant session complete!")
print("=" * 55)