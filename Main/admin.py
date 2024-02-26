from django.contrib import admin
from .models import Employees,Devices,Device_type,Users,Employee_device

admin.site.register(Employees)
admin.site.register(Device_type)
admin.site.register(Users)
admin.site.register(Devices)
admin.site.register(Employee_device)


# Register your models here.
