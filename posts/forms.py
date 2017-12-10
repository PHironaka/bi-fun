from django import forms
from django.forms import ModelForm
from markdownx.fields import MarkdownxFormField
from pagedown.widgets import PagedownWidget
from .models import Post
from taggit.forms import *



class PostForm(forms.ModelForm):
    content = MarkdownxFormField()
    publish = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
            "tags",
        ]

    