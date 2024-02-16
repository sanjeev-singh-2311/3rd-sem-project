from django.urls import path, include
from .views import LoginPageView, RegistrationPageView, logout_view

urlpatterns = [
    path("login/", LoginPageView.as_view(), name="login-page"),
    path("register/", RegistrationPageView.as_view(), name="register-page"),
    path('logout/', logout_view, name='logout'),
    # path("register/submit/", )
]
