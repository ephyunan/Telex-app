from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager



class UserAccountManager(BaseUserManager):
    def create_user(self,name,email,password=None):
        if not email:
            raise ValueError("Users must have email Adress")
        
        
        
class UserAccount(AbstractBaseUser,PermissionsMixin):
    email= models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    objects = UserAccountManager()
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    
    def get_fullname(self):
        return self.name
    
    def get_shortname(self):
        return self.name
    
    def __str__(self):
        return self.email
    
 

    

   
