import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from the .env file.")

client = genai.Client(api_key=api_key)

conversation_history = []

print("🤖 Custom Gemini AI Chatbot with Memory")
print("Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    conversation_history.append(
        {
            "role": "user",
            "parts": [{"text": user_input}]
        }
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=conversation_history
    )

    assistant_reply = response.text

    conversation_history.append(
        {
            "role": "model",
            "parts": [{"text": assistant_reply}]
        }
    )

    print(f"AI: {assistant_reply}\n")