from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View

from resume.models import Resume
# Create your views here.

class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, "resume/resumes.html",
                      context={"resumes": resumes})

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

