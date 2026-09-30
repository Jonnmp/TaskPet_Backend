from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id", "text", "description",
            "reminder_type", "reminder_at", "reminder_minutes", "reminder_interval",
            "completed", "last_reminded_at", "external_uid",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "last_reminded_at"]