from django import forms

class LoginForm(forms.Form):
	username = forms.CharField('username', max_length=100, required=True)
	password = forms.CharField('password', max_length=100, required=True)
