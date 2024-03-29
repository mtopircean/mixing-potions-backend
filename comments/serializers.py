from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User
from posts.models import Post
from profiles.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['id', 'nickname', 'image']


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializes comments with detailed information
    including the owner's profile and post URL."""
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_profile = ProfileSerializer(source='owner.profile', read_only=True)
    post_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='post-detail',
        source='post'
    )
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request and request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'post', 'created_at',
                  'updated_at', 'comment_text',
                  'owner_profile', 'post_url', 'is_owner', ]


class CommentDetailSerializer(CommentSerializer):

    post = serializers.ReadOnlyField(source='post.id')

    class Meta(CommentSerializer.Meta):
        pass
