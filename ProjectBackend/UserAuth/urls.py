from django.urls import path, include
from .views import LoginPageView, RegistrationPageView

urlpatterns = [
    path("login/", LoginPageView.as_view(), name="login-page"),
    path("register/", RegistrationPageView.as_view(), name="register-page"),
    # path("register/submit/", )
]
