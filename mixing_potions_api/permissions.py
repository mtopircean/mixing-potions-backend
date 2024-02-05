from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            print('method is safe')
            return True
        print(f'obj.owner == request.user : {obj.owner == request.user}')
        print(f'request.user.is_staff : {request.user.is_staff}')
        print(obj.owner == request.user or request.user.is_staff)
        return obj.owner == request.user or request.user.is_staff
