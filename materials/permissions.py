from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator():
    message = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsOwnerOrStaff(BasePermission):
    message = "Вы не являетесь владельцем!"

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.user == view.get_object().owner

