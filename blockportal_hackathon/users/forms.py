from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserForm(UserCreationForm):
    """
    Form that uses built-in UserCreationForm to handel user creation
    """

    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter First Name"}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter Last Name"}),
    )
    username = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter Email"}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Password", "class": "password"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Password", "class": "password"}
        )
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )


class UserProfileForm(forms.ModelForm):
    """
    Basic model-form for our user profile that extends Django user model.
    """

    telephone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter Phone Number"}),
    )
    address = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter Address"}),
    )
    town = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter City"}),
    )
    county = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter Country"}),
    )

    post_code = forms.CharField(
        max_length=8,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter Postal Code"}),
    )

    class Meta:
        model = UserProfile
        fields = (
            "telephone",
            "address",
            "town",
            "county",
            "post_code",
        )


class AuthForm(AuthenticationForm):
    """
    Form that uses built-in AuthenticationForm to handel user auth
    """

    username = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Enter Email"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter Password", "class": "password"}
        )
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )
