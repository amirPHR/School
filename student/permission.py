from rest_framework.permissions import BasePermission

# This permission check If user is student or admin. not teacher
class IsStudentOrAdmin(BasePermission):
    def has_permission(self , request , view):
        user = request.user 
        return True if user.user_type in ['student' , 'admin'] else False