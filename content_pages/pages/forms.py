



from django import forms

from . import models


class PageForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title']

    contents = forms.ModelMultipleChoiceField(models.Content.objects.filter(post__isnull=True).all(), required=True)

class ContentForm(forms.ModelForm):
    post = forms.ModelChoiceField(models.Post.objects.all(), required=True)
    type = forms.ChoiceField(choices=models.Content.TYPES, required=True)

    class Meta:
        model = models.Content
        fields = ['title', 'post', 'type', 'url', 'json_attrs']


class SourceForm(forms.ModelForm):
    mime_type = forms.ModelChoiceField(models.MimeType.objects.all(), required=True)

    class Meta:
        model = models.Source
        fields = ['mime_type', 'content', 'file', 'text', 'bitrate']

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        file = cleaned_data.get('file')
        if not text and not file:
            raise forms.ValidationError(f'Необходимо добавить данные контента (текст или файл')
        print(f'text {text}\nfile {str(file)} ')
        return cleaned_data

    def _construct_form(self, i, **kwargs):
        """
        Override the method to change the form attribute empty_permitted
        """
        form = super(SourceForm, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form