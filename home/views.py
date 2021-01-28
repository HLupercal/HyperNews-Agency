from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from resume.views import Resume

class HomeView(View):
    def get(self, request, *args, **kwargs):
        is_authenticated = request.user.is_authenticated
        if is_authenticated:
            return render(request, "home/home.html")

class CreateResumeView(View):
    def post(self, request, *args, **kwargs):
        is_authenticated = request.user.is_authenticated
        if is_authenticated:
            desc = request.POST.get("description")
            Resume.objects.create(description=desc,
                                  author=request.user)
            return redirect("/")
        else:
            raise PermissionDenied()