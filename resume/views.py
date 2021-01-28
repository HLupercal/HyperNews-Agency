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


