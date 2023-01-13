from django import forms

from .models import BlogPost

class TitleForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'title': 'title', 'text': ''}