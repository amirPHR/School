from django.db import models
from user.models import User 
from class_room.models import ClassRoom

class Student(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE) 
    father_name = models.CharField(max_length=50) 
    national_code = models.CharField(max_length=10 , unique = True)  
    birth_date = models.DateField() 
    phone_number = models.CharField(max_length=11 , unique = True)  
    address = models.TextField() 
    class_room =  models.ForeignKey(ClassRoom , on_delete = models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return (f'{self.user.username} (base: {self.class_room.base}) (field: {self.class_room.field})')    