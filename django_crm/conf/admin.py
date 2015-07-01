from django.contrib import admin
from .models import Setting


class SettingsModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Setting, SettingsModelAdmin)
