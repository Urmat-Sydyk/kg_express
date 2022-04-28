from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, CreateView

from .forms import LoginForm, UserRegisterForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return HttpResponse("Вы успешно вошли")
            else:
                return HttpResponse("Ваш аккаунт неактивен")
        return HttpResponse("Такого юзера не существует")

class UserRegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = "/"
