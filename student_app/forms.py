from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "marks", "email", "enrollment_date", "courses"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "marks": forms.TextInput(attrs={"class": "form-control", "placeholder": "Marks"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"}),
            "enrollment_date": forms.DateInput(attrs={"class": "form-control", "id":"datepicker", "type": "date"}),
            
        }

class UserRegisterationForm(UserCreationForm):
    
    ROLL_CHOICES = [
        ("Teacher", "Teacher"),
        ("Student", "Student"),
    ]
    
    email = forms.EmailField(required=False, label="Email")
    role = forms.ChoiceField(required=True, choices=ROLL_CHOICES)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
