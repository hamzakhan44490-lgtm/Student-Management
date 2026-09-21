from django.urls import path
from student_app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("student_list/", views.StudentListView.as_view(), name="student_list"),
    path("create/", views.StudentCreateView.as_view(), name="create_student"),
    path("detail/<int:pk>/", views.StudentDetailView.as_view(), name="detail_student"),
    path("update/<int:pk>/", views.StudentUpdateView.as_view(), name="update_student"),
    path("delete/<int:pk>/", views.StudentDeleteView.as_view(), name="delete_student"),
    path("login/", views.StudentLoginView.as_view(), name="login"),
    path("logout/", views.StudentLogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("reset_password/", auth_views.PasswordResetView.as_view(), name="reset_password"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
]
    

# template_name="registration/password_reset_form.html"
# template_name="registration/password_reset_done.html"
# template_name="registration/password_reset_confirm.html"
# template_name="registration/password_reset_complete.html"