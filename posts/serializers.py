from rest_framework import serializers
from .models import Post
from products.serializers import ProductSerializer

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_nickname = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        
        model = Post
        fields = [
            'id', 'title', 'description', 'created_at', 'updated_at',
            'image', 'owner', 'owner_nickname', 'products',
        ]
        
    def get_owner_nickname(self, obj):
        return obj.get_owner_nickname()