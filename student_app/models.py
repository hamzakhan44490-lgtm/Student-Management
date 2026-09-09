from django.db import models
from django.contrib.auth.models import User
from django.core import validators



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
        return super().clean()
    
    
    def __str__(self):
        return self.name
    
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name
    