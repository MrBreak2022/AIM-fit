import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv



# Google Gemini Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set the Google application credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "A:/School Files/3rd Year files/softdev/gen-lang-client-0123016998-d1e6af230d27.json"


model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "When users give their current weight and ideal weight, you must create a fitness plan"

while(True):
    question = input("You: ")
    
    if (question.strip() == ''):
        break


    response = chat.send_message(instruction+question)
    print('\n')
    print(f"Bot: {response.text}")
    print('\n')
    