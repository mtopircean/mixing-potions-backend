from rest_framework import generics, filters
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Post
from .serializers import PostSerializer
from mixing_potions_api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        OrderingFilter,
        SearchFilter
        ]
    ordering_fields = ['title', 'created_at', 'updated_at',
                       'owner__profile__nickname']
    search_fields = ['title', 'owner__profile__nickname', 'products__name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'
