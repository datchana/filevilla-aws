from django import forms
from django.core.validators import RegexValidator

alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, validators=[alpha])
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def validate(self, password, confirm_password):
        if password == confirm_password:
            return True
        else:
            return False

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)