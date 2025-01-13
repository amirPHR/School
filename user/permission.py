# Import rest_framework libraries
from rest_framework.permissions import BasePermission 

# Custom Permissions
class CheckAdminPassword(BasePermission):
    """
    Custom permission to ensure the admin password is correct during user creation.
    """
    
    USER_TYPE_ALLOW = ['admin' , 'teacher']
    ALLOWED_PASSWORD = ['0960034455@gholampour']
    
    def has_permission(self, request, view):
        if view.action == 'create' and request.data.get("user_type") in self.USER_TYPE_ALLOW:
            return request.data.get("password") == self.ALLOWED_PASSWORD
        return True
    
class IsAuthenticatedOrSignupOnly(BasePermission):
    """
    Custom permission class:
    - Allows unauthenticated users to sign up (create a new user).
    - Allows authenticated users to perform only authenticated operations.
    """
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user.is_authenticated