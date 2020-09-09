from django.contrib.auth.forms import UserCreationForm, UserChangeForm  # https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/

from twitteruser.models import CustomUserModel


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUserModel
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUserModel
        fields = ('username', 'email')
