from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect


class HomePageView(TemplateView):
    template_name = "homepage.html"
