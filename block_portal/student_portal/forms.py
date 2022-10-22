from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

# Hedera form.
class UserForm(UserCreationForm):
    """
    Form that uses built-in UserCreationForm to handel user creation
    """

    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Your first name.."}),
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Your last name.."}),
    )
    username = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Email.."}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "*Password..", "class": "password"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "*Confirm Password..", "class": "password"}
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


# Our form.
class UserProfileForm(forms.ModelForm):
    """
    Basic model-form for our user profile that extends Django user model.
    """

    phone_number = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Phone Number"}),
    )
    address = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*First line of address"}),
    )
    town = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Town or City"}),
    )
    province = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Province"}),
    )
    postal_code = forms.CharField(
        max_length=8,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Postal Code"}),
    )
    country = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Country"}),
    )
    uni = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*University"}),
    )
    student_number = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Student #"}),
    )

    class Meta:
        model = UserProfile
        fields = (
            "phone_number",
            "address",
            "town",
            "province",
            "postal_code",
            "country",
            "uni",
            "student_number",
        )


class AuthForm(AuthenticationForm):
    """
    Form that uses built-in AuthenticationForm to handel user auth
    """

    username = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "*Email"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "*Password", "class": "password"}
        )
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )
