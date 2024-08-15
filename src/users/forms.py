from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomInvitation, CustomUser


class SendResidentInvitationForm(forms.ModelForm):
    class Meta:
        model = CustomInvitation
        fields = ["email", "building"]
        labels = {"email": "Email", "building": "Building"}


class SendPropertyManagerInvitationForm(forms.ModelForm):
    class Meta:
        model = CustomInvitation
        fields = ["email"]
        labels = {"email": "Email"}


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        labels = {
            "username": "Username",
            "first_name": "First name",
            "last_name": "Last name",
            "email": "Email",
        }

        error_messages = {
            "username_exists": "User with this username already exists!",
            "email_exists": "User with this email already exists!",
            "password_mismatch": "The two password fields didn't match.",
            "first_name_required": "This field is required.",
            "last_name_required": "This field is required.",
            "email_required": "This field is required.",
        }

    def clean_username(self):
        username = self.cleaned_data["username"]
        if username and CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(self.Meta.error_messages["username_exists"], code="username_exists")
        return username

    def clean_first_name(self):
        if self.cleaned_data["first_name"]:
            return self.cleaned_data["first_name"].capitalize()
        raise forms.ValidationError(self.Meta.error_messages["first_name_required"], code="first_name_required")

    def clean_last_name(self):
        if self.cleaned_data["last_name"]:
            return self.cleaned_data["last_name"].capitalize()
        raise forms.ValidationError(self.Meta.error_messages["last_name_required"], code="last_name_required")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email:
            if CustomUser.objects.filter(email=email).exists():
                raise forms.ValidationError(self.Meta.error_messages["email_exists"], code="email_exists")
            return email.lower()
        raise forms.ValidationError(self.Meta.error_messages["email_required"], code="email_required")
