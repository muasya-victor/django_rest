from .models import Hero, Blog
from rest_framework import serializers


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['name', 'alias', 'id']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'created_at', 'updated_at']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ['username', 'email']

