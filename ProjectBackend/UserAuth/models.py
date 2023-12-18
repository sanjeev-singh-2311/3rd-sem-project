from django.db import models

# Create your models here.
class UserData(models.Model):

	username = models.TextField(verbose_name = "User Name")
	email = models.EmailField(max_length=254, verbose_name = "User Email")
	password = models.TextField(verbose_name = "Password")

	class Meta:
		verbose_name = "User Data"
		verbose_name_plural = "User Datas"

	def __str__(self):
		return f"{self.username}	{self.email}"

	def get_absolute_url(self):
		return reverse("UserData_detail", kwargs={"pk": self.pk})
