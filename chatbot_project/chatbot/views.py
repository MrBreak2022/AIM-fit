# chatbot/views.py
from django.http import JsonResponse
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Google Gemini Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set the Google application credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "A:\School Files\3rd Year files\softdev\gen-lang-client-0123016998-d1e6af230d27.json"

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def chatbot_view(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        if question.strip() == '':
            return JsonResponse({'response': 'No question provided'})
        
        response = chat.send_message(question)
        return JsonResponse({'response': response.text})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})
