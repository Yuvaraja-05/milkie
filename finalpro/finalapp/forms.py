from django import forms
from .models import Buys

class Buyform(forms.ModelForm):
    class Meta:
        model=Buys
        fields='__all__'