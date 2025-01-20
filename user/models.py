from django.db import models 
from django.contrib.auth.models import AbstractUser 

# User Model
class User(AbstractUser):
    USER_TYPE = [
        ('student' , 'Student') , 
        ('teacher' , 'Teacher'),
        ('admin' , 'Admin'), 
    ] 
    
    user_type = models.CharField(max_length=50 , choices = USER_TYPE, default='admin') 
    
    def save(self, *args, **kwargs):
        if self.user_type == 'admin':
            self.is_staff = True
        else:
            self.is_staff = False 
        super().save(*args, **kwargs) 
        
    def __str__(self):
        return f'{self.username} ({self.user_type})'