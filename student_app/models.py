from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marks = models.IntegerField()
    email = models.EmailField(max_length=100, blank=True)
    enrollment_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    courses = models.ManyToManyField("Course")


class Course(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    