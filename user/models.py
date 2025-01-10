from django.db import models 
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    USER_TYPE = [
        ('student' , 'Student') , 
        ('teacher' , 'Teacher'),
        ('admin' , 'Admin'), 
    ] 
    
    user_type = models.CharField(max_length=50 , choices = USER_TYPE , default = 'student') 
    
    def __str__(self):
        return f'{self.username} ({self.user_type})'