
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import rest_views

router = DefaultRouter()
router.register('pages', rest_views.PageViewSet, basename='pages')
router.register('contents', rest_views.ContentViewSet, basename='contents')

urlpatterns = [
    path('', include(router.urls))
]
