from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=30)
    sex = models.BooleanField(default=True)
    stu_id = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    qq = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    birth_date = models.CharField(max_length=50)
