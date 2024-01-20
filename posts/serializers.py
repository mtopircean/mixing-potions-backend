from rest_framework import serializers
from .models import Post
from products.models import Product
from products.serializers import ProductSerializer


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_nickname = serializers.SerializerMethodField()
    products = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Product.objects.all(),
        write_only=True
    )
    
    class Meta:
        
        model = Post
        fields = [
            'id', 'title', 'description', 'created_at', 'updated_at',
            'image', 'owner', 'owner_nickname', 'products',
        ]
        
    def get_owner_nickname(self, obj):
        return obj.get_owner_nickname()
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['products'] = ProductSerializer(instance.products.all(), many=True).data
        return representation