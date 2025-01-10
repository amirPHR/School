from django.db import models
from student.models import Student 

class Attendance(models.Model):
    student = models.ForeignKey(Student , on_delete = models.CASCADE)
    date = models.DateField()
    
    STATUS_CHOICES = [
        ('present' , 'Present') ,
        ('absent' , 'Absent') ,
        ('late' , 'Late')
    ] 
    status = models.CharField(max_length=30 , choices=STATUS_CHOICES)
    
    def __str__(self):
        return (f'{self.student.user.username} status: {self.status}({self.date})')