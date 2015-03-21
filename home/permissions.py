from rest_framework import permissions
from home.models import Member


class HomeMemberPermission(permissions.BasePermission):
    """
    Handles permission for home members
    """
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'home') and request.user.is_authenticated():
            member = Member.objects.filter(home=obj.home, user=request.user)
            return member.exists()
        return False


class HomeManagerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'home') and request.user.is_authenticated():
            return obj.home.manager == request.user
        return False
