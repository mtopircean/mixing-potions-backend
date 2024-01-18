from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        
        model = Profile
        fields = [
            'id', 'user_status', 'owner', 'first_name', 'last_name', 
            'age', 'about', 'nickname', 'email', 'phone_number', 
            'member_since', 'updated_at', 'image'
        ]
        read_only_fields = ['user_status']