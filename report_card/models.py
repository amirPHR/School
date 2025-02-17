from django.db import models
from student.models import Student 
from score.models import Score 

class ReportCard(models.Model):
    student = models.OneToOneField(Student , models.CASCADE) 
    score = models.ManyToManyField(Score) 

    def calculate_average(self):
        scores = self.score.all() 
        if scores.exists():
            total_score = sum(score.score for score in scores) 
            return total_score / 8
        return 0 
    
    def __str__(self):
        return f'Report Card for {self.student.user.username}' 