from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.sign_up, name="signup"),
    path("record/<int:pk>", views.patient_record, name="record"),
    path("add/", views.add_patient, name="add_record"),
    path("delete/<int:pk>", views.delete_patient, name="delete_record"),
 ]
