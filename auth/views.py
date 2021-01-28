from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "signup.html"
