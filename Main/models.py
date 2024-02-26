from django.db import models

# Create your models here.

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=45, null=False)
    UserPass = models.CharField(max_length=45, null=False)  
    UserMail = models.CharField(max_length=45, null=True)
    Loged_in = models.BooleanField(null=True)
    user_Token = models.CharField(max_length=45, null=True)
    toke_exp = models.DateField(null=True)

class Employees(models.Model):
    Id_rut = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=45, null=False)
    Area = models.CharField(max_length=45, null=False)
    Mail = models.CharField(max_length=45, null=True)
    status = models.CharField(max_length=45,null=False)
    last_change = models.ForeignKey(Users, on_delete=models.CASCADE)

class Device_type(models.Model):
    id_type = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=45,null=False)
    last_change = models.ForeignKey(Users, on_delete=models.CASCADE)

class Devices(models.Model):
    id_device = models.CharField(primary_key=True)
    id_type = models.ForeignKey(Device_type, on_delete=models.CASCADE)
    Model = models.CharField(max_length=45, null=False)
    Waranty = models.DateField(null=True)
    Number = models.IntegerField(null=True)
    Status = models.CharField(max_length=45,null=True)
    Assigned = models.BooleanField(null=True)
    last_change= models.ForeignKey(Users, on_delete=models.CASCADE)

class Employee_device(models.Model):
    id_ed = models.AutoField(primary_key=True)
    id_employees = models.ForeignKey(Employees, on_delete=models.CASCADE)
    id_device = models.ForeignKey(Devices, on_delete=models.CASCADE)
    Assig_date = models.DateField(null=True)
    Fin_date = models.DateField(null=True)
    last_change= models.ForeignKey(Users, on_delete=models.CASCADE)


    '''
    /\
   / /              /¯¯¯¯¯0\
   \ \__/¯¯¯¯¯¯¯¯¯¯         ¯¯www     >> K@m0doro <<
    \_____________________/¯¯¯¯¯¯
        /  /       \  \
        ¯¯¯         ¯¯¯

'''