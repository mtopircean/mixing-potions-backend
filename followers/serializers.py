from rest_framework import serializers
from .models import Follower
from django.contrib.auth.models import User
from profiles.models import Profile


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializes follower information including owner
    and followed user's usernames and nicknames.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')
    followed_nickname = serializers.SerializerMethodField()
    followed_profile_id = serializers.SerializerMethodField()

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'followed', 'followed_name',
                  'followed_nickname', 'created_at', 'followed_profile_id']

    def get_followed_nickname(self, obj):
        """
        Retrieve the nickname of the followed user from their profile.
        """
        profile = Profile.objects.filter(owner=obj.followed).first()
        return profile.nickname if profile else None
    
    def get_followed_profile_id(self, obj):
        """
        Retrieve the profile ID of the followed user.
        """
        profile = Profile.objects.filter(owner=obj.followed).first()
        return profile.id if profile else None

    def validate(self, data):
        """
        Custom validation to prevent users from following themselves
        and to ensure a user is not followed more than once.
        """
        owner_id = self.context['request'].user.id
        followed_id = data.get('followed').id

        if owner_id == followed_id:
            raise serializers.ValidationError("You can't follow your own " +
                                              "account.")

        if Follower.objects.filter(owner_id=owner_id,
                                   followed_id=followed_id).exists():
            raise serializers.ValidationError("User is already in your " +
                                              "followed list.")

        return data
