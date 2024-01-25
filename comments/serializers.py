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
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    owner_profile = ProfileSerializer(source='owner.profile', read_only=True)
    post_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='post-detail',
        source='post'
    ) 
    
    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request and request.user == obj.owner
    
    class Meta:
        model = Comment
        fields = ['id', 'owner', 'post', 'created_at',
                  'updated_at', 'comment_text']