import pytest 
from rest_framework.test import APIClient 
from rest_framework import status 
from user.models import User 

class TestStudent:
    def test_student_if_not_anonymous_user(self):
        client = APIClient() 
        response = client.post('/student/Student/', {'user':4 , 'father_name':'hossein', 'national_code':'0960034455', 'birth_date':'2021-04-02', 'phone_number':'09154002526', 'address':'tolab', 'class_room': 1})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        