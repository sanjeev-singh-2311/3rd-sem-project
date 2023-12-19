from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# from .forms import RegistrationForm
from .models import UserData

class LoginPageView(TemplateView):
	template_name = "login.html"
	# TODO -> Make the login form work

class RegistrationPageView(TemplateView):
	template_name = "register.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):

		# TODO -> Make a validation system for the data
		# TODO -> Try to use a custom form for this
		# if form.is_valid():
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password1')  # TODO -> also ger password2 + Implement password hashing

		if (not all([username, email, password])):
			return HttpResponse("Empty fields are not allowed")

		data_entry = UserData(username=username, email=email, password=password)
		data_entry.save()
		return HttpResponse("Registration successful")