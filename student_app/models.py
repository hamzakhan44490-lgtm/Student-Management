from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils import timezone



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
    enrollment_date = models.DateField(default=timezone.localdate())
    is_active = models.BooleanField(default=True)
    courses = models.ManyToManyField("Course")
    
    
    def clean(self):
        if self.name and len(self.name) < 3:
            raise ValidationError({"name":"Enter more than or equal 3 character."})
        
        if self.enrollment_date > timezone.localdate():
            raise ValidationError({"enrollment_date":"Enrollment date cannot be in the future."})
   
   
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    