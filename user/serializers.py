from rest_framework import serializers 
from .models import User 
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer 

class UserCreate(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta): 
        fields = ['username' , 'email' , 'password' , 'first_name' , 'last_name' , 'user_type']
