from django import forms
from django.forms import ModelForm
from markdownx.fields import MarkdownxFormField
from pagedown.widgets import PagedownWidget
from .models import Court
from taggit.forms import *


class CourtForm(forms.ModelForm):
    content = MarkdownxFormField()
  
    class Meta:
        model = Court
        fields = [
            "title",
            "location",
            "image",
            "content",
            "tags",
        ]

