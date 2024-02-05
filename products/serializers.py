from rest_framework import serializers
from posts.models import Post
from profiles.models import Profile
from .models import Product, Condition, BodySystem


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['nickname']


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'


class BodySystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodySystem
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model, including custom methods
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    condition = serializers.SlugRelatedField(
        many=True,
        # When serializing, the name of each related
        # Condition instance is used instead of the pk.
        slug_field='name',
        queryset=Condition.objects.all()
    )
    body_systems = serializers.SlugRelatedField(
        many=True,
        # When serializing, the name of each related
        # Condition instance is used instead of the pk.
        slug_field='name',
        queryset=BodySystem.objects.all()
    )
    # Custom field to serialize posts where the product is used.
    posts_used_in = PostSerializer(many=True, read_only=True,
                                   source='get_posts_used_in')
    # Custom field to serialize profiles of users who used the product.
    used_by_users = ProfileSerializer(many=True, read_only=True,
                                      source='get_used_by_users')

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['user_status']

    def get_posts_used_in(self, obj):
        """
        Retrieves and serializes posts where the product is used.
        """
        posts = Post.objects.filter(products=obj)
        post_serializer = PostSerializer(posts, many=True)
        return post_serializer.data

    def get_used_by_users(self, obj):
        """
        Retrieves and serializes profiles of users who have used the product.
        """
        users = Profile.objects.filter(products_used=obj)
        profile_serializer = ProfileSerializer(users, many=True)
        return profile_serializer.data
