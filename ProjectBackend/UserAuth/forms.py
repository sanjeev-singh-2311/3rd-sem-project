from .models import UserData
import re

# ! NOT TO BE USED RIGHT NOW, NEEDS COMPLETION
class RegistrationForm:
	def __init__(self, post):
		self.username = post.get('username')
		self.email = post.get('email')
		self.password = post.get('password1')
		self.repPassword = post.get('password2')

	def is_valid(self):
		if not (self.password == self.repPassword):
			# * Check if the Password and repeated passwords don't match
			return {"error" : "Password doesn't match Repeted Password", "status" : False}

		try:
			username_valid = UserData.objects.get(username=self.username)
		except:
			username_valid = None
		
		if username_valid is not None:
			return {"error" : "Username already exists", "status" : False}
		email_pat = re.compile(r"^\w+@\w+.\w+$")
		print(re.match(email_pat,self.email))
		if re.match(email_pat, self.email) is None:
			return {"error" : "Email is invalid", "status" : False}

		
		return {"error" : "Registration successful", "status" : True}

# ! NOT TO BE USED RIGHT NOW, NEEDS COMPLETION