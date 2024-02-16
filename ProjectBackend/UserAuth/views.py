from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RegistrationForm, LoginForm
from .models import UserData
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


class LoginPageView(TemplateView):
    template_name = "login.html"
    # TODO -> Make the login form work

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        print(request)
        form = LoginForm(request.POST)
        auth_json = form.formAuth()
        if auth_json["status"]:
            request.session['username'] = form.username
            print("Here")
            return redirect("home-page")
        return redirect('login-page')

        # user = authenticate(request, username=form.username, password=form.password)

        # if user:
        #     login(request, user)
        #     return redirect("HomePage:home-page")
        # else:
        #     return redirect("login-page")


def logout_view(request):
    if request.session.get('username'):
        p = request.session['username']
        del request.session['username']
    return redirect('login-page', {'username': p})


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
