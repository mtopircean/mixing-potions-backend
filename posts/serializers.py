from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_nickname = serializers.SerializerMethodField()
    
    class Meta:
        
        model = Post
        fields = [
            'id', 'title', 'description', 'created_at', 'updated_at', 'products',
            'image', 'owner', 'owner_nickname',
        ]
        
    def get_owner_nickname(self, obj):
        return obj.get_owner_nickname()