from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        
        model = Product
        fields = [
            'id', 'name', 'condition', 'body_systems', 'image'
        ]
        read_only_fields = ['user_status']