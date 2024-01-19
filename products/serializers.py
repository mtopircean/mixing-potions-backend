from rest_framework import serializers
from .models import Product, Condition, BodySystem

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

class BodySystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodySystem
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    condition = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Condition.objects.all()
    )
    body_systems = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=BodySystem.objects.all()
    )
    class Meta:
        
        model = Product
        fields = '__all__'
        read_only_fields = ['user_status']