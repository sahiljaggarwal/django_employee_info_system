from django.forms import ModelForm
from .models import Employee
from django import forms
class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields= '__all__'

        widgets={
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control'})
        }