from rest_framework import routers
from django.urls import path
from .views import EmployeeList,EmployeeDetail
from .api import EmployeeViewset,DeviceViewset,EmployeedeviceViewset

router=routers.DefaultRouter()
router.register('api/employee',EmployeeViewset,'Employee')
router.register('api/device',DeviceViewset,'Device')
router.register('api/employedevice',EmployeedeviceViewset,'Employedevice')

urlpatterns = router.urls
