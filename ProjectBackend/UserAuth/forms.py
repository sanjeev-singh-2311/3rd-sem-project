from .models import UserData

# ! NOT TO BE USED RIGHT NOW, NEEDS COMPLETION
class RegistrationForm:
	def __init__(self, username, email, password1, password2):
		self.username = username
		self.email = email
		self.password = password1
		self.repPassword = password2

	def is_valid(self):
		if not (self.password == self.repPassword):
			return False
		return True

# ! NOT TO BE USED RIGHT NOW, NEEDS COMPLETION