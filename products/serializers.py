from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    condition = serializers.StringRelatedField(many=True)
    body_systems = serializers.StringRelatedField(many=True)
    
    class Meta:
        
        model = Product
        fields = '__all__'
        read_only_fields = ['user_status']