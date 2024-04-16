from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator():
    message = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsAuthor():
    message = "Вы не являетесь владельцем!"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        else:
            return False
