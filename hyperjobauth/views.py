from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView

# Create your views here.
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "signup.html"


class SignInView(LoginView):
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = "signin.html"

