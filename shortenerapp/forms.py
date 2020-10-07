from .models import URL
from django.forms import ModelForm, TextInput


class URLForm(ModelForm):
    class Meta:
        model = URL
        fields = ["full_url"]
        widgets = {
            "full_url": TextInput(attrs={
                'placeholder': 'Введите ссылку'
            })
        }