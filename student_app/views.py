from .models import Student, Course
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django import forms
from .forms import StudentRegistrationForm
from django.shortcuts import redirect
from django.contrib import messages


class StudentLoginView(LoginView):
    success_url = reverse_lazy("student_list")
    template_name = "registration/login.html"


class StudentLogoutView(LogoutView):
    next_page = reverse_lazy("student_list")


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
    
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("student_list")
        return super().dispatch(request, *args, **kwargs)


class StudentListView(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(LoginRequiredMixin, CreateView):
    form_class = StudentRegistrationForm
    template_name = "student_app/student_form.html"
    success_url = reverse_lazy("student_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Student created successfully!")
        return super().form_valid(form)
    


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    form_class = StudentRegistrationForm
    template_name = "student_app/student_form.html"
    success_url = reverse_lazy("student_list")
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Student updated successfully!")
        return super().form_valid(form)
    

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)
    

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("student_list")
    
    
    def delete(self, request,  *args, **kwargs):
        messages.success(request, "Student deleted successfully")
        return super().delete(request, *args, **kwargs)
    
    
    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)
    


# class LoginForm(AuthenticationForm):

#     username = forms.CharField(
#         widget=forms.TextInput(attrs={
#             "class": "form-control",
#             "placeholder": "Username"
#         })
#     )

#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             "class": "form-control",
#             "placeholder": "Password"
#         })
#     )

# class StudentLoginView(LoginView):
#     authentication_form = Loginform
#     template_name = "registration/login.html"

