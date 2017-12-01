from django import forms
from django.forms import ModelForm
from markdownx.widgets import MarkdownxWidget

from pagedown.widgets import PagedownWidget
from .models import Post
from taggit.forms import *


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=MarkdownxWidget())
    publish = forms.DateField(widget=forms.SelectDateWidget)
    p_tags = TagField()

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]

    