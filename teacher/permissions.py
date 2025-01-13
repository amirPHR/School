from rest_framework.permissions import BasePermission 

# Permission class
class IsTeacherOrAdmin(BasePermission):
    """
    This permission check user is teacher or admin. 
    """
    def has_permission(self , request , view):
        user = request.user 
        return True if user.user_type in ['teacher','admin'] else False