from django import forms
from pagedown.widgets import PagedownWidget
from django.forms import ModelForm
from .models import Court


class CourtForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta:
        model = Court
        fields = [
            "title",
            "location",
            "image",
            "content",
        ]

