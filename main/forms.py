from django.forms import ModelForm
from .models import Clothes


class ClothesForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ['title', 'size', 'sex', 'category', 'image', 'composition', 'price']