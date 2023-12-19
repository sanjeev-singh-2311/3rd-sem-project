from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# from .forms import RegistrationForm
from .models import UserData

# Create your views here.
class LoginPageView(TemplateView):
	template_name = "login.html"

class RegistrationPageView(TemplateView):
	template_name = "register.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		# if form.is_valid():
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password1')  # Use password1 as it's the hashed password

		if (not all([username, email, password])):
			return HttpResponse("Empty fields are not allowed")

		data_entry = UserData(username=username, email=email, password=password)
		data_entry.save()
		return HttpResponse("Registration successful")

            # You might want to redirect to a success page after registration
            # return render(request, "registration_success.html")