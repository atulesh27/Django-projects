from django import forms
from .models import EmployeeData

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeData
        fields = ['name', 'email', 'phone', 'address']