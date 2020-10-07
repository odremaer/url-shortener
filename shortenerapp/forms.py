from django import forms
from .models import URL
from django.forms import ModelForm, TextInput

class URLForm(ModelForm):
    # your_name = forms.CharField(label='Your name', max_length=100)
    class Meta:
        model = URL
        fields = ["full_url"]
        widgets = {
            "full_url": TextInput(attrs={
                'placeholder': 'ur link'
            })
        }