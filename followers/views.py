from rest_framework import generics, permissions
from followers.models import Follower
from followers.serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Return a list of all followers for the current user,
        used to check object permissions.
        """
        return Follower.objects.filter(owner=self.request.user)

    def get_object(self):
        """
        Retrieve and return the current Follower instance.
        Ensure that the current user is the owner of the follower instance.
        """
        # Retrieve the Follower instance.
        obj = super().get_object()
        if obj.owner != self.request.user:
            # If the current user is not the owner of
            # the follower instance, deny access.
            raise permissions.PermissionDenied()
        return obj
