from rest_framework import serializers

from . import models




class PostSerializer(serializers.ModelSerializer):
    url_detail = serializers.URLField(source='get_page_url', read_only=True)
    class Meta:
        model = models.Post
        fields = (
            'id', 'title', 'url_detail'
        )

class MimeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MimeType
        fields = (
            'id', 'name'
        )

class SourceSerializer(serializers.ModelSerializer):
    mime_type = MimeTypeSerializer()
    class Meta:
        model = models.Source
        fields = (
            'id', 'content', 'mime_type', 'file', 'text', 'bitrate'
        )

class PostContentDetSerializer(serializers.ModelSerializer):
    sources = serializers.ListField(child=SourceSerializer(), source='get_sources',
                                     read_only=True)
    counter = serializers.CharField(read_only=True)
    class Meta:
        model = models.Content
        fields = (
            'id', 'title', 'type', 'url', 'counter', 'json_attrs', 'post', 'sources'
        )

class PostDetSerializer(PostSerializer):
    contents = serializers.ListField(child=PostContentDetSerializer(), source='get_contents',
                                      read_only=True)
    class Meta:
        model = models.Post
        fields = (
            'id', 'title', 'contents', 'url_detail'
        )


class ContentSerializer(serializers.ModelSerializer):
    counter = serializers.CharField(read_only=True)
    url_detail = serializers.URLField(source='get_content_url', read_only=True)

    class Meta:
        model = models.Content
        fields = (
            'id', 'title', 'type', 'url', 'counter', 'json_attrs', 'post', 'url_detail'
        )

class ContentDetSerializer(ContentSerializer):
    sources = serializers.ListField(child=SourceSerializer(), source='get_sources',
                                     read_only=True)
    counter = serializers.CharField(read_only=True)
    post = PostSerializer()
    class Meta:
        model = models.Content
        fields = (
            'id', 'title', 'type', 'url', 'counter', 'json_attrs', 'post', 'sources', 'url_detail'
        )