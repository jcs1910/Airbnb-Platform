from django.views import View
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse

from users.forms import LoginForm, SignUpForm

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            email    = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user     = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})

def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))

class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("core:home")
    initial = {
        'first_name': 'Lee',
        'last_name' : 'yoon',
        'email' : 'lee@naver.com',
    }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("eemail")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
