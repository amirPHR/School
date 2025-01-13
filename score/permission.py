from rest_framework.permissions import BasePermission
from rest_framework.response import Response 
from rest_framework import status 

class RoleBasedPermission(BasePermission):
    
    def __init__(self , allowed_roles):
        self.allowed_roles = allowed_roles 
        
    def has_permission(self , request , view):
        """
        Check if the user has permission to perform the action.
        """
        user = request.user 
        if not user.user_type in self.allowed_roles:
            return Response(
                {'detail':'You are not in list.'},
                status = status.HTTP_403_FORBIDDEN
            )
            return True