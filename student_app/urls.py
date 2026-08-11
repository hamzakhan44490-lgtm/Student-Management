from django.urls import path
from student_app import views

urlpatterns = [
    path("student_list/", views.StudentListView.as_view(), name="student_list"),
    path("create/", views.StudentCreateView.as_view(), name="create_student"),
    path("detail/<int:pk>/", views.StudentDetailView.as_view(), name="detail_student"),
    path("update/<int:pk>/", views.StudentUpdateView.as_view(), name="update_student"),
    path("delete/<int:pk>/", views.StudentDeleteView.as_view(), name="delete_student"),
    path("login/", views.StudentLoginView.as_view(), name="login"),
    path("logout/", views.StudentLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),


]
