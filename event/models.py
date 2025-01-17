from django.db import models 
from user.models import User 

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField() 
    date = models.DateTimeField()

    def __str__(self):
        return f'Event: {self.name}'
     
class SignUpToEvent(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    event = models.ForeignKey(Event , on_delete=models.CASCADE) 

    def __str__(self):
        return f'sutdent: {self.user} event: {self.event}'