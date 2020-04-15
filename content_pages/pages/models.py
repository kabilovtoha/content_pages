from django.db import models

# Create your models here.
from django.urls import reverse
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.contrib.sites.models import Site

class Post(models.Model):

    class Meta:
        verbose_name = 'Запись страницы'
        verbose_name_plural = 'Записи страниц'
        ordering = ['-id']

    title = models.CharField('Заголовок', max_length=255, blank=True, null=True)

    def get_page_url(self):
        return f"{settings.BASE_URL}{reverse('pages-list')}{self.id}/"


    def __str__(self):
        return self.title


class Content(models.Model):

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
        ordering = ['-id']

    TYPE_APPLICATION = 'application'
    TYPE_AUDIO = 'audio'
    TYPE_EXAMPLE = 'example'
    TYPE_IMAGE = 'image'
    TYPE_MESSAGE = 'message'
    TYPE_MODEL = 'model'
    TYPE_MULTIPART = 'multipart'
    TYPE_TEXT = 'text'
    TYPE_VIDEO = 'video'

    TYPES = (
        (TYPE_APPLICATION, 'Application'),
        (TYPE_AUDIO, 'Audio'),
        (TYPE_EXAMPLE, 'Example'),
        (TYPE_IMAGE, 'Image'),
        (TYPE_MESSAGE, 'Message'),
        (TYPE_MODEL, 'Model'),
        (TYPE_MULTIPART, 'Multipart'),
        (TYPE_TEXT, 'Text'),
        (TYPE_VIDEO, 'Video'),
    )

    title = models.CharField('Заголовок', max_length=120, blank=True, null=True)
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
    type = models.CharField('Тип контента', choices=TYPES, max_length=30, blank=True, null=True)
    url = models.URLField('Ссылка', blank=True, null=True)
    counter = models.PositiveIntegerField('Cчетчик просмотров', blank=True, default=0)
    json_attrs = JSONField('Доп. данные', default=dict, blank=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return f'ID: {self.id}, {dict(self.TYPES).get(self.type)}'


class MimeType(models.Model):
    name = models.CharField('MIME-тип', max_length=66, blank=False, null=False, default='')

    def __str__(self):
        return self.name

class Source(models.Model):

    class Meta:
        verbose_name = 'Данные (файл) контента'
        verbose_name_plural = 'Данные (файлы) контента'
        ordering = ['-id']

    content = models.ForeignKey(Content, blank=True, null=True, on_delete=models.CASCADE)
    mime_type = models.ForeignKey(MimeType, blank=True, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to='uploads/%Y/%m', blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    bitrate = models.PositiveIntegerField('Битрейт (кбит/с, kbps)', blank=True, null=True)

    def __str__(self):
        return f'Контент id {self.id}, {self.mime_type}'