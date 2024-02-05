from rest_framework import serializers
from .models import Profile
from followers.models import Follower
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    class Meta:

        model = Profile
        fields = [
            'id', 'user_status', 'owner', 'first_name', 'last_name',
            'age', 'about', 'nickname', 'email', 'phone_number',
            'member_since', 'updated_at', 'image', 'followers',
            'following', 'followers_count', 'following_count',
        ]
        read_only_fields = ['user_status']

    def get_followers(self, obj):
        followers = Follower.objects.filter(followed=obj.owner)
        follower_nicknames = []

        for follower in followers:
            profile = Profile.objects.filter(owner=follower.owner).first()
            if profile and profile.nickname:
                follower_nicknames.append(profile.nickname)
            else:
                follower_nicknames.append(follower.owner.username)

        return follower_nicknames

    def get_following(self, obj):
        following = Follower.objects.filter(owner=obj.owner)
        following_nicknames = []

        for followed_user in following:
            profile = Profile.objects.filter(
                owner=followed_user.followed
                ).first()
            if profile and profile.nickname:
                following_nicknames.append(profile.nickname)
            else:
                following_nicknames.append(followed_user.followed.username)

        return following_nicknames
