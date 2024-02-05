from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.sign_up, name="signup"),
    path("record/<int:pk>", views.patient_record, name="record"),
 ]
