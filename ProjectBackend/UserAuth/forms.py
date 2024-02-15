from .models import UserData
import re


class LoginForm:

    def __init__(self, post):
        self.username = post.get("username")
        self.password = post.get("password")

    def formAuth(self):
        try:
            db = UserData.objects.get(username=self.username)
            if not db.password == self.password:
                return {"error": "Password Mismatch", "status": False}
        except UserData.DoesNotExist:
            return {"error": "User doesn't exist", "status": False}

        return {"error": "Login successful", "status": True}


class RegistrationForm:  # ! NOT TO BE USED RIGHT NOW, NEEDS COMPLETION

    def __init__(self, post):
        self.username = post.get('username')
        self.email = post.get('email')
        self.password = post.get('password1')
        self.repPassword = post.get('password2')

    def is_valid(self):
        if not (self.password == self.repPassword):
            # * Check if the Password and repeated passwords don't match
            return {"error": "Password doesn't match Repeted Password",
                    "status": False}

        try:
            username_valid = UserData.objects.get(username=self.username)
        except UserData.DoesNotExist:
            username_valid = None

        if username_valid is not None:
            return {"error": "Username already exists", "status": False}
        email_pat = re.compile(r"^\w+@\w+.\w+$")
        print(re.match(email_pat, self.email))
        if re.match(email_pat, self.email) is None:
            return {"error": "Email is invalid", "status": False}

        return {"error": "Registration successful", "status": True}

# ! NOT TO BE USED RIGHT NOW, NEEDS COMPLETION
