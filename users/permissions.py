from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):
    message = "Вы не являетесь владельцем и не персонал!"

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.user.email == view.get_object().user.email
