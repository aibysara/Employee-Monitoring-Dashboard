from django.contrib import admin

from employee.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)