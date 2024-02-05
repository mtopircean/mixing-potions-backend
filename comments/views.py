from rest_framework import generics, permissions
from mixing_potions_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Comment.objects.all().select_related('owner', 'post')
        post_id = self.request.query_params.get('post_id')
        user_id = self.request.query_params.get('user_id')
        if post_id is not None:
            queryset = queryset.filter(post_id=post_id)
        elif user_id is not None:
            queryset = queryset.filter(owner_id=user_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method in ['GET', 'HEAD']:
            return CommentDetailSerializer
        return CommentSerializer

    def get_queryset(self):
        return Comment.objects.all().select_related('owner', 'post')
