from .models import Student
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django import forms

# class StudentLoginView(LoginView):
#     redirect_authenticated_user = True


class StudentLogoutView(LogoutView):
    next_page = reverse_lazy("student_list")


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class StudentListView(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    fields = ["name", "age", "subject", "marks"]
    success_url = reverse_lazy("student_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    fields = ["name", "age", "subject", "marks"]
    success_url = reverse_lazy("student_list")

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)
    

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("student_list")

    def get_queryset(self):
        return Student.objects.filter(üser=self.request.user)
    


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Username"
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Password"
        })
    )

class StudentLoginView(LoginView):
    authentication_form = LoginForm
    template_name = "registration/login.html"
