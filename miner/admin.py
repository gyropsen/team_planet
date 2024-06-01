from django.contrib import admin

from miner.models import Info, Achievement


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "amount",
    )
    ordering = ("amount",)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "task",
    )
    search_fields = ("name", "task")
