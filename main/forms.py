# main/forms.py
from django import forms

from .models import User

class UserDataForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'age', 'gender', 'country', 'bio']

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'age': forms.NumberInput(attrs={'class': 'form-control'}),
        'gender': forms.Select(attrs={'class': 'form-control'}),
        'country': forms.TextInput(attrs={'class': 'form-control'}),
        'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
    }