# chatbot/admin.py
from django.contrib import admin
from .models import Prompt

class PromptAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'updated_at')  # Display these fields in the admin list view

admin.site.register(Prompt, PromptAdmin)
