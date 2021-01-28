from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View

from vacancy.models import Vacancy


# Create your views here.
class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, "vacancy/vacancies.html",
                      context={"vacancies": vacancies})


