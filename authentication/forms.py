from django import forms


class SignupForm(forms.Form):
    email = forms.EmailField
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)
