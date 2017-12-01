from django import forms
from django.forms import ModelForm

from pagedown.widgets import PagedownWidget
from .models import Post
from taggit.forms import *


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
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

    