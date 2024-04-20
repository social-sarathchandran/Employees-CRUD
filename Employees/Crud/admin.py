from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "create_date", "update_date")
    search_fields = ("name", "email")


# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
