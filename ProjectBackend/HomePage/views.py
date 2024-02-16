from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect


class HomePageView(TemplateView):
    template_name = "homepage.html"

    def get(self, request):
        print(request.session["username"])
        return render(request, self.template_name)

def printSess(request):
    print(request.session['username'])
