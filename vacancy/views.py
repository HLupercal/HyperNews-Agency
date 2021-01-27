from django.shortcuts import render
from django.views import View


from vacancy.models import Vacancy

# Create your views here.
class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        print("Asdasdas")
        return render(request, "vacancy/vacancies.html",
               context={"vacancies": vacancies})
