from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    fields = ["question_text", "created_at"]
    list_display = ["question_text", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
