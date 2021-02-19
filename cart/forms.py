from django import forms
from .models import Pedido, Item
from config.models import Profile


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['size']
