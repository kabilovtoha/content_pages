from rest_framework import viewsets

from . import models
from . import serializers



class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_serializer_class(self, *args, **kwargs):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':
            return serializers.PostSerializer
        if self.action == 'retrieve':
            return serializers.PostDetSerializer
        return serializer_class

class ContentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer

    def get_serializer_class(self, *args, **kwargs):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':
            return serializers.ContentSerializer
        if self.action == 'retrieve':
            return serializers.ContentDetSerializer
        return serializer_class