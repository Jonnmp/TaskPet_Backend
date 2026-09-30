from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("text", "user", "completed", "reminder_type", "created_at")
    list_filter = ("completed", "reminder_type")
    search_fields = ("text", "user__username")
