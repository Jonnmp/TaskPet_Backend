from django.db import models
from django.conf import settings


class Task(models.Model):
    class ReminderType(models.TextChoices):
        ABSOLUTE = "absolute", "Fecha específica"
        RELATIVE = "relative", "Minutos relativos"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks")
    text = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")

    reminder_type = models.CharField(max_length=10, choices=ReminderType.choices, null=True, blank=True)
    reminder_at = models.DateTimeField(null=True, blank=True)
    reminder_minutes = models.PositiveIntegerField(null=True, blank=True)
    reminder_interval = models.PositiveIntegerField(null=True, blank=True)

    completed = models.BooleanField(default=False)
    last_reminded_at = models.DateTimeField(null=True, blank=True)
    external_uid = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["user", "completed"])]
        constraints = [
            models.UniqueConstraint(fields=["user", "external_uid"], name="unique_external_task_per_user")
        ]