from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = "User profiles"
        ordering = ["-timestamp"]

    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(
        verbose_name="Address", max_length=100, null=True, blank=True
    )
    town = models.CharField(
        verbose_name="Town/City", max_length=100, null=True, blank=True
    )
    province = models.CharField(
        verbose_name="Province", max_length=100, null=True, blank=True
    )
    postal_code = models.CharField(
        verbose_name="Postal Code", max_length=8, null=True, blank=True
    )
    country = models.CharField(
        verbose_name="Country", max_length=100, null=True, blank=True, default="Canada"
    )
    uni = models.CharField(
        verbose_name="University", max_length=100, null=True, blank=True
    )
    student_number = models.CharField(
        max_length=100, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)

    acc = models.CharField(max_length=20, null=True, blank=True)
    pubkey = models.CharField(max_length=200, null=True, blank=True)
    privatekey = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"
