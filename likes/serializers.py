from rest_framework import serializers
from .models import Like
from django.contrib.auth.models import User
from posts.models import Post

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:   
        model = Like
        fields = ['id', 'owner', 'post', 'created_at']
        
    def validate(self, data):
        owner_id = self.context['request'].user.id
        post_id = data.get('post')
        
        if Like.objects.filter(owner_id=owner_id, post_id=post_id).exists():
            raise serializers.ValidationError("You have already liked the post.")
        return data