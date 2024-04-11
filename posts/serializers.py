from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from .models import Post
from products.models import Product
from products.serializers import ProductSerializer
from likes.models import Like
from comments.serializers import CommentSerializer
from comments.models import Comment
from profiles.models import Profile


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.ReadOnlyField(source='owner.pk')
    owner_image = serializers.SerializerMethodField()
    owner_nickname = serializers.SerializerMethodField()
    liked_by = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    products = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Product.objects.all(),
        write_only=True
    )

    class Meta:

        model = Post
        fields = [
            'id', 'title', 'description', 'created_at', 'updated_at',
            'image', 'owner', 'owner_nickname', 'products', 'liked_by',
            'is_owner', 'like_count', 'comment_count', 'comments',
            'owner_id', 'owner_image',
            'like_id',
        ]

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request and request.user == obj.owner

    def get_owner_nickname(self, obj):
        return obj.get_owner_nickname()

    def get_owner_image(self, obj):
        try:
            profile = Profile.objects.get(owner=obj.owner)
            return profile.image.url
        except Profile.DoesNotExist:
            return None

    def get_liked_by(self, obj):
        return [like.owner.username for like in obj.likes.all()]

    def get_like_count(self, obj):
        return obj.likes.count()

    def get_like_id(self, obj):
        request = self.context.get('request')
        user = request.user if request else None
        if user and not user.is_anonymous:
            like = Like.objects.filter(post=obj, owner=user).first()
            if like:
                return like.id
        return None

    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()

    def to_representation(self, instance):
        """
        Customize how post is rendered in order to include detailed
        information about the product, not just the products id.

        Instance: The Post instance to represent.
        Returns:A dictionary representing the serialized Post instance
        with detailed information about associated products.
        """
        representation = super().to_representation(instance)
        representation['products'] = ProductSerializer(
            instance.products.all(), many=True
        ).data
        return representation
