from django.urls import re_path
from django.urls import path
from . import views


app_name = "student_portal"

urlpatterns = [
    path("", views.sign_in, name="sign-in"),
    re_path(r"^sign-up", views.sign_up, name="sign-up"),
    re_path(r"^sign-out", views.sign_out, name="sign-out"),
    re_path(r"^account", views.AccountView.as_view(), name="account"),
]
