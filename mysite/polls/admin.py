from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["created_at"]}),
    ]
    inlines = [ChoiceInline]

    list_display = ["question_text", "created_at", "was_published_recently"]
    list_filter = ["created_at"]
    search_fields = ["question_text"]
    date_hierarchy = "created_at"


admin.site.register(Question, QuestionAdmin)
