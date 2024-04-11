from rest_framework import generics, filters
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Post
from .serializers import PostSerializer
from mixing_potions_api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework import status


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [
        OrderingFilter,
        SearchFilter
    ]
    ordering_fields = ['title', 'description', 'created_at',
                       'updated_at',
                       'owner__username', 'products__name',
                       'products__condition__name',
                       'products__body_systems__name']
    search_fields = ['title', 'description', 'created_at',
                     'updated_at',
                     'owner__username', 'products__name',
                     'products__condition__name',
                     'products__body_systems__name']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'
