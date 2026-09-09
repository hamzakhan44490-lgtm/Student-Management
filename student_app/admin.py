from django.contrib import admin
from .models import Student, Course

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "marks", "email", "enrollment_date", "is_active"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name"]