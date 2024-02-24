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
    When serializing, the name of each related
    Condition instance is used instead of the pk.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    condition = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Condition.objects.all()
    )
    body_systems = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=BodySystem.objects.all()
    )

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['user_status']
