from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_Tutor = models.BooleanField(default=False)
    
    
class Tutor(models.Model):
    tutor = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField()
    
    def __str__(self):
        return self.tutor.username
    
    
class Student(models.Model):
    student = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.student.username