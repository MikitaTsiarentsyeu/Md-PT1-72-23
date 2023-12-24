from typing import Any
from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=150, label="Title")
    content = forms.CharField(widget=forms.Textarea(), label="Content")
    post_type = forms.ChoiceField(choices=Post.POST_TYPES, label="Content type")
    image = forms.ImageField(label="Main image")

    def clean_title(self):
        raw_title = self.cleaned_data['title']
        raw_title = raw_title.strip()

        return raw_title
    
    def clean_content(self):
        raw_content = self.cleaned_data['content']
        clean_content = raw_content.strip()

        clean_title = self.cleaned_data['title']

        if clean_content == clean_title:
            raise ValidationError("The content should not be the same as the title")

        return clean_content


class AddPostModel(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'post_type', 'image')
        widgets = {'content': forms.Textarea()}