from django.contrib import admin
from . import models

@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = ("guest","room", "status", "check_in", "check_out", "in_progress", "is_finished")

    list_filter = ("status",)
