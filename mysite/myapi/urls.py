from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.documentation import include_docs_urls, get_docs_view
from . import views

schema_view = get_docs_view(title="Swagger View")

router = DefaultRouter()
router.register(r'heroes', views.HeroViewSet, basename='heroes')
router.register(r'blogs', views.BlogViewSet, basename='blogs')
router.register(r'users', views.UserVewSets, basename='users')

urlpatterns = [
    path('', include(router.urls)),

]
