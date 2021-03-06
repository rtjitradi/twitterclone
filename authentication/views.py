from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView

from authentication.forms import SignupForm, LoginForm
from twitteruser.models import CustomUserModel


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signup_data = form.cleaned_data
            new_user = CustomUserModel.objects.create(
                username=signup_data.get('username'),
                password=signup_data.get('password'),
                # email=signup_data.get('email')
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, 'generic_form.html', {'page_title': 'TwitterClone: Signup Form', 'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('homepage')))

    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('homepage'))


class LogoutView(TemplateView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('homepage'))
