from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"placeholder": "Email"}))

    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Username"}))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Password"}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Confirm Password"}))


    class Meta:
        model = Account
        fields = ["email", "username", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            Account.objects.get(email=email)
        except:
            return email
        raise forms.ValidationError("This email is exist. Please enter another email")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Account.objects.get(username=username)
        except:
            return username
        raise forms.ValidationError("This username is exist. Please enter another username")


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Password"}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"placeholder": "Email"}))

    class Meta:
        model = Account
        fields = [
            "email",
            "password",
            ]

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Password and Email Not Matched!")


class ProfileForm(forms.Form):
    user = forms.HiddenInput()
    firstname = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "First Name"}))

    lastname = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Last Name"}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "email"}))



