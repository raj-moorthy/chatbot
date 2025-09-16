import os
from google import genai

# Set your Gemini API key
os.environ["GEMINI_API_KEY"] = "AIzaSyDxrY5VyE9p1mOuzOIyJBFJc4ND5GBx55Y"

def chat_simple():
    client = genai.Client()

    print("Gemini Chatbot started! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Call Gemini to generate response for raw input string
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )
        print("Gemini:", response.text)

if __name__ == "__main__":
    chat_simple()
