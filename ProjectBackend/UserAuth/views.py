from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegistrationForm, LoginForm
from .models import UserData
from django.shortcuts import redirect
# from django.contrib.auth import authenticate, login


class LoginPageView(TemplateView):
    template_name = "login.html"
    # TODO -> Make the login form work

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        resp = form.formAuth()

        if resp["status"]:
            request.session['user-name'] = form.username
            return redirect("HomePage:home-page")


class RegistrationPageView(TemplateView):
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        # TODO -> Make a validation system for the data
        # TODO -> Try to use a custom form for this
        # if form.is_valid():
        # username = request.POST.get('username')
        # email = request.POST.get('email')
        # password = request.POST.get('password1')  # TODO -> also ger password2 + Implement password hashing

        form = RegistrationForm(request.POST)
        print(request.POST)

        form_check = form.is_valid()

        if form_check["status"]:
            UserData.enterData(form)

        return HttpResponse(form_check["error"])
