from django.contrib import admin
from .              import models

@admin.register(models.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):

    pass

@admin.register(models.Rooms)
class RoomAdmin(admin.ModelAdmin):

    pass

