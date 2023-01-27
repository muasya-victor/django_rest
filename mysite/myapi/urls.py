from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'heroes', views.HeroViewSet, basename='heroes')
router.register(r'blogs', views.BlogViewSet, basename='blogs')

urlpatterns = [
    path('', include(router.urls)),
]