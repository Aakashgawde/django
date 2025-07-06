from django import forms
# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields='__all__'
        
