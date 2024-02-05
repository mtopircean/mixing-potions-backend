from rest_framework import generics, permissions
from likes.models import Like
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Retrieve the Follower instance.
        obj = super().get_object()
        if obj.owner != self.request.user:
            # If the current user is not the owner
            # of the follower instance, deny access.
            raise permissions.PermissionDenied()
        return obj
