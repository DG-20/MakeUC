from django.urls import re_path
from . import views


app_name = "api"
urlpatterns = [
    re_path(r"^cart", views.CartView.as_view(), name="cart"),
    re_path(r"^payment", views.payment, name="payment"),
    re_path(r"^student_portal", views.student_portal, name="student_portal")
]
