from rest_framework import generics, permissions
from django.http import Http404
from followers.models import Follower
from followers.serializers import FollowerSerializer
from mixing_potions_api.permissions import IsOwnerOrReadOnly


class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Follower.objects.all()
        return Follower.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Return a list of all followers for the current user,
        used to check object permissions.
        """
        if self.request.user.is_staff:
            return Follower.objects.all()
        return Follower.objects.filter(owner=self.request.user)

    def get_object(self):
        """
        Retrieve and return the current Follower instance.
        Ensure that the current user is the owner of the follower instance.
        """
        try:
            obj = super().get_object()
        except Follower.DoesNotExist:
            raise Http404("Follower not found")
        return obj
