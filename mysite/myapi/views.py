from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serializers import HeroSerializer, BlogSerializer, UserSerializer
from .models import Hero, Blog
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

    @action(detail=True, methods=['GET'])
    def get_hero(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # @action(detail=True, methods=['GET', 'DELETE'])
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        post_data = request.data
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserVewSets(viewsets.ModelViewSet):
    queryset = User.objects.values()
    serializer_class = UserSerializer

    @action(detail=True, methods=['GET'])
    def get_users(self):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return serializer.data
