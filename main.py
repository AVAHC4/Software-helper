from google import genai
client = genai.Client()

question = input("What is your Question: ").strip()
if question == "":
    print("Please ask a valid Question")
else:
    print("You asked:",question )
response = client.interactions.create(
    model="YOUR_MODEL_NAME",
    input=question,
)