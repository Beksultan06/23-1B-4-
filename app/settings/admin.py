from django.contrib import admin
from app.settings.models import Settings, Newave, Good, Team, Technology
# Register your models here.
admin.site.register(Settings)
admin.site.register(Newave)
admin.site.register(Good)
admin.site.register(Technology)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', "name", "direction"]
    list_filter = ['id', "name", "direction"]
    search_fields = ['id', "name", "direction"]