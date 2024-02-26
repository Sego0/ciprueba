from .models import Employees,Devices,Device_type,Employee_device,Users
from rest_framework import viewsets,permissions,generics
#from rest_framework.decorators import action
#from rest_framework.response import Response
from .serializers import EmployeesSerializer,DevicesSerializer,DeviceTypeSerializer,EmployeDeviceSerializer,UsersSerializer
import django_filters

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    permission_classes =[permissions.AllowAny]
    serializer_class= EmployeesSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        queryset = super().get_queryset()
        #filtro por status
        status=self.request.query_params.get('status')
        if status:
            queryset=queryset.filter(status=status)

        #filtro por nombre
        Name = self.request.query_params.get('Name',None)
        if Name is not None:
            queryset = queryset.filter(Name__icontains=Name)

        #filtro por rut
        Id_rut=self.request.query_params.get('Id_rut')
        if Id_rut:
            queryset=queryset.filter(Id_rut=Id_rut)

        queryset = queryset.order_by('Name')
        return queryset



class DeviceViewset(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class=DevicesSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        queryset = super().get_queryset()
        #filtro por asignacion
        Assigned=self.request.query_params.get('Assigned')
        if Assigned:
            queryset=queryset.filter(Assigned=Assigned)
        #filtro por tipo
        id_type = self.request.query_params.get('id_type')
        if id_type:
            queryset = queryset.filter(id_type=id_type)
        #filtro por serialnumber
        id_device = self.request.query_params.get('id_device',None)
        if id_device is not None:
            queryset = queryset.filter(id_device__icontains=id_device)
        return queryset


class EmployeedeviceViewset(viewsets.ModelViewSet):
    queryset = Employee_device.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class=EmployeDeviceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        queryset= super().get_queryset()
       
        #Filtro por rut
        id_employees = self.request.query_params.get('id_employees')
        if id_employees:
            queryset = queryset.filter(id_employees=id_employees)
        #filtro por numero de serie
        id_device = self.request.query_params.get('id_device')
        if id_device:
            queryset = queryset.filter(id_device=id_device)
        #filtro por termino
        Fin_date = self.request.query_params.get('Fin_date')
        if Fin_date:
        # Excluye los registros donde Fin_date es nulo
            queryset = queryset.exclude(Fin_date=None)

        elif Fin_date is None:
        # Si no se especifica ningún filtro, retorna todos los datos
            pass

        else:
        # Filtra los registros donde Fin_date no es nulo
            queryset = queryset.filter(Fin_date__isnull=True)
        queryset = queryset.order_by('-Fin_date')
        return queryset