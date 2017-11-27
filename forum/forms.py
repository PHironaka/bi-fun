from django import forms

from pagedown.widgets import PagedownWidget

from .models import Forum


class ForumForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Forum
        fields = [
            "title",
            "content",
            "draft",
            "publish",
        ]