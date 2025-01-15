from django.db import models
from student.models import Student 
from subject.models import Subject 

class Score(models.Model):
    student = models.ForeignKey(Student , on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    
    DATE_YEAR = [
        ('first_turn' , 'First Turn'),
        ('second_turn' , 'Second Turn')
    ]
     
    date_year = models.CharField(max_length = 50 , choices = DATE_YEAR)
    score = models.IntegerField()
    date = models.DateField()  
    
    DISCIPLINARY_STATUS_CHOICES = [
        ('very_good' , 'Very Good') ,
        ('good' , 'Good') , 
        ('normal' , 'Normal'), 
        ('bad' , 'Bad')
    ]
    disciplinery_status = models.CharField(max_length=255 , choices = DISCIPLINARY_STATUS_CHOICES) 
    
    def __str__(self):
        return f'{self.student.user.username} - {self.subject.name}'