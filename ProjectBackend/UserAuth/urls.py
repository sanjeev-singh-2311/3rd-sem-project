from django.urls import path, include
from .views import LoginPageView

urlpatterns = [
	path("login/", LoginPageView.as_view(), name="login-page")
]
