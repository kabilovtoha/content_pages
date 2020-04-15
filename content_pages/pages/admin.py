from django.contrib import admin

from . import models
from . forms import PageForm, ContentForm, SourceForm

# Register your models here.


class SourceAdminInline(admin.TabularInline):
    model = models.Source
    form = SourceForm
    extra = 0
    # max_num = 1
    min_num = 1

class ContentAdmin(admin.ModelAdmin):
    list_filter = ('type', 'post')
    search_fields = ['title', 'post']
    list_display = ('title', 'id', 'post', 'type', 'counter')
    form = ContentForm
    # model = models.Content
    inlines = [SourceAdminInline]

admin.site.register(models.Content, ContentAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    search_fields = ['title']

admin.site.register(models.Post, PostAdmin)


class MimeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(models.MimeType, MimeTypeAdmin)