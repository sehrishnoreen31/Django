from django.contrib import admin
from .models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('empname', 'contact', 'joined_date')
    search_fields = ('empname__startswith',)

