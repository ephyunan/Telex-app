from django.db import models
from django.contrib.auth import get_user_model
from django import forms

from email.policy import default

User = get_user_model()
# Create your models here.
class Tutor(models.Model):
    username = models.CharField(max_length=40)
    
    email = models.EmailField()
    
    def __str__(self):
        return str(self.username.username)