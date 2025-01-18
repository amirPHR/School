from django.db import models 

# Event Model
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField() 
    date = models.DateTimeField()

    def __str__(self):
        return f'Event: {self.name}'