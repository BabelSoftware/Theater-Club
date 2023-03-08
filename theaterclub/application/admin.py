from django.contrib import admin
from .models import Application

# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    fields = ['id', 'full_name', 'email', 'school']
    list_display = ['id', 'full_name', 'email', 'school']
    search_fields = ['full_name']

admin.site.register(Application, ApplicationAdmin)