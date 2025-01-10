from django.db import models 
from user.models import User 
from subject.models import Subject 

class Teacher(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE) 
    subject = models.ForeignKey(Subject , on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=11 , unique = True)  
    national_code = models.CharField(max_length=10 , unique = True) 
    birth_date = models.DateField() 
    date_add = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f'{self.user.username} ({self.subject.name})')