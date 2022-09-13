from django.contrib import admin
from backend.models.models import Bulb, House

@admin.register(Bulb)
class BulbAdmin(admin.ModelAdmin):
    list_display = ('ip', 'name')
    search_fields = ['ip', 'name']

@admin.register(House)
class BulbAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')
    search_fields = ['name']
