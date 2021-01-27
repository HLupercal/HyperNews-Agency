from django.shortcuts import render

# Create your views here.\
from django.views import View


class MainMenuView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "menu/menu.html", context={"context": []})
