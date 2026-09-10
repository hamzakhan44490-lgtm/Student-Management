from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django import forms



class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=(validators.MinValueValidator(1),
                    validators.MaxValueValidator(120)
        )
    )
    marks = models.IntegerField(
        validators=(validators.MinValueValidator(1),
                    validators.MaxValueValidator(100)
        )
    )
    email = models.EmailField(max_length=100, blank=True)
    enrollment_date = models.DateField()
    is_active = models.BooleanField(default=True)
    courses = models.ManyToManyField("Course")
    
    
    def clean(self):
        if self.name and len(self.name) < 3:
            raise ValidationError("Enter more than or equal 3 character.")
        if self.age and self.age < 1:
            raise ValidationError("Ensure this value YES is greater than or equal to 1.")
        if self.marks and self.marks < 1:
            raise ValidationError("Ensure this value is YES greater than or equal to 1.")
        if self.email and len(self.email) < 15:
            raise ValidationError("Ensure this value is greater than or equal to 15.")
        
        
    def __str__(self):
        return self.name
    
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    