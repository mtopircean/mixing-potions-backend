from rest_framework import serializers
from .models import Follower
from django.contrib.auth.models import User
from profiles.models import Profile

class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')
    followed_nickname = serializers.SerializerMethodField()
    
    class Meta:   
        model = Follower
        fields = ['id', 'owner', 'followed', 'followed_name', 'followed_nickname', 'created_at']
        
    def get_followed_nickname(self, obj):
        profile = Profile.objects.filter(owner=obj.followed).first()
        return profile.nickname if profile else None
        
    def validate(self, data):
        owner_id = self.context['request'].user.id
        followed_id = data.get('followed').id
        
        if owner_id == followed_id:
            raise serializers.ValidationError("You can't follow your own account.")
        
        if Follower.objects.filter(owner_id=owner_id, followed_id=followed_id).exists():
            raise serializers.ValidationError("User is already in your followed list.")
        
        return data
        