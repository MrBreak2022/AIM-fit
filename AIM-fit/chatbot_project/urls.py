# chatbot_project/urls.py
from django.contrib import admin
from django.urls import path
from chatbot.views import chatbot_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for Django admin panel
    path('chatbot/', chatbot_view, name='chatbot'),  # URL for chatbot API endpoint
    path('', TemplateView.as_view(template_name='chatbot/chat.html'), name='home'),  # URL for rendering the chatbot interface
]
