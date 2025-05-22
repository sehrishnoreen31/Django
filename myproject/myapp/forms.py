from django import forms 
from .models import Dreamreals

class DreamRealsForm(forms.ModelForm):
    class Meta:
        model = Dreamreals
        fields = '__all__'