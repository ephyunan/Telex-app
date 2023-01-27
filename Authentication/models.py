from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tutor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    models.EmailField(_(""), max_length=254)
    

    def __str__(self):
        return 

   
