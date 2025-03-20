from django import forms
from .models import UserData


class UserForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['name', 'email', 'phone']
