from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import HeroSerializer, BlogSerializer
from .models import Hero, Blog
from django.contrib.auth import get_user_model


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

    @action(detail=True, methods=['GET'])
    def get_blogs(self):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)

        return serializer.data
