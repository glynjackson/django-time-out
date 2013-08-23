"""Admin classes for the time_out app."""

# Django/Python imports.
from django.contrib import admin

# App imports
from .models import MaintenanceSchedule


class MaintenanceScheduleAdmin(admin.ModelAdmin):
    """
    Attributes admin overrides.
    """
    list_display = ['start_time', 'end_time', 'active']
    search_fields = ['start_time', 'end_time', 'description']
    sortable_field_name = "start_time"


admin.site.register(MaintenanceSchedule, MaintenanceScheduleAdmin)
