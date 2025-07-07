from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll_number = models.IntegerField(unique=True)
    department = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    
