from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    topic = forms.CharField(
        label="Topic",
        widget=forms.TextInput(attrs={
            'placeholder': 'Type or select a topic',
        })
    )
    class Meta:
        model = Room
        fields = ['name', 'description']