from django import forms
from django.forms import ModelForm
from .models import Court


class CourtForm(forms.ModelForm):
    class Meta:
        model = Court
        fields = [
            "title",
            "location",
            "image",
            "content",

        ]

