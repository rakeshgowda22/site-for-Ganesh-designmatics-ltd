from django.db import models


# Create your models here.
class glxs(models.Model):
    phoneno=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    password1=models.CharField(max_length=50)
    password2=models.CharField(max_length=40)

class login(models.Model):
     phoneno=models.CharField(max_length=100)
     password=models.CharField(max_length=50)
    
class about(models.Model):
      phone=
     class Meta:
         db_table:'app_glxs'
         db_table:'app_login'