from django.contrib import admin
from .models import Employee, Dreamreals

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('empname', 'contact', 'joined_date')
    search_fields = ('empname__startswith',)

@admin.register(Dreamreals)
class DreamrealsAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'mail')
    search_fields = ('website__startswith',)

