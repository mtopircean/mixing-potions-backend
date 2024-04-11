from rest_framework import generics, filters
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from mixing_potions_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        followers_count=Count('owner__followers'),
        following_count=Count('owner__following'),
    )
    serializer_class = ProfileSerializer
    filter_backends = [
        OrderingFilter,
        SearchFilter
    ]
    ordering_fields = [
        'user_status', 'member_since', 'updated_at',
        'followers_count', 'following_count'
    ]
    search_fields = [
        'user_status', 'first_name', 'last_name',
        'age', 'nickname', 'phone_number',
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering', None)
        if ordering:
            return queryset.order_by(ordering)
        return queryset


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'
