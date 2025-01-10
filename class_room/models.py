from django.db import models 
 
class ClassRoom(models.Model):
    BASE_CHOICES = [
        ('10th' , '10th') ,
        ('11th' , '11th') ,
        ('12th' , '12th')
    ]
    base = models.CharField(max_length=10, choices=BASE_CHOICES) 
    
    FIELD_CHOICES = [
        ('computer' , 'Computer') , 
        ('electronic' , 'Electronic') , 
        ('mechanic' , 'Mechanic')
    ]
    field = models.CharField(max_length=255 , choices=FIELD_CHOICES)
    
    def __str__(self):
        return f'{self.base} ({self.field})' 
    