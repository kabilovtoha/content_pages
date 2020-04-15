from rest_framework import serializers

from . import models




class PostSerializer(serializers.ModelSerializer):
    url_detail = serializers.URLField(source='get_page_url', read_only=True)
    class Meta:
        model = models.Post
        fields = (
            'id', 'title', 'url_detail'
        )

class PostDetSerializer(serializers.ModelSerializer):



    class Meta:
        model = models.Post
        fields = (
            'id', 'title'
        )


class ContentSerializer(serializers.ModelSerializer):
    counter = serializers.CharField(read_only=True)
    class Meta:
        model = models.Content
        fields = (
            'id', 'title', 'type', 'url', 'counter', 'json_attrs', 'post',
        )