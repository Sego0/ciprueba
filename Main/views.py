from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status,generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Main.models import Users,Employees,Devices,Device_type,Employee_device
from Main.serializers import UsersSerializer,EmployeesSerializer,DevicesSerializer,DeviceTypeSerializer,EmployeDeviceSerializer

# Create your views here.

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class DeviceList(generics.ListCreateAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer

class EmployeeDeviceList(generics.ListCreateAPIView):
    queryset = Employee_device.objects.all()
    serializer_class = EmployeDeviceSerializer

class EmployeeDeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee_device.objects.all()
    serializer_class = EmployeDeviceSerializer

@csrf_exempt
def EmployeesApi(request,id=0):
    if request.method=='GET':
        employee = Employees.objects.all()
        employee_serializer = EmployeesSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    
    elif request.method=='POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeesSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed to add',safe=False)
    
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(Id_rut=employee_data['Id_rut'])
        employee_serializer=EmployeesSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Update Successfully',safe=False)
        return JsonResponse('Failed to Update')
    
    elif request.method=='DELETE':
        employee=Employees.objects.get(Id_rut=id)
        employee.delete()
        return JsonResponse('Delete Successfully', safe=False)
    
@csrf_exempt
def DeviceApi(request,id=0):
    if request.method=='GET':
        device = Devices.objects.all()
        device_serializer = DevicesSerializer(device, many=True)
        return JsonResponse(device_serializer.data,safe=False)
    
    elif request.method=='POST':
        device_data = JSONParser().parse(request)
        device_serializer = DevicesSerializer(data=device_data)
        if device_serializer.is_valid():
            device_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed to add',safe=False)
    
    elif request.method=='PUT':
        device_data=JSONParser().parse(request)
        device=Devices.objects.get(id_device=device_data['id_device'])
        device_serializer=DevicesSerializer(device,data=device_data)
        if device_serializer.is_valid():
            device_serializer.save()
            return JsonResponse('Update Successfully',safe=False)
        return JsonResponse('Failed to Update')
    
    elif request.method=='DELETE':
        device=Devices.objects.get(id_device=id)
        device.delete()
        return JsonResponse('Delete Successfully', safe=False)
    
@csrf_exempt
def EmployeeDeviceApi(request,id=0):
    if request.method=='GET':
        employeedevice = Employee_device.objects.all()
        employeedevice_serializer = EmployeDeviceSerializer(employeedevice, many=True)
        return JsonResponse(employeedevice_serializer.data,safe=False)
    
    elif request.method=='POST':
        employeedevice_data = JSONParser().parse(request)
        employeedevice_serializer = EmployeDeviceSerializer(data=employeedevice_data)
        if employeedevice_serializer.is_valid():
            employeedevice_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed to add',safe=False)
    
    elif request.method=='PUT':
        employeedevice_data=JSONParser().parse(request)
        employeedevice=Employee_device.objects.get(id_ed=employeedevice_data['id_ed'])
        employeedevice_serializer=EmployeDeviceSerializer(employeedevice,data=employeedevice_data)
        if employeedevice_serializer.is_valid():
            employeedevice_serializer.save()
            return JsonResponse('Update Successfully',safe=False)
        return JsonResponse('Failed to Update')
    
    elif request.method=='DELETE':
        employeedevice=Employee_device.objects.get(id_ed=id)
        employeedevice.delete()
        return JsonResponse('Delete Successfully', safe=False)
    
@csrf_exempt
def DeviceTypeApi(request,id=0):
    if request.method=='GET':
        devicetype = Device_type.objects.all()
        devicetype_serializer = DeviceTypeSerializer(devicetype, many=True)
        return JsonResponse(devicetype_serializer.data,safe=False)
    
    elif request.method=='POST':
        devicetype_data = JSONParser().parse(request)
        devicetype_serializer = DeviceTypeSerializer(data=devicetype_data)
        if devicetype_serializer.is_valid():
            devicetype_serializer.save()
            return JsonResponse('Added Successfully',safe=False)
        return JsonResponse('Failed to add',safe=False)
    
    elif request.method=='PUT':
        devicetype_data=JSONParser().parse(request)
        devicetype=Device_type.objects.get(id_type=devicetype_data['id_ed'])
        devicetype_serializer=DeviceTypeSerializer(devicetype,data=devicetype_data)
        if devicetype_serializer.is_valid():
            devicetype_serializer.save()
            return JsonResponse('Update Successfully',safe=False)
        return JsonResponse('Failed to Update')
    
    elif request.method=='DELETE':
        devicetype=Employee_device.objects.get(id_ed=id)
        devicetype.delete()
        return JsonResponse('Delete Successfully', safe=False)