from rest_framework import serializers 
from .models import User 
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer 

# User Serializer
class UserCreate(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta): 
        fields = ['username' , 'email' , 'password' , 'first_name' , 'last_name' , 'user_type']
