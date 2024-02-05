from rest_framework import serializers
from .models import Like
from django.contrib.auth.models import User
from posts.models import Post


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # Custom field to get the post's title
    title = serializers.SerializerMethodField()

    class Meta:
        model = Like
        fields = ['id', 'owner', 'post', 'title', 'created_at']

    def get_title(self, obj):
        return obj.post.title

    def validate(self, data):
        """
        Custom validation method to ensure a user
        cannot like a post more than once.
        """
        owner_id = self.context['request'].user.id
        post_id = data.get('post')
        # Check if a like by this user for this post already exists
        if Like.objects.filter(
            owner_id=owner_id, post_id=post_id
                              ).exists():
            raise serializers.ValidationError("You have already " +
                                              "liked the post.")
        return data
