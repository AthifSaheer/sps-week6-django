from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
    }), label="Username")
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "input",
        "type": "text",
    }), label="Email")
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        "type": "password",
    }), label="Password")
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        "type": "password",
    }), label="Confirmation Password")

    # class Meta:
    #     model = 'User'
    #     feilds = ['username']

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Username already exists")
        return uname

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
    }), label="Username")
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input",
        "type": "password",
    }), label="Password")

class UserRegistrationFormForAdmin(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
    }), label="Username")
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "input",
        "type": "text",
    }), label="Email")

    class Meta:
        model = User
        fields = ['username', 'email']