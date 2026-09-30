from django.contrib import admin
from .models import PetStats

@admin.register(PetStats)
class PetStatsAdmin(admin.ModelAdmin):
    list_display = ("user", "level", "experience", "last_interaction")
