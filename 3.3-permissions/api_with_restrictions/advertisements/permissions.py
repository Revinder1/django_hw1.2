from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        # Если пользователь, обращающийся к объекту создатель или админ - позволяем редактировать объект
        return request.user == obj.creator or request.user.is_superuser