from django import forms
from .models import Student


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
