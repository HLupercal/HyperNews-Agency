from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from resume.views import Resume
from vacancy.views import Vacancy

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/home.html")

class CreateResumeView(View):
    def post(self, request, *args, **kwargs):
        is_authenticated = request.user.is_authenticated
        if is_authenticated:
            desc = request.POST.get("description")
            Resume.objects.create(description=desc,
                                  author=request.user)
            return redirect("/home")
        else:
            raise PermissionDenied()

class CreateVacancyView(View):
    def post(self, request, *args, **kwargs):
        is_manager = request.user.is_staff
        is_authed = request.user.is_authenticated
        if is_authed and is_manager:
            desc = request.POST.get("description")
            Vacancy.objects.create(description=desc, author=request.user)
            return redirect("/home")
        else:
            raise PermissionDenied()