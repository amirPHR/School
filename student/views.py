# Imports
from rest_framework.viewsets import ModelViewSet 

from .serializers import StudentSerializer 
from .models import Student  

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer 