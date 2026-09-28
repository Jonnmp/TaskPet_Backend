from django.db import models
from django.conf import settings


class PetStats(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pet_stats")
    level = models.PositiveIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)
    last_interaction = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Pet Stats"