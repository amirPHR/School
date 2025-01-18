from rest_framework.permissions import BasePermission 

class IsAdmin(BasePermission):
    """
    Only admins can create, delete and update.
    """
    def has_permission(self, request, view):
        user = request.user 
        if view.action in ['create', 'destroy', 'update', 'partial_update']:
            if user.user_type != 'admin':
                return False 
        return True 
    
class IsAdminOrTeacher(BasePermission):
    """
    Only admins and teachers can create, delete and update.
    """
    def has_permission(self, request, view):
        user = request.user 
        if view.action in ['create', 'destroy', 'update', 'partial_update']:
            if not user.user_type in ['teacher', 'admin']:
                return False 
        return True 
    
