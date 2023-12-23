from django.db import models

# Create your models here.
class UserData(models.Model):
	# Username as the Primary Key of the model
	username = models.CharField(primary_key = True, max_length=100, verbose_name = "User Name")
	
	email = models.EmailField(max_length=254, verbose_name = "User Email")
	password = models.CharField(max_length=100, verbose_name = "Password")

	class Meta:
		verbose_name = "User Data" # Human readable version for table name in the database 
		verbose_name_plural = "User Datas"
	
	def enterData(form):
		data = UserData()
		data.username = form.username
		data.email = form.email
		data.password = form.password

		data.save()

	def __str__(self):
		return f"{self.username}"

	def get_absolute_url(self):
		return reverse("UserData_detail", kwargs={"pk": self.pk})
