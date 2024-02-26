from rest_framework import serializers
from Main.models import Users,Employees,Devices,Device_type,Employee_device
from django_filters import rest_framework as filters

#Filters

class EmployeeFilter(filters.FilterSet):
    Name=filters.CharFilter(field_name='Name',lookup_expr='icontains')
    status=filters.CharFilter(field_status='status',lookup_expr='exact')
    Id_rut=filters.CharFilter(field_status='Id_rut',lookup_expr='exact')

    class Meta:
        model = Employees
        fields = {
            'status':['exact'],
            'Name':['icontains'],
            'Id_rut':['exact']

        }

class Devicefilter(filters.FilterSet):
    Assigned = filters.BooleanFilter(field_assigned='Assigned',lookup_expr='exact')
    id_type = filters.NumberFilter(field_id_type='id_type',lookup_expr='exact')
    id_device = filters.NumberFilter(field_id_device='id_device',lookup_expr='icontains')

    class  Meta:
        model = Devices
        fields = {
            'Assigned':['exact'],
            'id_type':['exact'],
            'id_device':['icontains']
        }


#Serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('UserId', 'UserName', 'UserPass', 'UserMail', 'Loged_in', 'user_Token','toke_exp')

class DevicesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Devices
        fields=('id_device', 'id_type','Model', 'Waranty', 'Number', 'Status','Assigned','last_change')


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('Id_rut', 'Name', 'Area', 'Mail', 'status','last_change')
        filertset_class = EmployeeFilter 

class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device_type
        fields=('id_type', 'type_name', 'last_change')

class EmployeDeviceSerializer(serializers.ModelSerializer):
    nombre = serializers.SerializerMethodField()
    tipo = serializers.SerializerMethodField()


    class Meta:
        model=Employee_device
        fields=('id_ed', 'id_employees', 'id_device', 'Assig_date', 'Fin_date','last_change','nombre','tipo')

    def get_nombre(self, obj):
        return obj.id_employees.Name if obj.id_employees else None
    
    def get_tipo(self, obj):
        return obj.id_device.id_type.type_name if obj.id_device.id_type else None

#filtro employeesdevice

class Employeedevicefilter(filters.FilterSet):
    Fin_date = filters.DateFilter(Fin_date='Fin_date',lookup_expr='isnull')
    id_employees = filters.NumberFilter(field_name='id_employees',lookup_expr='exact')
    id_device = filters.CharFilter(field_name='id_device',lookup_expr='exact')
    
    class Meta:
        model = Employee_device
        fields = {
            'Fin_date':['isnull'],
            'id_employees':['exact'],
            'id_device':['exact'],
            
        }

        

