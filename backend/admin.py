from django.contrib import admin
from .models import Bulb

@admin.register(Bulb)
class BulbAdmin(admin.ModelAdmin):
    pass