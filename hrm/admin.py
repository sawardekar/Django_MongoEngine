from django_mongoengine import mongo_admin as admin
from hrm.models import Employee, Department

# Register your models here.


class EmployeeAdmin(admin.DocumentAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)
