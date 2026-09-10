from django import forms
from .models import Student, Course


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "age", "marks", "email", "enrollment_date", "courses"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "age": forms.TextInput(attrs={"class": "form-control", "placeholder": "Age"}),
            "marks": forms.TextInput(attrs={"class": "form-control", "placeholder": "Marks"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"}),
            "enrollment_date": forms.DateInput(attrs={"class": "form-control", "id":"datepicker", "type": "date"}),
            
        }
